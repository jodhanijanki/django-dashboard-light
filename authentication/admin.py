# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import BankDetails,CompanyUser,IndividualUser,UserType,BankStatement,Category,Keyword
# Register your models here.
class BankDetailsAdmin(admin.ModelAdmin):
	list_display=['user','bank_name','account_number','account_type']


admin.site.register(BankDetails,BankDetailsAdmin)

admin.site.register(CompanyUser)
admin.site.register(IndividualUser)

class UserTypeAdmin(admin.ModelAdmin):
	list_display=['user','user_type']
admin.site.register(UserType,UserTypeAdmin)



class BankStatementAdmin(admin.ModelAdmin):
	list_display=['narration','category','date']
	search_fields=['narration','category','date']
	list_editable=['category']
admin.site.register(BankStatement,BankStatementAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display=['id','name']
	search_fields=['name']
	list_editable=['name']
admin.site.register(Category,CategoryAdmin)

class KeywordAdmin(admin.ModelAdmin):
	list_display=['id','name','category']
	search_fields=['name']
	list_editable=['name','category']

admin.site.register(Keyword,KeywordAdmin)


