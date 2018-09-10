from django.shortcuts import render
from django.views.generic import TemplateView
from generator.forms import AddCategoryForm, AddHashtagForm
from categories.models import User, Category

def home(request):
    return render(request, 'generator/home.html')

class AddCategoryOrHashtag(TemplateView):
    template_name = 'generator/add.html'

    def get(self, request):

        category_form = AddCategoryForm()
        hashtag_form = AddHashtagForm(user_id=request.user.id)
        args = {'category_form':category_form, 'hashtag_form':hashtag_form}
        return render(request, self.template_name, args)

    def post(self, request):
        hashtag_form = AddHashtagForm(user_id=request.user.id)
        category_form = AddCategoryForm()

        args = {
            'category_form': category_form,
            'hashtag_form': hashtag_form,
        }

        if 'category_form' in request.POST:
            category_form = AddCategoryForm(request.POST)
            if category_form.is_valid():
                category = category_form.save(commit=False)
                category.user_id_id = request.user.id
                category.save()
                category_name = category_form.cleaned_data['category_name']
                args['category_name'] = category_name

        elif 'hashtag_form' in request.POST:
            hashtag_form = AddHashtagForm(request.POST, user_id=request.user.id)
            if hashtag_form.is_valid():
                hashtag = hashtag_form.save(commit=False)
                hashtag.category_id_id = hashtag_form.cleaned_data['category_id'].category_id
                hashtag.save()
                hashtag_name = hashtag_form.cleaned_data['hashtag']
                args['hashtag'] = hashtag_name

        return render(request, self.template_name, args)
