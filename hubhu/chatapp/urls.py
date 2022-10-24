from django.urls import path

from chatapp import views

app_name = 'chatapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index')
]