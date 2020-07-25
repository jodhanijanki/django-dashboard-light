# -*- encoding: utf-8 -*-
import openpyxl
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, IndividualForm, CompanyForm, BankForm
from django.views.generic import TemplateView
from .models import IndividualUser, CompanyUser, BankDetails, UserType,BankStatement
from django.core.files.storage import FileSystemStorage
import pandas as pd
import datetime
from xlrd import open_workbook
from .utils import narration23

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    
    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):
    msg     = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)      
        if form.is_valid():
            print(1)
            form.save()
            data = request.POST.copy()
            usertype=data.get('usertype')
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            print(usertype)
            if user is not None:
                print(usertype)
                login(request, user)
                if usertype =='Individual':
                    UserType.objects.create(user_type='Individual',user=request.user)
                    return redirect('/indivisualuser')
                elif usertype =='Company':
                    UserType.objects.create(user_type='Company',user=request.user)
                    return redirect('/companyuser')    
        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()
    print( {"form": form, "msg" : msg, "success" : success })



    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })


def indivisualuser(request):
    print(request.user)
    userform = IndividualForm(request.POST)
    if request.method == "POST":
        print('yes1')
        if IndividualUser.objects.filter(user=request.user).exists():
            indiuser = IndividualUser.objects.filter(user=request.user).first()
            userform = IndividualForm(request.POST, instance=indiuser )
            print(userform.errors.as_json())
            print('yes2')
            if userform.is_valid():
                userdata=userform.save(commit=False)
                userdata.user=request.user
                userdata.save()
                return redirect('/')
            else:
                return redirect('indivisualuser')
        else:
            userform = IndividualForm(request.POST)
            if userform.is_valid(): 
                userdata=userform.save(commit=False)
                userdata.user=request.user
                userdata.save()
                return redirect('/')
    context={}
    user=request.user
    context['form']=IndividualForm()
    individual_users = IndividualUser.objects.filter(user=user)
    print('ind',individual_users)
    if individual_users.exists():
          context['individual_user'] = individual_users.first()
    return render(request, "user.html",context)         
def companyuser(request):
        print(request.user)

        if request.method == "POST":
            companyuser= CompanyForm(request.POST)

            if CompanyUser.objects.filter(user=request.user).exists():
                compuser = CompanyUser.objects.filter(user=request.user).first()
                userform = CompanyForm(request.POST, instance=compuser )
                print(userform.errors.as_json())
                print('yes2')
                if userform.is_valid():
                        userdata=userform.save(commit=False)
                        userdata.user=request.user
                        userdata.save()
                        return redirect('/')
                else:
                    return redirect('companyuser')
            else:
                userform = CompanyForm(request.POST)
                if userform.is_valid(): 
                    userdata=userform.save(commit=False)
                    userdata.user=request.user
                    userdata.save()
                    return redirect('/')
        context={}
        user=request.user
        context['form']=CompanyForm()
        company_users = CompanyUser.objects.filter(user=user)
        print('ind',company_users)
        if company_users.exists():
              context['company_user'] = company_users.first()
        return render(request, "company.html",context) 

def bankdetails(request):
            if request.method == "POST":
                bankform= BankForm(request.POST)
                print(bankform)
                if BankDetails.objects.filter(user=request.user).exists():
                    bankdata = BankDetails.objects.filter(user=request.user).first()
                    bankform = BankForm(request.POST, instance=bankdata )
                    print(bankform.errors.as_json())
                    print('yes2')
                    if bankform.is_valid():
                            userdata=bankform.save(commit=False)
                            userdata.user=request.user
                            userdata.save()
                            return redirect('/')
                    else:
                        return redirect('bankdetails')
                else:
                    userform = BankForm(request.POST)
                    if userform.is_valid(): 
                        userdata=userform.save(commit=False)
                        userdata.user=request.user
                        userdata.save()
                        return redirect('/')
            context={}
            user=request.user
            context['form']=BankForm()
            bankdata = BankDetails.objects.filter(user=user)
            print('ind',bankdata)
            if bankdata.exists():
                  context['bankdata'] = bankdata.first()
            return render(request, "bankdetail.html",context) 

def productview(request):
    user=request.user
    data= UserType.objects.filter(user=request.user)
    check=data.first()
    print(check.user_type)
    if check.user_type =='Individual':
        return redirect('/indivisualuser')
    elif check.user_type =='Company':
        return redirect('/companyuser') 
    return HttpResponse('/')

