from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tempview/', views.html_template),
    path('htmlview/', views.html_view, name='html_view'),
    path('<name>/', views.detail),
]