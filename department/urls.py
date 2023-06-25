from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet

app_name = 'department'

router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = router.urls
