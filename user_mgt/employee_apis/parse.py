from rest_framework import serializers

from .models import Employee, EmployeeReview


class EmployeeJsonParse(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'department', 'phone', 'email', 'isActive']


class EmployeeReviewJsonParse(serializers.ModelSerializer):
    class Meta:
        model = EmployeeReview
        fields = ['id', 'reviewer_id', 'employee_id', 'review']