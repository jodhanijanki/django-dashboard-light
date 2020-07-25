# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import IndividualUser,BankDetails,CompanyUser
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))
    USER_TYPE = [
        ('Individual', 'Individual'),
        ('Company', "Company"),
        ]
    usertype = forms.ChoiceField(label='usertype', choices=USER_TYPE,
                                        widget=forms.Select(
                                            attrs={
                                                "class": "form-control form-control-lg"
                                            },
                                        ))    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','usertype')


class IndividualForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control form-control-lg"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control form-control-lg"
            }
        ))
    brand_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Brand Name",
                "class": "form-control form-control-lg"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address line one",
                "class": "form-control form-control-lg"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "City",
                "class": "form-control form-control-lg"
            }
        ))
    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "State",
                "class": "form-control form-control-lg"
            }
        ))
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Country",
                "class": "form-control form-control-lg"
            }
        ))
    pin_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Pin Code",
                "class": "form-control form-control-lg"
            }
        ))
    started_in_year = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "DD/MM/YYYY",
                "class": "form-control form-control-lg"
            }
        ))
    website_address = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder": "Website URL",
                "class": "form-control form-control-lg"
            }
        ))
    PROFESSION_TYPE = [
        ('CA', "CA"),
        ('CS', "CS"),
        ("Tax_Adviser", "Tax Adviser"),
        ("Legal_Adviser", "Legal Adviser"),
        ("Analyst", "Analyst"),
        ("Business_Adviser", "Business Adviser"),
        ("Finance_Adviser", "Finance Adviser"),
        ("Diversified", "Diversified")]
    profession_type = forms.ChoiceField(label='Profession Type', choices=PROFESSION_TYPE,
                                        widget=forms.Select(
                                            attrs={
                                                "class": "form-control form-control-lg"
                                            },
                                        ))
    SPECIALITY_TYPE = [("FMCG", "FMCG"),
        ("Manufacturer", "Manufacturer"),
        ("Trader", "Trader"),
        ("IMPEX", "IMPEX"),
        ("Retailer", "Retailer"),
        ("IT", "IT"),
        ("Diversified", "Diversified")]
    speciality_type = forms.ChoiceField(required=False,label='Speciality Type', choices=SPECIALITY_TYPE,
                                        widget=forms.Select(
                                            attrs={
                                                "class": "form-control form-control-lg"
                                            },
                                        ))
    BUSINESS_CATER = [("Startup", "Startup"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
        ("Corporate", "Corporate"),
        ("Institution", "Institution")]
    business_cater = forms.ChoiceField(required=False,label='Speciality Type', choices=BUSINESS_CATER,
                                       widget=forms.Select(
                                           attrs={
                                               "class": "form-control form-control-lg"
                                           },
                                       ))
    EXPERIENCE = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5+')]
    experience = forms.ChoiceField(required=False,label='Speciality Type', choices=EXPERIENCE,
                                   widget=forms.Select(
                                       attrs={
                                           "class": "form-control form-control-lg"
                                       },
                                   ))
    annual_business_turnover = forms.DecimalField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Anuual Business Turnover",
                "class": "form-control form-control-lg"
            }
        ))
    number_of_employees = forms.IntegerField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Number of Employees",
                "class": "form-control form-control-lg"
            }
        ))
    core_team_members = forms.IntegerField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Core Team Members",
                "class": "form-control form-control-lg"
            }
        ))
    GST_number = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "GST Number",
                "class": "form-control form-control-lg",
                
            }
        ))
    PAN_number = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "PAN Number",
                "class": "form-control form-control-lg"
            }
        ))
    description = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Description",
                "class": "form-control form-control-lg"
            }
        ))
    logo = forms.FileField(required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True
            }
        ))


    class Meta:
        model = IndividualUser
        fields = ('first_name', 'last_name', 'brand_name', 'address', 'city', 'state', 'country', 'pin_code', 'started_in_year', 'website_address', 'profession_type', 'speciality_type', 'business_cater', 'experience', 'annual_business_turnover', 'number_of_employees', 'core_team_members', 'GST_number', 'PAN_number', 'description', 'logo' )

class CompanyForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control form-control-lg"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control form-control-lg"
            }
        ))
    contact_person_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Contact Person",
                "class": "form-control form-control-lg"
            }
        ))
    contact_person_mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mobile",
                "class": "form-control form-control-lg"
            }
        ))
    brand_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Brand Name",
                "class": "form-control form-control-lg"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address line two",
                "class": "form-control form-control-lg"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "City",
                "class": "form-control form-control-lg"
            }
        ))
    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "State",
                "class": "form-control form-control-lg"
            }
        ))
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Country",
                "class": "form-control form-control-lg"
            }
        ))
    pin_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Pin Code",
                "class": "form-control form-control-lg"
            }
        ))
    started_in_year = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "DD/MM/YYYY",
                "class": "form-control form-control-lg"
            }
        ))
    website_address = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder": "Website URL",
                "class": "form-control form-control-lg"
            }
        ))
    COMPANY_TYPE = [(1, 'Partnership'), (2, 'LLP'), (3, 'Pvt Ltd'), (4, 'Ltd'), (5, 'others')]
    company_type = forms.ChoiceField(label='Company Type', choices=COMPANY_TYPE,
                                     widget=forms.Select(
                                         attrs={
                                             "class": "form-control form-control-lg"
                                         },
                                     ))
    BUSINESS_TYPE = [(1, 'FMCG'), (2, 'Manufacturer'), (3, 'Trader'), (4, 'IMPEX'), (5, 'Retailer'), (6, 'IT'),
                     (7, 'Diversified')]
    business_type = forms.ChoiceField(label='Speciality Type', choices=BUSINESS_TYPE,
                                      widget=forms.Select(
                                          attrs={
                                              "class": "form-control form-control-lg"
                                          },
                                      ))
    BUSINESS_SIZE = [(1, 'Startup'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Corporate'), (6, 'Institution')]
    business_size = forms.ChoiceField(label='Speciality Type', choices=BUSINESS_SIZE,
                                      widget=forms.Select(
                                          attrs={
                                              "class": "form-control form-control-lg"
                                          },
                                      ))
    annual_business_turnover = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Anuual Business Turnover",
                "class": "form-control form-control-lg"
            }
        ))
    number_of_employees = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Number of Employees",
                "class": "form-control form-control-lg"
            }
        ))
    core_team_members = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Core Team Members",
                "class": "form-control form-control-lg"
            }
        ))
    GST_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "GST Number",
                "class": "form-control form-control-lg"
            }
        ))
    PAN_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "PAN Number",
                "class": "form-control form-control-lg"
            }
        ))
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Description",
                "class": "form-control form-control-lg"
            }
        ))
    logo = forms.FileField(required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True
            }
        ))


    class Meta:
        model = CompanyUser
        fields = ('first_name', 'last_name', 'brand_name', 'contact_person_name', 'contact_person_mobile', 'address', 'city', 'state', 'country', 'pin_code', 'started_in_year', 'website_address', 'company_type', 'business_type', 'business_size', 'annual_business_turnover', 'number_of_employees', 'core_team_members', 'GST_number', 'PAN_number', 'description', 'logo')


class BankForm(forms.ModelForm):
    bank_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Bank Name",
                "class": "form-control form-control-lg"
            }
        ))
    branch_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Branch Name",
                "class": "form-control form-control-lg"
            }
        ))
    ifsc_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Branch Name",
                "class": "form-control form-control-lg"
            }
        ))
    account_number = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Branch Name",
                "class": "form-control form-control-lg"
            }
        ))
    ACCOUNT_TYPE = [(1, '-----'), (2, 'Saving Account'), (3, 'Current Account'), (4, 'Overdraft Account')]
    account_type = forms.ChoiceField(label='Account Type', choices=ACCOUNT_TYPE,
                                     widget=forms.Select(
                                         attrs={
                                             "class": "form-control form-control-lg"
                                         },
                                     ))
    class Meta:
        model = BankDetails
        fields = ('bank_name', 'branch_name', 'ifsc_code', 'account_number', 'account_type')


