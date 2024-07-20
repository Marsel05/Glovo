from django.urls import path
from .views import *

urlpatterns = [
    path('userprofile/', UserProfileViewSet.as_view({'get': "list", 'post': 'create'}), name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'destroy': 'delete'}),
         name='userprofile_detail'),

    path('category/', CategoryViewSet.as_view({'get': "list", 'post': 'create'}), name='category'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'destroy': 'delete'}),
         name='category_detail'),

    path('food/', FoodViewSet.as_view({'get': "list", 'post': 'create'}), name='food_list'),
    path('food/<int:pk>/', FoodViewSet.as_view({'get': 'retrieve', 'put': 'update', 'destroy': 'delete'}),
         name='food_detail'),

    path('courier/', CourierViewSet.as_view({'get': "list", 'post': 'create'}), name='courier_list'),
    path('courier/<int:pk>/', CourierViewSet.as_view({'get': 'retrieve', 'put': 'update', 'destroy': 'delete'}),
         name='courier_detail'),

    path('order/', OrderViewSet.as_view({'get': "list", 'post': 'create'}), name='order_list'),
    path('order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'destroy': 'delete'}),
         name='order_detail'),

    path('delivery/', DeliveryViewSet.as_view({'get': "list", 'post': 'create'}), name='delivery_list'),
    path('delivery/<int:pk>/', DeliveryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'destroy': 'delete'}),
         name='delivery_detail'),

    path('rating/', RatingViewSet.as_view({'get': "list", 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'destroy': 'delete'}),
         name='rating_detail'),

    path('review/', ReviewViewSet.as_view({'get': "list", 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'destroy': 'delete'}),
         name='review_detail'),

]