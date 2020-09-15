from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',views.Product.as_view({'get':'list'})),
    path('getOneProduct/<int:pk>',views.Product.as_view({'get':'retrieve'})),
    path('insert/',views.Product.as_view({'post':'create'})),
    path('update/<int:pk>',views.Product.as_view({'put':'update'})),
    path('delete/<int:pk>',views.Product.as_view({'delete':'destroy'})),
]
