from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer, BranchListSerializer
from django.shortcuts import render


class BankListView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code']
    ordering_fields = ['name', 'created_at']

class BankDetailView(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchListView(generics.ListAPIView):
    queryset = Branch.objects.select_related('bank').all()
    serializer_class = BranchListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['bank', 'city', 'state']
    search_fields = ['branch', 'ifsc', 'city', 'bank__name']
    ordering_fields = ['branch', 'created_at']

class BranchDetailView(generics.RetrieveAPIView):
    queryset = Branch.objects.select_related('bank').all()
    serializer_class = BranchSerializer

@api_view(['GET'])
def bank_branches(request, bank_id):
    try:
        bank = Bank.objects.get(id=bank_id)
        branches = Branch.objects.filter(bank=bank).select_related('bank')
        serializer = BranchSerializer(branches, many=True)
        return Response({
            'bank': BankSerializer(bank).data,
            'branches': serializer.data
        })
    except Bank.DoesNotExist:
        return Response({'error': 'Bank not found'}, status=404)

def landing_page(request):
    """
    Landing page view that displays project overview and capabilities
    """
    context = {
        'project_name': 'Bank Branches REST API',
        'description': 'Comprehensive Django REST API for managing bank and branch information',
        'total_banks': 8,
        'total_branches': 12,
        'api_endpoints': 5,
        'test_cases': 17
    }
    return render(request, 'landing.html', context)
