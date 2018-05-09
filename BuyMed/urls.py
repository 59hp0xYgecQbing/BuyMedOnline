from django.urls import path
from . import views

app_name='BuyMed'
urlpatterns=[
	path(r'^$',views.product_list,name='product_list'),
	path(r'^(?P<category_slug>[-\w]+)/$',views.product_detail,name='product_detail'),
]