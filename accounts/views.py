from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import jwt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class Login(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
        except:
            return Response("Please give all details")
        user = authenticate(username=username,password=password)
        if user is not None:
            payload ={
                'username':username,
                'password':password
            }
            jwt_token = jwt.encode({'payload':payload},'secret',algorithm='HS256')
            response = Response({"status":"Logged",'payload':payload,'jwt_token':jwt_token})
            return response
        else:
            return Response("Account not exist")
            
