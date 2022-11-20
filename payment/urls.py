from django.urls import path
from .views import purchase_item, get_item_page, success_purchase, cancel_purchase

urlpatterns = [
    path('buy/<int:pk>', purchase_item),
    path('item/<int:pk>', get_item_page),
    path('success', success_purchase),
    path('cancel', cancel_purchase),
]
