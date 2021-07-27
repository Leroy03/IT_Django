from django.urls import path
from templates.rango import views
app_name = 'rango'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),

]
