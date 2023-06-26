from django_filters import filters, filterset

from .models import Employee


class EmployeeFilterSet(filterset.FilterSet):
    full_name = filters.CharFilter(lookup_expr='icontains', field_name='full_name')

    class Meta:
        model = Employee
        fields = [
            'full_name',
            'department',
        ]
