from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FacultyViewSet, GroupViewSet, DepartmentViewSet,
    SubjectViewSet, TeacherViewSet, StudentViewSet
)

router = DefaultRouter()
router.register(r'faculties', FacultyViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]