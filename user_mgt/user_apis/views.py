from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .parse import UserJsonParse


@api_view(['GET'])
def get_all_user(request):
    users = User.objects.all()
    serializer = UserJsonParse(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    getuser = User.objects.filter(name=request.data['name'])
    if getuser.exists():
        return Response("User Name Exist, Try Another One", status=status.HTTP_400_BAD_REQUEST)

    user = UserJsonParse(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_by_id(request, uid):
    try:
        getuser = User.objects.get(id=uid)
    except User.DoesNotExist:
        return Response("User Not Found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user = UserJsonParse(getuser)
        return Response(user.data)

    elif request.method == 'PUT':
        updated_user = UserJsonParse(getuser, data=request.data)
        if updated_user.is_valid():
            updated_user.save()
            return Response(updated_user.data, status=status.HTTP_200_OK)
        return Response(updated_user.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        getuser.delete()
        return Response('User Deleted Successfully', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def user_by_name(request):
    name = request.GET.get('name')
    try:
        getuser = User.objects.get(name=name)
    except User.DoesNotExist:
        return Response("User Not Found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user = UserJsonParse(getuser)
        return Response(user.data)

    elif request.method == 'PUT':
        updated_user = UserJsonParse(getuser, data=request.data)
        if updated_user.is_valid():
            updated_user.save()
            return Response(updated_user.data, status=status.HTTP_200_OK)
        return Response(updated_user.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        getuser.delete()
        return Response('User Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
