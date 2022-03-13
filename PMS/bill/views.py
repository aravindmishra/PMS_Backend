from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .controller.common import Common
from .serializers import BillValidSerializer, PurchaseDetailsListSerializer, BillDetailsListSerializer
from .models import CustomerDetails, PurchaseDetails, BillDetails
from datetime import datetime
import json
import logging

# Get an instance of a logging
log = logging.getLogger(__name__)

# Create your views here.
class BillEntry(APIView):
     def post(self,request):
        try:
            serializer = BillValidSerializer(data = request.data)
            if serializer.is_valid():
                if Common.purchaseEntry(request.data):
                    log.info("Data Inserted")
                    return Response({"error":False,"status_code":200,"message":"Data Inserted"})
                else:
                    log.error("Somthing Went Wrong")
                    return Response({"error":False,"status_code":400,"message":"Somthing Went Wrong"})
            else:
                log.error(serializer.errors)
                return Response({"error":True,"status_code":400,"message":serializer.errors})
        
        except KeyError:
            log.error("Invalid Request Data")
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})



class CheckCustomer(APIView):
    def post(self,request):
        try:
            # Check is already exist.
            if "mobile_no" in request.data:
                customerResponse = CustomerDetails.objects.values('name').filter(mobile_no = int(request.data["mobile_no"]))
                if len(customerResponse) != 0:
                    log.info("Customer Exist")
                    return Response({"error":False,"status_code":200,"message":"Customer Exist","data":customerResponse[0]})
                else:
                    log.error("Customer Not Exist")                  
                    return Response({"error":False,"status_code":201,"message":"Customer Not Exist"})
            else:
                log.error("Mobile No is required")
                return Response({"error":True,"status_code":400,"message":"Mobile No is required"})

        except KeyError:
            log.error("Invalid Request Data")
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})


class PurchaseDetailsList(APIView):
    def post(self,request):
        try:
            response = PurchaseDetails.purchase_list()
            serializer = PurchaseDetailsListSerializer(response,many=True)
            log.info("Data Retrived")
            return Response({"error":False,"status_code":200,"data":serializer.data})
            
        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})

class BillDetailsList(APIView):
    def post(self,request):
        try:
            response = BillDetails.bill_list()
            serializer = BillDetailsListSerializer(response,many=True)
            log.info("Data Retrived")
            return Response({"error":False,"status_code":200,"data":serializer.data})
            
        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})


class FilterPurchaseDetails(APIView):
    def post(self,request):
        try:
            if "filter" in request.data:
                response = PurchaseDetails.purchase_list(filter = json.loads(request.data["filter"]))
                serializer = PurchaseDetailsListSerializer(response,many=True)
                log.info("Data Retrived")
                return Response({"error":False,"status_code":200,"data":serializer.data})
            log.error("Invalid Request Data")
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})
