from catalog.apps import CatalogConfig
from catalog.views import contact_inf, HomeListView, ProductListView, ProductDetailView
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contact_inf, name='contacts'),
    path('product/', ProductListView.as_view(), name='product'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
