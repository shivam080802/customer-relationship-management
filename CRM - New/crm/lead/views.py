import random
from django.shortcuts import render
from lead.models import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from lead.serializers import *
# Create your views here.

class CreateLead(APIView):
    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response("data aa gya bhai")
        print(serializer.errors)
        return Response("Sahi data de bhai")
    
    def get(self, request):
        lead = leadModel.objects.all()
        serializer = LeadSerializer(lead, many=True)
        # print(serializer.data)
        return Response(serializer.data)
    
    # def delete(self,request,pk):
    #     lead = leadModel.objects.get(pk=pk)
    #     serializer = LeadSerializer(lead)
    #     lead.delete()
    #     return Response("Data delete kar diya bhai")

    
class LeadRetrieve(generics.RetrieveAPIView):
    def get(self, request, pk):
         lead = leadModel.objects.get(pk=pk)
         serializer = LeadSerializer(lead)
        #  print(serializer.data)
         return Response(serializer.data)

class DeleteLead(APIView):
    def delete(self,request,pk):
        lead = leadModel.objects.get(pk=pk)
        if lead.status=='closed'or lead.status=='Closed':
            return Response("Record is Closed. Can't deletes")
        lead.delete()
        return Response("Data delete kar diya bhai")
    
class UpdateLead(APIView):
    def put(self,request,pk):
        lead = leadModel.objects.get(pk=pk)
        serializer = LeadSerializer(lead, data=request.data, partial=True)
        # print(serializer.data)
        if serializer.is_valid():
            if lead.status=='closed'or lead.status=='Closed':
                return Response("Record is Closed. Can't change details")
            serializer.save()
            print(serializer.data)
            return Response("Updated Successfully")
        return Response("Update nahi hua bhai wapas se try kar")

# class PatchLead(APIView):
#     def put(self,request,pk):
#         lead = leadModel.objects.get(pk=pk)
#         serializer = LeadSerializer(lead, data=request.data, partial=True)
#         # print(serializer.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response("Update kar diya bhai")
#         print(serializer.error)
#         return Response("Update nahi hua bhai wapas se try kar")

class GetCompany(APIView):
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response("data aa gya bhai")
        print(serializer.errors)
        return Response("Sahi data de bhai")
    
    def get(self, request):
        lead = companyModel.objects.all()
        
        serializer = CompanySerializer(lead, many=True)
        # print(serializer.data)
        return Response(serializer.data)
    
class CompanyRetrieve(generics.RetrieveAPIView):
    def get(self, request, pk):
         lead = companyModel.objects.get(pk=pk)
        #  print(type(lead.companyName))
         serializer = CompanySerializer(lead)
        #  print(type(serializer.data))
         return Response(serializer.data)


class UserRetrieve(generics.RetrieveAPIView):
    def get(self, request, pk):
         user = userModel.objects.get(pk=pk)
        #  print(type(lead.companyName))
         serializer = UserSerializer(user)
        #  print(type(serializer.data))
         return Response(serializer.data)


class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            if userModel.objects.filter(username=username).exists() and userModel.objects.filter(password=password).exists():
                return Response("Login")
            else:
                return Response("Not Login")
                
        


class GetUser(APIView):
    def get(self, request):
        user = userModel.objects.all()   
        serializer = UserSerializer(user, many=True)
        # print(serializer.data)
        return Response(serializer.data)

class Count(APIView):
    def get(self, request):
        count = {
            "yarn" : 10000,
            "fabric": 5000,
            "greige": 10000
        }

        return Response(count)