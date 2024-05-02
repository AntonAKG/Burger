from django.views.generic import TemplateView, ListView
import requests

from shop.models import Categories


class IndexView(ListView):
    model = Categories
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Головна сторінка"
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"


class Weather(TemplateView):
    template_name = "main/weather.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Погода"

        api_key = "651cd2b38e940e9e3a22687d11e20d38"
        city_name = "Kyiv"

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

        res = requests.get(url)
        data = res.json()

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        context["humidity"] = humidity
        context["pressure"] = pressure
        context["wind"] = wind
        context["description"] = description
        context["temp"] = temp
        context["city"] = city_name

        return context
