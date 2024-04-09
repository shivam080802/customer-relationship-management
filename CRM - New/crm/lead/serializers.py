from rest_framework import serializers
from lead.models import *

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = leadModel
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = companyModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = '__all__'