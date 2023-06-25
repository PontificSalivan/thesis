from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    pagination_class = None


class EmployeeFilterMixin:
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('last_name', openapi.IN_QUERY,
                          description='Filter by last name (if full_name contains it)',
                          type=openapi.TYPE_STRING),
        openapi.Parameter('department__id', openapi.IN_QUERY,
                          description='Filter by department ID (exact match)',
                          type=openapi.TYPE_INTEGER),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class EmployeeViewSet(EmployeeFilterMixin, viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        last_name = self.request.query_params.get('last_name', None)
        department_id = self.request.query_params.get('department__id', None)
        if last_name:
            queryset = queryset.filter(full_name__icontains=last_name)
        if department_id:
            queryset = queryset.filter(department=department_id)
        return queryset
