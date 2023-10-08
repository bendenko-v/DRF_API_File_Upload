from django.urls import include, path
from files.views import FileViewSet, UploadView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'files', FileViewSet)

urlpatterns = [
    path('upload/', UploadView.as_view(), name='upload_view'),
    path('', include(router.urls)),
]
