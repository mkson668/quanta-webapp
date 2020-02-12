from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view
)

urlpatterns = [
    path('product/', product_detail_view, name = 'product-detail-simple'),
    path('create/', product_create_view, name = 'product-create'), 
    path('<int:my_id>/', dynamic_lookup_view, name = 'product-detail'),
    path('<int:del_id>/delete/', product_delete_view, name = 'product-delete'),
    path('list/', product_list_view, name = 'product-list')
]
