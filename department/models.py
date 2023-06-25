from django.db import models
from django.core.exceptions import ValidationError


def validate_director(director_id):
    employee = Employee.objects.filter(id=director_id).first()
    if employee.position != Employee.PositionChoices.DIRECTOR:
        raise ValidationError('Директором департамента может быть только сотрудник с должностью директор')


class Department(models.Model):
    name = models.CharField('Название', max_length=200)
    director = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True, blank=True,
                                    validators=[validate_director],
                                    related_name='director_department')

    def __str__(self):
        return self.name


class Employee(models.Model):
    class PositionChoices(models.TextChoices):
        DIRECTOR = 'DR'
        OTHER = 'OT'

    full_name = models.CharField('ФИО', max_length=200)
    photo = models.ImageField('Фото', upload_to='images', null=True, blank=True)
    position = models.CharField('Должность', choices=PositionChoices.choices, max_length=2,
                                default=PositionChoices.OTHER)
    salary = models.DecimalField('Оклад', max_digits=50, decimal_places=2)
    age = models.PositiveIntegerField('Возраст')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.full_name
