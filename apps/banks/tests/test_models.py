# apps/banks/tests/test_models.py
from django.test import TestCase
from django.db import IntegrityError
from apps.banks.models import Bank, Branch

class BankModelTest(TestCase):
    def test_bank_creation_with_valid_data(self):
        """Test creating a bank with valid data"""
        bank = Bank.objects.create(name="State Bank of India", code="SBIN")
        self.assertEqual(bank.name, "State Bank of India")
        self.assertEqual(bank.code, "SBIN")
    
    def test_bank_name_uniqueness(self):
        """Test that bank names must be unique"""
        Bank.objects.create(name="HDFC Bank", code="HDFC")
        with self.assertRaises(IntegrityError):
            Bank.objects.create(name="HDFC Bank", code="HDFC2")
    
    def test_bank_code_uniqueness(self):
        """Test that bank codes must be unique"""
        Bank.objects.create(name="HDFC Bank", code="HDFC")
        with self.assertRaises(IntegrityError):
            Bank.objects.create(name="HDFC Bank Limited", code="HDFC")

class BranchModelTest(TestCase):
    def setUp(self):
        self.bank = Bank.objects.create(name="State Bank of India", code="SBIN")
    
    def test_branch_creation_with_valid_data(self):
        """Test creating a branch with valid data"""
        branch = Branch.objects.create(
            bank=self.bank,
            branch="Mumbai Main Branch",
            ifsc="SBIN0000001",
            address="Fort, Mumbai",
            city="Mumbai",
            district="Mumbai",
            state="Maharashtra"
        )
        self.assertEqual(branch.bank, self.bank)
        self.assertEqual(branch.ifsc, "SBIN0000001")
    
    def test_ifsc_uniqueness(self):
        """Test that IFSC codes must be unique"""
        Branch.objects.create(
            bank=self.bank,
            branch="Mumbai Branch",
            ifsc="SBIN0000001",
            address="Mumbai",
            city="Mumbai",
            district="Mumbai",
            state="Maharashtra"
        )
        with self.assertRaises(IntegrityError):
            Branch.objects.create(
                bank=self.bank,
                branch="Delhi Branch",
                ifsc="SBIN0000001",  # Same IFSC
                address="Delhi",
                city="Delhi",
                district="Delhi",
                state="Delhi"
            )
