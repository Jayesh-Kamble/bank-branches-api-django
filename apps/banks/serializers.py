from rest_framework import serializers
from .models import Bank, Branch

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'code', 'created_at', 'updated_at']

class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)
    
    class Meta:
        model = Branch
        fields = [
            'id', 'branch', 'ifsc', 'address', 
            'city', 'district', 'state', 'bank',
            'created_at', 'updated_at'
        ]

class BranchListSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source='bank.name', read_only=True)
    
    class Meta:
        model = Branch
        fields = [
            'id', 'branch', 'ifsc', 'city', 
            'district', 'state', 'bank_name'
        ]
