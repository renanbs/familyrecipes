from django.conf.urls import url
from .views import IngredientsList


urlpatterns = [

    url(r'^$', IngredientsList.as_view(), name="ingredient_list"),
    # url(r'^create/$', control_create),
    # url(r'^(?P<id>\d+)/$', group_detail, name="detail"),
    # url(r'^(?P<id>\d+)/edit/$', group_update, name="update"),
    # url(r'^(?P<id>\d+)/delete/$', group_delete),
]
