from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='spaces'),

    path('<int:space_id>', views.space, name='space'),

    path('search', views.search, name='search'),

]