def statement(request):
    context={}
    if request.method == 'POST' and request.FILES['excel_file']:
        data= BankDetails.objects.filter(user=request.user)
        check=data.first()
        check1=check.account_number
        # print(type(check1))
        excelfile = request.FILES['excel_file']
        fs = FileSystemStorage()
        filename = fs.save(excelfile.name, excelfile)
        uploaded_file_url = fs.url(filename)
        # print(uploaded_file_url)
        workbookaddress='core'+uploaded_file_url
        # print(workbookaddress)
        test=''
        book = open_workbook(workbookaddress)
        count=0
        for sheet in book.sheets():
            # print(sheet)
            for rowidx in range(sheet.nrows):
                row = sheet.row(rowidx)
                if row:
                    for colidx, cell in enumerate(row):
                        if str(cell.value).find(check1)!= -1:
                            test=True
                            # print(test)
                            break

            if test:
                for rowidx in range(sheet.nrows):
                    row = sheet.row(rowidx)
                    if row :
                        # print(row[count])
                        for colidx, cell in enumerate(row):
                            if str(cell.value).find('Narration')!= -1:                  
                                count=rowidx+2
                                # print(cell.value,count)
                                break
                # print('count',count)

                for rowidx in range(sheet.nrows):  
                    if rowidx>count:

                        row = sheet.row(rowidx)
                        # print(row[0],row[1])
                        if str(row[0]) and str(row[1])=="empty:''":
                            print('success')
                            context['success']='Added sucessfully'

                            break
                        if row :
                        # print(row[count])
                            for colidx, cell in enumerate(row):
                                # print(colidx,cell.value)
                                if cell.value=='':
                                    cell.value=0
                                if colidx==0:
                                    day=int(cell.value[0:2])
                                    month=int(cell.value[3:5])
                                    year=int(cell.value[6:10])                                   
                                    # print(day,month,year)
                                    now=datetime.date(year,month,day)
                                    # print(now)
                                    date=now
                                elif colidx==1:
                                    narration=cell.value
                                    category=narration23(cell.value)
                                    # print(category)
                                    # print()
                                elif colidx==2:
                                    ref_no=cell.value
                                elif colidx==3:
                                    day=int(cell.value[0:2])
                                    month=int(cell.value[3:5])
                                    year=int(cell.value[6:10])                                 
                                    # print(day,month,year)
                                    now=datetime.date(year,month,day)
                                    value_dt=now
                                elif colidx==4:
                                    withdrawal_amt=cell.value
                                elif colidx==5:
                                    deposite_amt=cell.value
                                elif colidx==6:
                                    closing_balance=cell.value
                            
                            Bd=BankDetails.objects.filter(account_number=check1).first()
                            available=BankStatement.objects.filter(user=request.user,bankdetails=Bd,date=date,narration=narration,ref_no=ref_no,closing_balance=closing_balance,category=category)
                            if available:
                                context['success']='Already added'
                                print('Already added')
                                break
                            else:
                                bankext=BankStatement.objects.filter(ref_no=ref_no)

                                if bankext.filter().count () !=0: 
                                    for bankext1 in bankext:
                                        if bankext1.closing_balance==closing_balance and bankext1.ref_no==ref_no and bankext1.narration==narration:
                                            print('Entry exists')
                                            break
                                    else:
                                        BankStatement.objects.create(user=request.user,bankdetails=Bd,date=date,narration=narration,ref_no=ref_no,value_dt=value_dt,withdrawal_amt=withdrawal_amt,deposite_amt=deposite_amt,closing_balance=closing_balance,category=category)
                                        print('Ref')
                                        # print(bankext.ref_no,bankext.narration)
                                else:

                                    print('Added sucessfully')
                                    BankStatement.objects.create(user=request.user,bankdetails=Bd,date=date,narration=narration,ref_no=ref_no,value_dt=value_dt,withdrawal_amt=withdrawal_amt,deposite_amt=deposite_amt,closing_balance=closing_balance,category=category)
                        if row==[]:
                            print('Added sucessfully')

                            break
            else:
                context['success']='Account number didnt match,Upload valid file'
                print("AccountNumber didn't match")
    queryset = BankStatement.objects.order_by('-date')[:5]
    context['queryset']=queryset
    # print(context['queryset'])
    return render(request,'table.html',context)

def analyse(request):
    labels = []
    data = []
    queryset = BankStatement.objects.order_by('-withdrawal_amt')[:5]
    for withdr in queryset:
        labels.append(withdr.narration)
        data.append(withdr.withdrawal_amt)
    return render(request, 'piechart.html', {
        # 'labels': labels,
        'data': data,
            })






   








































            # if request.method == 'POST':
    #     excel_file = request.FILES['excel_file']
    #     with os.open(fd, 'wb') as out: # create new file objects
    #         out.write(excel_file.read())
    #             book = xlrd.open_workbook(fd)
    #             sheet = book.sheet_by_index(0)
    #             obj=Project(
    #                 project_title = sheet.cell_value(rowx=1, colx=1),
    #                 project_sector = sheet.cell_value(rowx=2, colx=1),
    #                 project_location = sheet.cell_value(rowx=3, colx=1),
    #                 project_tot_cost = sheet.cell_value(rowx=4, colx=1),
    #                 project_descr = sheet.cell_value(rowx=5, colx=1),
    #                 project_fund = sheet.cell_value(rowx=6, colx=1),
    #                 project_cofin = sheet.cell_value(rowx=7, colx=1),
    #                 project_applicant = sheet.cell_value(rowx=8, colx=1)
    #             )
    #             obj.save()
    # return render(request,'table.html')
