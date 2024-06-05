from django.urls import path
from .views import login,register, ProductApiView, ProductCategoryApiView,DepartmentApiView,SupplierApiView,ProductCategoryDetailApiView

urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('product/',ProductApiView.as_view({'get':'list','post':'create'}),name='product'),
    path('product/<int:pk>/',ProductApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='product-details'),
    path('product-category/',ProductCategoryApiView.as_view(),name='product-category'),
    path('product-category/<int:pk>/',ProductCategoryDetailApiView.as_view(),name='product-category'),
    path('department/',DepartmentApiView.as_view(),name='department'),
    path('supplier/',SupplierApiView.as_view(),name='supplier'),

    
]
   