# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

class UserType(models.Model):
    
    user_type = models.CharField(max_length=10,blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='user_type')
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_type

class BankDetails(models.Model):
    AccountType = [
        (1, '--------------'),
        (2, 'Saving Account'),
        (3, 'Current Account'),
        (4, 'Overdraft Account')
    ]
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='bank_detail')
    bank_name = models.CharField(max_length=200, null=True, blank=False)
    branch_name = models.CharField(max_length=20, null=True, blank=False)
    ifsc_code = models.CharField(max_length=20, null=True, blank=False)
    account_number = models.CharField(max_length=20,null=True, blank=False)
    account_type = models.IntegerField(choices=AccountType, blank=True,null=True)
    def __str__(self):
        return f'{self.account_number}'

class BankStatement(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='bank_data')
    bankdetails=models.ForeignKey(BankDetails,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='bank_statements')
    date = models.DateField(null=True, blank=False)
    narration = models.CharField(max_length=100, null=True, blank=False)
    ref_no = models.CharField(max_length=40, null=True, blank=False)
    value_dt = models.DateField(null=True, blank=False)
    withdrawal_amt = models.FloatField(blank=True,null=True)
    deposite_amt = models.FloatField(blank=True,null=True)
    closing_balance = models.FloatField(blank=True,null=True)
    category =models.CharField(max_length=40, null=True, blank=False)
    def __str__(self):
        return f'{self.narration}'
class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    def __str__(self):
        return f'{self.name}'
class Keyword(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='keywords')
    def __str__(self):
        return f'{self.name}'








class CompanyUser(models.Model):
    CompanyType = [
        (1, "Partnership"),
        (2, "LLP"),
        (3, "Pvt Ltd"),
        (4, "Ltd"),
        (5, "others")
        ]
    BusinessType = [
        (1, "FMCG"),
        (2, "Manufacturer"),
        (3, "Trader"),
        (4, "IMPEX"),
        (5, "Retailer"),
        (6, "IT"),
        (7, "Diversified")
        ]
    BusinessSize = [
        (1, "Startup"),
        (2, "Small"),
        (3, "Medium"),
        (4, "Large"),
        (5, "Corporate"),
        (6, "Institution"),
    ]

    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='company_profile')
    first_name = models.CharField(max_length=200, null=True, blank=False)
    last_name = models.CharField(max_length=200, null=True, blank=False)
    contact_person_name = models.CharField(max_length=200, null=True, blank=False)
    contact_person_mobile = models.CharField(max_length=200, null=True,blank=False)
    brand_name = models.CharField(max_length=200, null=True, blank=False)
    address = models.TextField(null=True, blank=False)
    city = models.CharField(max_length=200, null=True, blank=False)
    state = models.CharField(max_length=200, null=True, blank=False)
    country = models.CharField(max_length=200, null=True, blank=False)
    pin_code = models.CharField(max_length=200, null=True, blank=False)
    logo = models.ImageField(upload_to='media/', null=True, blank=True)
    started_in_year = models.DateField(auto_now=False, auto_now_add=False, blank=True,null=True)
    website_address = models.URLField(null=True, blank=True)
    company_type = models.IntegerField(choices=CompanyType, blank=True,null=True)
    business_type = models.IntegerField(choices=BusinessType, blank=True, null=True)
    business_size = models.IntegerField(choices=BusinessSize, blank=True, null=True)
    annual_business_turnover = models.DecimalField(blank=True, max_digits=20, null=True, decimal_places=2)
    number_of_employees = models.IntegerField(blank=True, null=True)
    core_team_members = models.IntegerField(blank=True, null=True)
    GST_number = models.CharField(max_length=15, blank=True, null=True)
    PAN_number = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.first_name


class IndividualUser(models.Model):
    CA='CA'
    CS='CS'
    ProfessionType = [
        (CA, "CA"),
        (CS, "CS"),
        ("Tax_Adviser", "Tax Adviser"),
        ("Legal_Adviser", "Legal Adviser"),
        ("Analyst", "Analyst"),
        ("Business_Adviser", "Business Adviser"),
        ("Finance_Adviser", "Finance Adviser"),
        ("Diversified", "Diversified")
        ]
    SpecialityType = [
        ("FMCG", "FMCG"),
        ("Manufacturer", "Manufacturer"),
        ("Trader", "Trader"),
        ("IMPEX", "IMPEX"),
        ("Retailer", "Retailer"),
        ("IT", "IT"),
        ("Diversified", "Diversified")
        ]
    BusinessCater = [
        ("Startup", "Startup"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
        ("Corporate", "Corporate"),
        ("Institution", "Institution")
    ]
    Experience = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5+")
    ]

    # user_id = models.OneToOneField(User, on_delete=models.DO_NOTHING,related_name='individual')
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,related_name='individual_profile')
    first_name = models.CharField(max_length=200, null=True, blank=False)
    last_name = models.CharField(max_length=200, null=True, blank=False)
    brand_name = models.CharField(max_length=200, null=True, blank=False)
    address = models.TextField(null=True, blank=False)
    city = models.CharField(max_length=200, null=True, blank=False)
    state = models.CharField(max_length=200, null=True, blank=False)
    country = models.CharField(max_length=200, null=True, blank=False)
    pin_code = models.CharField(max_length=200, null=True, blank=False)
    logo = models.ImageField(upload_to='media/', null=True, blank=True)
    started_in_year = models.DateField(auto_now=False, auto_now_add=False, blank=True,null=True)
    website_address = models.URLField(null=True, blank=True)
    profession_type = models.CharField(max_length=20 ,choices=ProfessionType, blank=True,null=True)
    speciality_type = models.CharField(max_length=20 ,choices=SpecialityType, blank=True, null=True)
    business_cater = models.CharField(max_length=20 ,choices=BusinessCater, blank=True, null=True)
    experience = models.IntegerField(choices=Experience, blank=True, null=True)
    annual_business_turnover = models.DecimalField(blank=True, max_digits=20, null=True, decimal_places=2)
    number_of_employees = models.IntegerField(blank=True, null=True)
    core_team_members = models.IntegerField(blank=True, null=True)
    GST_number = models.CharField(max_length=15, blank=True, null=True)
    PAN_number = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    # bank_details = models.ForeignKey(BankDetails, null=True)
    # user_type = models.ForeignKey(UserType, null=True)
    def __str__(self):
        return self.first_name