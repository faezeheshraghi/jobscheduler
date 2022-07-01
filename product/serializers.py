from rest_framework import serializers
from .models import basket

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = basket
        fields = ['email','subject', 'date_add', 'count','basket_id']
