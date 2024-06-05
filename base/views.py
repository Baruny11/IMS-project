from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from.models import Product, ProductCategory ,Department, Supplier
from.serializer import ProductSerializer,UserSerializer,  ProductCategorySerializer,DepartmentSerializer,SupplierSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view([])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email,password=password)

    if user == None:
        return Response('invalid credential')
    
    else:
        token,_=Token.objects.get_or_create(user=user)
        return Response(token.key)

@api_view(['post'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hash_password = make_password(password)
        a = serializer.save()
        a.password = hash_password
        a.save()
        return Response('User created!')
    else:
        return Response(serializer.errors)


class ProductApiView(ModelViewSet):
    queryset =Product.objects.all()
    serializer_class =ProductSerializer

class ProductCategoryApiView(GenericAPIView):
    queryset=ProductCategory.objects.all()
    serializer_class= ProductCategorySerializer

    def get(self,request):
        product_category_objs = self.get_queryset()
        serializer = self.serializer_class(product_category_objs,many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer = self .serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
        

class ProductCategoryDetailApiView(GenericAPIView):
    queryset=ProductCategory.objects.all()
    serializer_class= ProductCategorySerializer

    def get(self,request,pk):
        try:
            object = ProductCategory.objects.get(id=pk)
        except:
            return Response('Data not found')
        serializer = self.serializer_class(object)
        return Response(serializer.data)

    def put(self,request,pk):
        try:
            object = ProductCategory.objects.get(id=pk)
        except:
            return Response('Data not found')
        serializer = self.serializer_class(object,data=request.data)
        if serializer .is_valid():
              serializer.save()
              return Response('Data update!')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            object = ProductCategory.objects.get(id=pk)
        except:
            return Response('Data not found')
        object.delete()
        return Response('Data deleted!')

         





class DepartmentApiView(GenericAPIView):
    queryset=Department.objects.all()
    serializer_class= DepartmentSerializer

    def get(self,request):
        department_objs = self.get_queryset()
        serializer = self.serializer_class(department_objs,many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer = self .serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

   
        

class SupplierApiView(GenericAPIView):
    queryset=Supplier.objects.all()
    serializer_class= SupplierSerializer

    def get(self,request):
        supplier_objs = self.get_queryset()
        serializer = self.serializer_class(supplier_objs,many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer = self .serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
        
