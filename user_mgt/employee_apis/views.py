from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .parse import EmployeeJsonParse, EmployeeReviewJsonParse


@api_view(['GET'])
def get_all_employee(request):
    employees = Employee.objects.all()
    serializer = EmployeeJsonParse(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_employee(request):

    employee = EmployeeJsonParse(data=request.data)
    if employee.is_valid():
        employee.save()
        return Response(employee.data, status=status.HTTP_201_CREATED)
    return Response(employee.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_by_id(request, eid):
    try:
        get_employee = Employee.objects.get(id=eid)
    except Employee.DoesNotExist:
        return Response("Employee Not Found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        employee = EmployeeJsonParse(get_employee)
        return Response(employee.data)

    elif request.method == 'PUT':
        updated_employee = EmployeeJsonParse(get_employee, data=request.data)
        if updated_employee.is_valid():
            updated_employee.save()
            return Response(updated_employee.data, status=status.HTTP_200_OK)
        return Response(updated_employee.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        get_employee.delete()
        return Response('Employee Deleted Successfully', status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def deactivate_employee(request, eid):

    try:
        get_employee = Employee.objects.get(id=eid)
    except Employee.DoesNotExist:
        return Response("Employee Not Found", status=status.HTTP_404_NOT_FOUND)

    deactivate = EmployeeJsonParse(get_employee, data=request.data)
    if deactivate.is_valid():
        deactivate.save()
        return Response(deactivate.data, status=status.HTTP_200_OK)
    return Response(deactivate.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_active_employees(request):
    employees = Employee.objects.filter(isActive=True)
    serializer = EmployeeJsonParse(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def give_review_employee(request):

    review = EmployeeReviewJsonParse(data=request.data)
    if review.is_valid():
        review.save()
        return Response(review.data, status=status.HTTP_200_OK)
    return Response(review.errors, status=status.HTTP_400_BAD_REQUEST)
