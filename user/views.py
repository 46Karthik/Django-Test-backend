from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User,Profile
from .serializers import UserSerializer,profileSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import secrets

def generate_api_key(length=32):
    secrets_api_key = secrets.token_hex(length)
    return secrets_api_key

@api_view(['GET'])
def example_view(request,userid):
    api_key = request.GET.get('api_key', '')
    if request.method == 'GET':
        if userid:
            found = get_object_or_404(User,userid=userid)
            serializer = UserSerializer(found).data
            keyfound = serializer.get("apikey")
            # return Response(serializer, status=status.HTTP_200_OK)
            if keyfound == api_key:
                profile = get_object_or_404(Profile, id=userid)
                finaldata = profileSerializer(profile).data
                return Response(finaldata, status=status.HTTP_200_OK)
            else:
                response = HttpResponse(f"Error = api_key is Wrong")
                return response


    # response = HttpResponse(f"API Key: {api_key},{id},{key}")
    # return response
@api_view(['GET'])
def apidetails(request,userid=None):
    print("data found")
    if request.method == 'GET':
        if userid:
            # Retrieve data for a specific user by username
            found = get_object_or_404(User,userid=userid)
            serializer = UserSerializer(found).data
            # print(serializer.data,"dataaaaaaaaaaaa")
            return Response(serializer, status=status.HTTP_200_OK)
            # return Response(serializer.data)
            # print(userid)
        # else:
        #     # Retrieve data for all profiles
        #     profiles = Profile.objects.all()
        #     serializer = profileSerializer(profiles, many=True)
        

class UserCreate(APIView):
    def post(self, request):
        data = request.data
        userid = data.get('userid')
        apikey  = data.get('apikey')
        # 1st type to create data
        # user = User.objects.create(name=name)

        #2st type to create data
        # user = User()
        # user.name = name
        # user.save()
        #3st type to create data
        user = User(userid=userid,apikey=apikey)
        user.save()
    

        output = {
           "userid": user.userid,
           "apikey": user.apikey
        }
        # print(name)
        # Return a success response with the created user's data
        # return Response({'message': 'User created successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(data=output, status=status.HTTP_201_CREATED)
    # def get(self, request):
    #     userdata = User.objects.all()
    #     data =UserSerializer(userdata,many=True).data
    #     # serialized_data = data
    #     return Response(data=data, status=status.HTTP_200_OK)

    # def put(self, request):
    # def post(self, request):