from .models import Keyword,Category,BankStatement

# bdata=BankStatement.objects.all()

def narration23(data):
    key1=Keyword.objects.all()
    recv='other'
    for a in key1:
    	if a.category.name in data:
    		recv=a.name
    return recv







# def narration23(data):
#     key1=Keyword.objects.all()
#     for a in key1:
#     	if a.category.name in data:
# 	    	# print('data',data)
# 	    	# print(a.name)
# 	    	if a.name:
# 	    		return a.name
# 	    	else:
# 	    		return a.category.name
    	# print(type(a.name))
    	# print(a.category)
    	
    	# if a.name in data:
    		
    		

    			
	
	# Mode=['DD','CHQ','NEFT','IMPS','RTGS','TPT','DD','ATW','INSTALLMENT','CASHDEPOSIT','BANKER CHQ',
	# 'DEBITCARD','POS','MOBILE WALLETS','AEPS','USSD','PREPAID CARD','BANKCHARGES/BC',
	# 'NWD','EAW','UPI','ACH','INT','FI/INFS','SP','BIL','EBA','IB','INF','INW CLG',
	# 'ICONN','AUTOSWEEP',"REV SWEEP","SWEEP TRF","VMT","CWDR","PUR","TIP/SCG", 
	# 'RATE.DIFF',"CLG","EDC","SETU","Int. Pd. ","Int. Coll.","MMT"]
	
	# for y in Mode:			
	# 	if  y in data:
			# return y
	# narration=['POS 438624XXXXXX1138 VODAFONE ESSAR S POS DEBIT',
	# 'NEFT DR-IBKL0001024-ASVH PROJECT RECEIPT ACCOUNT-NETBANK, MUM-N296150102525926',
	# 'NWD-438624XXXXXX1138-00387029-INDORE','ATW-438624XXXXXX1138-S1AWID22-INDORE',
	# 'RTGS DR-IBKL0001024-ASVH PROJECT RECEIPT ACCOUNT-NETBANK, MUM-HDFCR52015102369499134',
	# 'CHQ PAID-MICR CTS-MU-PODAR INTERNATIONAL','IMPS-P2A-509311336761-917024578789-IB: IMPS TO  00011020001220',
	# '00011580000026  -TPT-FAMILY MAINTAINCE','AIRTEL PREPAID-HDFC118230310-BILLPAY ONLINEPAYMENT-04992990009396',
	# 'IB FUNDS TRANSFER CR-00011590000039','50400028788200- RD INSTALLMENT-MAR 2015','DD CR-00011590000039','DD ISSUE  - HDFC BANK LT - MUMBAI CLEAR - 010526 - 040413010750 - *****KOTAK  SECURITIES   LTD*******']

# print(narration)
	# narr='IB FUNDS TRANSFER CR-00011590000039'
	# for x in Mode:

	# 	if x in narr:
	# 		print(x)
	# 		break



	# for y in narration:
	# 	for x in Mode:
	# 		result=y.find(x)
	# 		if  result!= -1:
	# 			print(y)
	# 			print(x)
	# 			print()

	# 			break
			

























































































































































































































































































