from django.shortcuts import render
from rest_framework.response import Response
from . models import Products,Category,Customer
from rest_framework.decorators import api_view
from . serializers import CustomerSerializer,ProductsSerializer,CategorySerializer
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def index(request):
    products={
        'pid':2,
        'category':'grocery',
        'pname':'sunflower oil',
        'price':3400
    }
    return Response(products)

@api_view(['GET','POST','PUT','PATCH'])
def customer(request):
    if request.method=='GET':
        customer_obj=Customer.objects.all()
        serialize=CustomerSerializer(customer_obj,many=True)
        return Response(serialize.data)
    
    elif request.method=='POST':
        serialize=CustomerSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
    elif request.method=='PUT':
        serialize=CustomerSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
    elif request.method=='PATCH':
        obj=Customer.objects.get(id=request.data['id'])
        serialize=CustomerSerializer(obj,data=request.data,partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
    elif request.method=='DELETE':
        obj=Customer.objects.get(id=request.data['id'])
        serialize=CustomerSerializer(obj,data=request.data,partial=True) 
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)    
        

class productscreate(APIView):
    def get(self,request):
        obj=Products.objects.all()
        serialize=ProductsSerializer(obj,many=True)
        return Response(serialize.data)

    def post(self,request):
        serialize = ProductsSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
        
class categorycreate(APIView):
    def get(self,request):
        obj=Category.objects.all()
        serialize=CategorySerializer(obj,many=True)
        return Response(serialize.data) 

    def post(self,request):
        serialize = CategorySerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)        



