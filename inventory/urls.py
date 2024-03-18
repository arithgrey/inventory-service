from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import InventoryView

router = DefaultRouter()
router.register(r'', InventoryView, basename='inventory')

urlpatterns = [
    path('', include(router.urls)),
]
