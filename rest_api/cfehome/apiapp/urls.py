from django.contrib import admin
from django.urls import path
from .views import CafeList, CafeDetail, CafeRating, Endpoints

urlpatterns = [
    path('', Endpoints.as_view(), name='endpoints'),
    path('cafes/', CafeList.as_view(), name='all'),
    path('cafes/name/<str:name>', CafeDetail.as_view(), name='detail'),
    path('cafes/rating/<path:rating>/', CafeRating.as_view(), name='rating'),
]
