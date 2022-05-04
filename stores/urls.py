from django.urls import path

from .views import *


urlpatterns = [
    path('', PizzeriaListAPIView.as_view(), name='pizzeria_list'),
    path('detail/<int:id>/', PizzeriaRetrieveAPIView.as_view(), name='pizzeria_detail'),
    path('create/', PizzeriaCreateAPIView.as_view(), name='pizzeria_create'),
    path('update/<int:id>/', PizzeriaRetrieveUpdateAPIView.as_view(), name='pizzeria_update'),
    path('delete/<int:id>/', PizzeriaDestroyAPIView.as_view(), name='pizzeria_delete'),
]

