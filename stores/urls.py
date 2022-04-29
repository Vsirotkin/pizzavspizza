from django.urls import path

from .views import *


urlpatterns = [
    path('', PizzeriaListAPIView.as_view(), name='pizzeria_list'),
    path('<int:id>/', PizzeriaRetrieveAPIView.as_view(), name='pizzeria_detail'),
]
