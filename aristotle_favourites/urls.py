from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from aristotle_favourites import views

urlpatterns = patterns(
    'aristotle_favourites.views',
    url(r'^account/favourites/?$', views.all_folders, name='folders'),
    url(r'^account/favourites/f/(?P<folder_slug>.+)/toggle/?$', views.toggle_item_in_folder, name='toggle_in_folder'),
    url(r'^account/favourites/f/(?P<folder_slug>.+)/?$', views.view_folder, name='view_folder'),
    url(r'^account/favourites/quick/?$', views.quick_favourites, name='quick_favourites'),
    url(r'^account/favourites/add_folder/?$', views.add_folder, name='add_folder'),
)
