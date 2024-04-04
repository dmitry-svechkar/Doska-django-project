from django.forms import ModelForm
from multiupload.fields import MultiFileField

from goods.models import Goods, GoodsPhoto


class AddGoodForm(ModelForm):
    """ Форма для заполнения полей товаров. """
    good_photos = MultiFileField()

    class Meta:
        model = Goods
        fields = (
            'good_name',
            'model',
            'condition',
            'in_stock',
            'good_cost',
            'description',
            'good_category',
        )

    def save(self, commit=True):
        instance = super(AddGoodForm, self).save(commit)
        for photo in self.cleaned_data['good_photos']:
            GoodsPhoto.objects.create(good_photo=photo, good=instance)
        return instance
