from django.db.models import Sum
from rest_framework import serializers

from .models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    employees_number = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    def get_employees_number(self, obj):
        return obj.employees.count()

    def get_total_salary(self, obj):
        aggregate = obj.employees.aggregate(salary_sum=Sum('salary'))
        return aggregate.get('salary_sum')

    class Meta:
        model = Department
        fields = ('id', 'name', 'director', 'employees_number', 'total_salary')
