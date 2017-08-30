from django.conf.urls import url
from .views import RecipesList, RecipeDetail


urlpatterns = [

    url(r'^$', RecipesList.as_view(), name="recipes_list"),
    # url(r'^create/$', control_create),
    url(r'^(?P<id>\d+)/$', RecipeDetail.as_view(), name="detail"),
    # url(r'^(?P<id>\d+)/edit/$', group_update, name="update"),
    # url(r'^(?P<id>\d+)/delete/$', group_delete),
]
