from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('natives', views.NativeViewSet, basename='native')
router.register('cohort', views.CohortViewSet, basename='cohort')

urlpatterns = [
    path('', include(router.urls))
]
