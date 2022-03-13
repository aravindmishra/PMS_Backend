from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserDetails
from .serializers import UserSerializer, UserListSerializer, UserUpdateSerializer
from .controller.common import Common
from datetime import datetime
import logging

# Get an instance of a logging
log = logging.getLogger(__name__)

# Create your views here.
class AddUser(APIView):
    def post(self,request):
        try:
            serializer = UserSerializer(data = request.data)
            if serializer.is_valid():
                password = Common.encryptPassword(request.data["password"])
                if password:
                    serializer.save(password = password, created_by = 1, created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    log.info("Data Inserted")
                    return Response({"error":False,"status_code":200,"message":"Data Inserted"})
                log.error("Password Error")
                return Response({"error":True,"status_code":400,"message":"Password Error"})
            else:
                log.error(serializer.errors)
                return Response({"error":True,"status_code":400,"message":serializer.errors})
        
        except KeyError:
            log.error("Invalid Request Data")
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})


class UpdateUser(APIView):
    def post(self,request,id):
        try:
            response = UserDetails.objects.get(user_id = id)
            serializer = UserUpdateSerializer(response,data = request.data)
            if serializer.is_valid():
                if request.data["password"] != '':
                    password = Common.encryptPassword(request.data["password"])
                    if password:
                        serializer.save(password = password, modified_by = 1, modified_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        log.info("Data Updated")
                        return Response({"error":False,"status_code":200,"message":"Data Updated"})
                    return Response({"error":True,"status_code":400,"message":"Password Error"})
                else:
                    serializer.save(modified_by = 1, modified_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    log.info("Data Updated")
                    return Response({"error":False,"status_code":200,"message":"Data Updated"})
            else:
                log.error(serializer.errors)
                return Response({"error":True,"status_code":400,"message":serializer.errors})
        
        except KeyError:
            log.error("Invalid Request Data")
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})

class UserDetailsList(APIView):
    def post(self,request):
        try:
            response = UserDetails.objects.all()
            serializer = UserListSerializer(response,many=True)
            log.info("Data Retrived")
            return Response({"error":False,"status_code":200,"data":serializer.data})
            
        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})

class CheckUserAuth(APIView):
    def post(self,request):
        try:
            if "username" and "password" in request.data:
                password = Common.encryptPassword(request.data["password"])
                response = UserDetails.objects.filter(name = request.data["username"],password = password).count()
                print(response)
                if response:
                    log.info("Authorized User")
                    return Response({"error":False,"status_code":200,"message":"Authorized User", "data":{}})
                else:
                    log.error("Un-Authorized User")
                    return Response({"error":False,"status_code":401,"message":"Un-Authorized User"})
            else:
                log.error("Invalid Request Data")
                return Response({"error":True,"status_code":400,"message":"Invalid Input Request"})
        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})
