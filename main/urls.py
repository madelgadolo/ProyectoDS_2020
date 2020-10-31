from django.urls import path

from . import views

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
    path('productos', views.ProductListView.as_view(), name='producto_list'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='producto_detail'),
    path('registro/', views.RegistrationView.as_view(), name='register'),
]