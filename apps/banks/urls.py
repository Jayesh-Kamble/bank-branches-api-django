from django.urls import path
from . import views

app_name = 'banks'

urlpatterns = [
    path('banks/', views.BankListView.as_view(), name='bank-list'),
    path('banks/<int:pk>/', views.BankDetailView.as_view(), name='bank-detail'),
    path('branches/', views.BranchListView.as_view(), name='branch-list'),
    path('branches/<int:pk>/', views.BranchDetailView.as_view(), name='branch-detail'),
    path('banks/<int:bank_id>/branches/', views.bank_branches, name='bank-branches'),
]
