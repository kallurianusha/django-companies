from rest_framework import serializers
from .models import Companydb

class Companydbserializer(serializers.ModelSerializer):
    class Meta:
        model =Companydb
        fields =['id','name','location']