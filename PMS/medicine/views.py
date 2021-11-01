from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedicineSerializer, MedicineListSerializer
from .models import MedicineDetails
from datetime import datetime
from .controller.common import Common

# Create your views here.

class AddMedicine(APIView):
    def post(self,request):
        try:
            serializer = MedicineSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(status = 1, created_by = 1, created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                return Response({"error":False,"status_code":200,"message":"Data Inserted"})
            else:
                return Response({"error":True,"status_code":400,"message":serializer.errors})
        
        except KeyError:
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            return Response({"error":True,"status_code":500,"message":str(e)})


class UpdateMedicine(APIView):
    def post(self,request,id):
        try:
            response = MedicineDetails.objects.get(medicine_id = id)
            serializer = MedicineSerializer(response,data = request.data)
            if serializer.is_valid():
                serializer.save(status = 1, modified_by = 1, modified_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                return Response({"error":False,"status_code":200,"message":"Data Updated"})
            else:
                return Response({"error":True,"status_code":400,"message":serializer.errors})
        
        except KeyError:
            return Response({"error":True,"status_code":400,"message":"Invalid Request Data"})

        except Exception as e:
            return Response({"error":True,"status_code":500,"message":str(e)})


class MedicineList(APIView):
    def post(self,request):
        try:
            response = MedicineDetails.medicineList()
            serializer = MedicineListSerializer(response, many=True)
            for data in serializer.data:
                data["available_percentage"] = Common.percentageCalculation(total = data["quantity"], detect = data["purchased_qty"])
            return Response({"error":False,"status_code":200,"data":serializer.data})

        except Exception as e:
            print(str(e))
            return Response({"error":True,"status_code":500,"message":str(e)})