from django.views.generic import TemplateView, ListView

from shop.models import Categories


class IndexView(ListView):
    model = Categories
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'
