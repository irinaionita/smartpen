
from django.urls import path, include
from accounts.views import LoginCustomView
urlpatterns = [
    path('login/', LoginCustomView.as_view(), name='irina_login'),
]
