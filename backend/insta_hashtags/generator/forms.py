from django import forms
from categories.models import Category, Hashtag

class AddCategoryForm(forms.ModelForm):
    category_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].label= 'Category'

    class Meta:
        model = Category
        fields = ('category_name',)


class AddHashtagForm(forms.ModelForm):
    hashtag = forms.CharField()

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super(AddHashtagForm, self).__init__(*args, **kwargs)
        self.fields['hashtag'].label= 'Hashtag'
        self.fields['category_id'].label = 'Category'
        self.fields['category_id'].queryset = Category.objects.filter(user_id_id=user_id)

    class Meta:
        model = Hashtag
        fields = ('category_id','hashtag',)

