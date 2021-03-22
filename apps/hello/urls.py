from django.urls import path
from apps.hello import views

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
]