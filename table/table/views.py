from django.shortcuts import render
from django.views import View
from goods.models import GoodCategory
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@method_decorator(cache_page(60*1), name='dispatch')
class MainView(View):
    """
    Вью для отображения главной страницы сайта.
    """
    def get(self, request):
        category_list = GoodCategory.objects.all()
        return render(request, 'main.html', {'category_list': category_list})


def not_found(request, exception):
    return render(request, '404.html', status=404)
