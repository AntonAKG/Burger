from django.urls import path, include

from account.views import LoginClassView, RegisterView, ProfileView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginClassView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

    ]