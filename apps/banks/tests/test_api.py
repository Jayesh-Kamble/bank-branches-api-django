# apps/banks/tests/test_api.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.banks.models import Bank, Branch

class BankAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bank1 = Bank.objects.create(name="State Bank of India", code="SBIN")
        self.bank2 = Bank.objects.create(name="HDFC Bank", code="HDFC")
    
    def test_get_banks_list(self):
        """Test GET /api/banks/ returns list of banks"""
        url = reverse('banks:bank-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_get_specific_bank(self):
        """Test GET /api/banks/{id}/ returns specific bank"""
        url = reverse('banks:bank-detail', args=[self.bank1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "State Bank of India")
    
    def test_get_nonexistent_bank_returns_404(self):
        """Test GET /api/banks/999/ returns 404"""
        url = reverse('banks:bank-detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class BranchAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bank = Bank.objects.create(name="State Bank of India", code="SBIN")
        self.branch = Branch.objects.create(
            bank=self.bank,
            branch="Mumbai Main Branch",
            ifsc="SBIN0000001",
            address="Fort, Mumbai",
            city="Mumbai",
            district="Mumbai",
            state="Maharashtra"
        )
    
    def test_get_branches_list(self):
        """Test GET /api/branches/ returns list of branches"""
        url = reverse('banks:branch-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_search_branches_by_city(self):
        """Test filtering branches by city"""
        url = reverse('banks:branch-list')
        response = self.client.get(url, {'city': 'Mumbai'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_search_branches_by_bank_name(self):
        """Test searching branches by bank name"""
        url = reverse('banks:branch-list')
        response = self.client.get(url, {'search': 'State Bank'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
