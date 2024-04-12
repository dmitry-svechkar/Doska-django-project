from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

from goods.forms import AddGoodForm, CheckoutForm
from goods.models import Carts, Goods, WishGoods, GoodCategory, Orders
from goods.tasks import send_new_good_notification
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


class CategoryView(ListView):
    model = GoodCategory
    template_name = 'site/goods_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = GoodCategory.objects.all()
        return context

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            return Goods.objects.filter(
                good_category__category_slug=category_slug
            )
        else:
            return Goods.objects.all()


@method_decorator(cache_page(60*1), name='dispatch')
class GoodsListView(ListView):
    """
    Вью для отображения списков товаров.
    Показываются только товары,
    прошедшие проверку модератора.
    """
    model = Goods
    paginate_by = 6
    template_name = 'site/goods_list.html'
    context_object_name = 'goods_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = GoodCategory.objects.all()

        return context


class GoodDetailView(DetailView):
    """ Вью страницы отображения товара. """
    model = Goods
    template_name = 'site/good_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class AddGoodsView(CreateView):
    """ Вью добавления товаров. """
    template_name = 'site/add_add.html'
    form_class = AddGoodForm
    model = Goods

    def form_valid(self, form):
        form.instance.seller = self.request.user
        good = form.save()
        send_new_good_notification.delay(good_id=good.id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('goods-list')


class AddToWishListView(View):
    """ Добавление товара в список желаемого. """
    def get(self, request, slug):
        good = get_object_or_404(Goods, slug=slug)
        _, created = WishGoods.objects.get_or_create(
            user=self.request.user, good=good)
        if not created:
            obj = WishGoods.objects.filter(user=self.request.user, good=good)
            obj.delete()
            return redirect('good-detail', slug=slug)
        else:
            return redirect('good-detail', slug=slug)


@method_decorator(cache_page(60*1), name='dispatch')
class WishListView(ListView):
    """ Вью отображения желаемых товаров. """
    model = WishGoods
    paginate_by = 3
    template_name = 'site/wishlist.html'
    context_object_name = 'wish_list'

    def get_queryset(self):
        return WishGoods.objects.filter(user=self.request.user)


class AddDeleteCartView(View):
    """ Вью добавления и удаления товаров из списка покупок. """
    def post(self, request, slug, quantity=1):
        good = get_object_or_404(Goods, slug=slug)
        _, created = Carts.objects.get_or_create(
            user=self.request.user, quantity=quantity, good=good)
        if not created:
            obj = Carts.objects.filter(user=self.request.user, good=good)
            obj.delete()
            return redirect('carts')
        else:
            return redirect('good-detail', slug=slug)


class CartView(ListView):
    """
    Вью отображения списка товаров в корзине.
    Реализована логика рассчета кол-ва товаров и общей суммы покупок.
    """
    model = Carts
    template_name = 'site/cart.html'
    context_object_name = 'cart_list'

    def get_queryset(self) -> QuerySet[Any]:
        return Carts.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        objs = Carts.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        count_obj = objs.count()
        total = sum(obj.good.good_cost for obj in objs)
        context['count_obj'] = count_obj
        context['total'] = total
        return context


class SuccessCart(TemplateView):
    template_name = 'site/order_complete.html'


class CheckoutCart(FormView):
    """ Вью логики оформления заказа. """
    template_name = 'site/checkout.html'
    model = Orders
    form_class = CheckoutForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        objs = Carts.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        count_obj = objs.count()
        total = sum(obj.good.good_cost for obj in objs)
        context['cart_list'] = Carts.objects.filter(user=self.request.user)
        context['count_obj'] = count_obj
        context['total'] = total
        context['total_with_delivery'] = total + 10
        return context

    def form_valid(self, form):
        orders_instance = form.save(commit=False)

        cart_items = Carts.objects.filter(user=self.request.user)
        orders_instance.save()
        orders_instance.cart.set(cart_items)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success_cart')
