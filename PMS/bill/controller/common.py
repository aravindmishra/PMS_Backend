from ..models import CustomerDetails, PurchaseDetails
from ..serializers import AddCustomerDetailsSerializer, AddPurchaseDetailsSerializer, BillValidSerializer
from datetime import datetime
import json

class Common:
    def purchaseEntry(requestData):
        try:
            customer_id = 0
            # Check is already exist.
            customerResponse = CustomerDetails.objects.values('customer_id','name').filter(mobile_no = int(requestData["mobile_no"]))
            if len(customerResponse) == 0:
                # Add New Customer.
                customerRequest = {"name":requestData["name"],"mobile_no":requestData["mobile_no"]}
                customerSerializer = AddCustomerDetailsSerializer(data = customerRequest)
                if customerSerializer.is_valid():
                    customerSerializer.save(status = 1, created_by = 1, created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    lastCustomerId = CustomerDetails.objects.latest('customer_id')[0]
                    customer_id = lastCustomerId
                    print(lastCustomerId)
                    if Common.addPurchase(medicineList = requestData["bill_medicine_list"],customer_id = customer_id):
                        return True
                    return False
                else:
                    print(customerSerializer.errors)
                    return False
            
            elif len(customerResponse) > 0:
                customer_id = int(customerResponse[0]["customer_id"])
                if(customerResponse[0]["name"] != requestData["name"]):
                    customerResponse.update(name = requestData["name"], modified_by = 1, modified_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                if Common.addPurchase(medicineList = requestData["bill_medicine_list"],customer_id = customer_id):
                    return True
                return False

        except Exception as e:
            print(str(e))
            return False


    def addPurchase(medicineList,customer_id = 0):
        try:
            if customer_id and medicineList:
                for data in json.loads(medicineList):
                    print(data)
                    request = {"customer_id": customer_id, "medicine_id": data["medicine_id"], "purchased_qty": data["purchased_qty"]}
                    serializer = AddPurchaseDetailsSerializer(data = request)
                    if serializer.is_valid():
                        serializer.save(status = 1, created_by = 1, created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))                
                return True
            return False

        except Exception as e:
            print(str(e))
            return False


