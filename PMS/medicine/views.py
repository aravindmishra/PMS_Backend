from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedicineSerializer, MedicineListSerializer
from .models import MedicineDetails
from datetime import datetime
from .controller.common import Common
import logging

# Get an instance of a logging
log = logging.getLogger(__name__)

# Create your views here.

class AddMedicine(APIView):
    def post(self,request):
        try:
            serializer = MedicineSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(created_by = 1, created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                log.info("Data Inserted")
                return Response({"error":False,"status_code":200,"message":"Data Inserted"})
            else:
                return Response({"error":True,"status_code":400,"message":serializer.errors})
        
        except KeyError:
            log.error("Invalid Request Data")
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})


class UpdateMedicine(APIView):
    def post(self,request,id):
        try:
            response = MedicineDetails.objects.get(medicine_id = id)
            serializer = MedicineSerializer(response,data = request.data)
            if serializer.is_valid():
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


class MedicineList(APIView):
    def post(self,request):
        try:
            response = MedicineDetails.medicineList()
            serializer = MedicineListSerializer(response, many=True)
            for data in serializer.data:
                if(data["purchased_qty"] == None):
                    data["purchased_qty"] = 0
                data["avaiable_quantity"] = (int(data["quantity"]) - int(data["purchased_qty"]))
                data["available_percentage"] = Common.percentageCalculation(total = data["quantity"], detect = data["purchased_qty"])
            log.info("Data Retrived")
            return Response({"error":False,"status_code":200,"data":serializer.data})

        except Exception as e:
            log.error(e)
            return Response({"error":True,"status_code":500,"message":str(e)})