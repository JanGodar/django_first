from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('category/<int:cat_id>/', views.show_category, name='category')
]