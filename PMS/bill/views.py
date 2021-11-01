from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .controller.common import Common
from .serializers import BillValidSerializer
from .models import CustomerDetails
from datetime import datetime
# Create your views here.

class BillEntry(APIView):
     def post(self,request):
        try:
            serializer = BillValidSerializer(data = request.data)
            if serializer.is_valid():
                if Common.purchaseEntry(request.data):
                    return Response({"error":False,"status_code":200,"message":"Data Inserted"})
                else:
                    return Response({"error":False,"status_code":400,"message":"Something went wrong"})
            else:
                return Response({"error":True,"status_code":400,"message":serializer.errors})
        
        except KeyError:
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            return Response({"error":True,"status_code":500,"message":str(e)})



class CheckCustomer(APIView):
    def post(self,request):
        try:
            # Check is already exist.
            if "mobile_no" in request.data:
                customerResponse = CustomerDetails.objects.values('name').filter(mobile_no = int(request.data["mobile_no"]))
                if len(customerResponse) != 0:
                    return Response({"error":False,"status_code":200,"message":"Customer Exist","data":customerResponse[0]})
                else:                  
                    return Response({"error":False,"status_code":201,"message":"Customer Not Exist"})
            else:
                return Response({"error":True,"status_code":400,"message":"Mobile No is required"})

        except KeyError:
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            return Response({"error":True,"status_code":500,"message":str(e)})
