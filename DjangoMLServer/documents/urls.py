from rest_framework import routers
from django.urls import include, path   
from documents.views import DocumentViewSet

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]