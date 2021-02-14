from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('count', views.welcome, name='welcome'),
    path('<int:server_id>/', views.server, name="server"),
]