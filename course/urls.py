from course.views import ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView, ProductUpdateNew
from django.urls import path


urlpatterns = [
    path('', ProductListView.as_view(), name = 'product_list'),
    path('product/create', ProductCreateView.as_view(), name = 'product_create'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name ='product_detail'),
    path('product/<int:product_id>/edit', ProductUpdateNew.as_view(), name ='product_edit'),
    path('product/<int:product_id>/delete', ProductDeleteView.as_view(), name ='product_delete'),



]