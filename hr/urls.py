from django.contrib import admin
from django.urls import include, path

from hr.views import DocViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('doc', DocViewSet ,basename='doc')

urlpatterns = [
    path('',include(router.urls))
]
