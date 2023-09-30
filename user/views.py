from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserCreate(APIView):
    def post(self, request):
        data = request.data
        name = data.get('name')

        # 1st type to create data
        # user = User.objects.create(name=name)

        #2st type to create data
        # user = User()
        # user.name = name
        # user.save()
        #3st type to create data
        user = User(name=name)
        user.save()
        output = {
           "name": user.name
        }
        print(name)
        # Return a success response with the created user's data
        # return Response({'message': 'User created successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(data=output, status=status.HTTP_201_CREATED)
    def get(self, request):
        userdata = User.objects.all()
        data =UserSerializer(userdata,many=True).data
        # serialized_data = data
        return Response(data=data, status=status.HTTP_200_OK)
    # def put(self, request):
    # def post(self, request):