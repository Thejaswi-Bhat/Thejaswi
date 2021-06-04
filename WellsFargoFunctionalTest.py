import json
import requests
# import sys

# sys.stdout = open('D:\Project\kote.txt', 'w')

from Generic import *

# Populate Access Token
data = {'grant_type': grant_type, 'username': Username, 'password': Password, 'scope': Scope,
        'acr_values': ACR_VALUES}
data1 = {'grant_type': grant_type, 'username': Np_Username, 'password': Np_Password, 'scope': No_Scope,
         'acr_values': ACR_VALUES}

# Get access token
access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=True,
                                      auth=(client_id, client_secret))
NoPermission_token_response = requests.post(token_url, data=data1, verify=True, allow_redirects=True,
                                    auth=(client_id, client_secret))

# Print access token
print(access_token_response.text)
print(NoPermission_token_response.text)
tokens = json.loads(access_token_response.text)
tokens_np = json.loads(NoPermission_token_response.text)

headers = {'Authorization': 'Bearer ' + tokens['access_token'], 'Content-Type': 'application/json',
           'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

expired_header = {'Authorization': 'Bearer ' + ExpiredToken, 'Content-Type': 'application/json',
                  'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

NoPermission_header = {'Authorization': 'Bearer ' + tokens_np['access_token'], 'Content-Type': 'application/json',
                       'DataEncoding': 'UTF-8', 'Accept': 'application/json'}


# POST ADD GENERAL SETUP
print("POST Add General Setup")
parameters = {
    "companyId": "WellsFargoID" + str(random_value),
    "buyerId": str(random_value),
}
response = requests.post(url + generalSetup, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result1 = 'PASS'
else:
    result1 = 'FAIL'


print("Verify User NOT able to Post Add General Setup without permission")
parameters = {
    "companyId": "WellsFargoID" + str(random_value),
    "buyerId":  str(random_value),
}
response = requests.post(url + generalSetup, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result2 = 'PASS'
else:
    result2 = 'FAIL'



print("Verify User NOT able to Post Add General Setup with expired token")
parameters = {
    "companyId": "WellsFargoID" + str(random_value),
    "buyerId":  str(random_value),
}
response = requests.post(url + generalSetup, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result3 = 'PASS'
else:
    result3 = 'FAIL'


print("Verify User NOT able to Post Add General Setup without mandatory fields")
parameters = {
    "companyId": "",
    "buyerId": ""
}
response = requests.post(url + generalSetup, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result4 = 'PASS'
else:
    result4 = 'FAIL'


# GET GENERAL SETUP
print("GET General setup details")
response = requests.get(url + generalSetup, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result5 = 'PASS'
else:
    result5 = 'FAIL'


print("Verify User NOT able to GET General Setup with expired token")
response = requests.get(url + generalSetup, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result6 = 'PASS'
else:
    result6 = 'FAIL'


print("Verify User NOT able to GET General Setup without permission")
response = requests.get(url + generalSetup, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result7 = 'PASS'
else:
    result7 = 'FAIL'


# Bank Account

# POST ADD BANK ACCOUNT
print("POST Add Bank Account")
parameters = {
    "accountCode": "WellsFargoAcc12" + str(random_value),
    "accountNumber": AccountNumber,
    "routingCode": RoutingCode,
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": PPD_formatCode,
    "isActive": true
}
response = requests.post(url + bank_accounts, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
accountID = data['result']
print(accountID)
if response.status_code == ExpectedCode201:
    result8 = 'PASS'
else:
    result8 = 'FAIL'


print("Verify User is NOT able to Post Add Bank Account without permission")
parameters = {
    "accountCode": "WFAcc12" + str(random_value),
    "accountNumber": AccountNumber,
    "routingCode": RoutingCode,
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": PPD_formatCode,
    "isActive": true
}
response = requests.post(url + bank_accounts, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result9 = 'PASS'
else:
    result9 = 'FAIL'


print("Verify User is NOT able to Post Add Bank Account with expired token")
parameters = {
    "accountCode": "WFAcc12" + str(random_value),
    "accountNumber": AccountNumber,
    "routingCode": RoutingCode,
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": PPD_formatCode,
    "isActive": true
}
response = requests.post(url + bank_accounts, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result10 = 'PASS'
else:
    result10 = 'FAIL'


print("Verify User is NOT able to Post Add Bank Account without mandatory fields")
parameters = {
    "accountCode": "",
    "accountNumber": "",
    "routingCode": "",
    "companyId": "",
    "defaultFormatCode": "",
    "isActive": true
}
response = requests.post(url + bank_accounts, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result11 = 'PASS'
else:
    result11 = 'FAIL'


print("Verify User is NOT able to Post Add Bank Account with Invalid Routing code field")
parameters = {
    "accountCode": "WFAcc12" + str(random_value),
    "accountNumber": AccountNumber,
    "routingCode": "abc12345789654",
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": PPD_formatCode,
    "isActive": true
}
response = requests.post(url + bank_accounts, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result12 = 'PASS'
else:
    result12 = 'FAIL'


print("Verify User is NOT able to Post Add Bank Account with Invalid Default Format code field")
parameters = {
    "accountCode": "WFAcc12" + str(random_value),
    "accountNumber": AccountNumber,
    "routingCode": "abc12345789654",
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": "IOT",
    "isActive": true
}
response = requests.post(url + bank_accounts, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result13 = 'PASS'
else:
    result13 = 'FAIL'



# GET ADD BANK ACCOUNT
print("Get Bank Account")
response = requests.get(url + bank_accounts, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result14 = 'PASS'
else:
    result14 = 'FAIL'


print("Verify User is NOT able to Get Bank Account without permission")
response = requests.get(url + bank_accounts, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result15 = 'PASS'
else:
    result15 = 'FAIL'


print("Verify User is NOT able to Get Bank Account with expired token")
response = requests.get(url + bank_accounts, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result16 = 'PASS'
else:
    result16 = 'FAIL'



# UPDATE BANK ACCOUNT ID
print("Put Update Bank Account")
parameters = {
    "accountCode": "acc12345",
    "accountNumber": AccountNumber,
    "routingCode": RoutingCode,
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": CTX_formatCode,
    "isActive": false
}
response = requests.put(url + bank_accounts + '/' + str(accountID), data=json.dumps(parameters), headers=headers,
                        verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result17 = 'PASS'
else:
    result17 = 'FAIL'



print("Verify User is NOT able to Put Update Bank Account without permission")
parameters = {
    "accountCode": "acc12345",
    "accountNumber": AccountNumber,
    "routingCode": RoutingCode,
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": CTX_formatCode,
    "isActive": false
}
response = requests.put(url + bank_accounts + '/' + str(accountID), data=json.dumps(parameters), headers=NoPermission_header,
                        verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result18 = 'PASS'
else:
    result18 = 'FAIL'


print("Verify User is NOT able to Put Update Bank Account with expired token")
parameters = {
    "accountCode": "acc12345",
    "accountNumber": str(random_value),
    "routingCode": RoutingCode,
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": PPD_formatCode,
    "isActive": false
}
response = requests.put(url + bank_accounts + '/' + str(accountID), data=json.dumps(parameters), headers=expired_header,
                        verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result19 = 'PASS'
else:
    result19 = 'FAIL'


print("Verify User is NOT able to Put Update Bank Account without mandatory fields")
parameters = {
    "accountCode": "",
    "accountNumber": "",
    "routingCode": "",
    "companyId": "",
    "defaultFormatCode": "",
    "isActive": true
}
response = requests.put(url + bank_accounts + '/' + str(accountID), data=json.dumps(parameters), headers=headers,
                        verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result20 = 'PASS'
else:
    result20 = 'FAIL'


print("Verify User is NOT able to Put Update Bank Account with Invalid account ID")
parameters = {
    "accountCode": "acc12345",
    "accountNumber": str(random_value),
    "routingCode": RoutingCode,
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": CTX_formatCode,
    "isActive": false
}
response = requests.put(url + bank_accounts + '/' + str(Invalid), data=json.dumps(parameters), headers=headers,
                        verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result21 = 'PASS'
else:
    result21 = 'FAIL'


print("Verify User is NOT able to Put Update Bank Account with Invalid default format code")
parameters = {
    "accountCode": "acc1234569",
    "accountNumber": str(random_value),
    "routingCode": RoutingCode,
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": "BBQ",
    "isActive": false
}
response = requests.put(url + bank_accounts + '/' + str(accountID), data=json.dumps(parameters), headers=headers,
                        verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result22 = 'PASS'
else:
    result22 = 'FAIL'


print("Verify User is NOT able to Put Update Bank Account with Invalid Routing code field")
parameters = {
    "accountCode": "WFAcc12" + str(random_value),
    "accountNumber": AccountNumber,
    "routingCode": "abc12345789654",
    "companyId": "WFID12" + str(random_value),
    "defaultFormatCode": PPD_formatCode,
    "isActive": true
}
response = requests.put(url + bank_accounts + '/' + str(accountID), data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result23 = 'PASS'
else:
    result23 = 'FAIL'


# DELETE BANK ACCOUNT ID
print("Delete Bank Account")
response = requests.delete(url + bank_accounts + '/' + str(accountID), headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result24 = 'PASS'
else:
    result24 = 'FAIL'


print("Verify User is NOT able to Delete Bank Account without permission")
response = requests.delete(url + bank_accounts + '/' + str(accountID), headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result25 = 'PASS'
else:
    result25 = 'FAIL'


print("Verify User is NOT able to Delete Bank Account with expired token")
response = requests.delete(url + bank_accounts + '/' + str(accountID), headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result26 = 'PASS'
else:
    result26 = 'FAIL'


print("Verify User is NOT able to Delete Bank Account with Invalid accountID")
response = requests.delete(url + bank_accounts + '/' + str(Invalid), headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result27 = 'PASS'
else:
    result27 = 'FAIL'


# POST ADD CARD ACCOUNT

print("Post Add Card Account")
parameters = {
    "accountCode": "WFCard12" + str(random_value),
    "accountNumber":  str(random_value),
    "days": 10,
    "enabled": true
}
response = requests.post(url + card_accounts, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
cardID = data['result']
print(cardID)
if response.status_code == ExpectedCode201:
    result28 = 'PASS'
else:
    result28 = 'FAIL'


print("Verify User NOT able to Post Add Card Account without permission")
parameters = {
    "accountCode": "WFCard12" + str(random_value),
    "accountNumber":  str(random_value),
    "days": 10,
    "enabled": true
}
response = requests.post(url + card_accounts, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result29 = 'PASS'
else:
    result29 = 'FAIL'


print("Verify User NOT able to Post Add Card Account with expired token")
parameters = {
    "accountCode": "WFCard12" + str(random_value),
    "accountNumber": str(random_value),
    "days": 10,
    "enabled": true
}
response = requests.post(url + card_accounts, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result30 = 'PASS'
else:
    result30 = 'FAIL'


print("Verify user NOT able to Post Add Card Account with negative validity of days")
parameters = {
    "accountCode": "WFCard12345" + str(random_value),
    "accountNumber": str(random_value),
    "days": -10,
    "enabled": true
}
response = requests.post(url + card_accounts, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result31 = 'PASS'
else:
    result31 = 'FAIL'


print("Verify user NOT able to Post Add Card Account without mandatory fields")
parameters = {
    "accountCode": "",
    "accountNumber": "",
    "days": 0,
    "enabled": true
}
response = requests.post(url + card_accounts, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result32 = 'PASS'
else:
    result32 = 'FAIL'


# GET CARD ACCOUNT
print("Get Card Account")
response = requests.get(url + card_accounts, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result33 = 'PASS'
else:
    result33 = 'FAIL'


print("Verify User is NOT able to Get Card Account without permission")
response = requests.get(url + card_accounts, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result34 = 'PASS'
else:
    result34 = 'FAIL'


print("Verify User is NOT able to Get Card Account with expired token")
response = requests.get(url + card_accounts, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result35 = 'PASS'
else:
    result35 = 'FAIL'




# UPDATE CARD ACCOUNTS
print("PUT Update Card Account")
parameters = {
    "accountCode": "Acc25698",
    "accountNumber": "326547891",
    "days": 10,
    "enabled": true
}
response = requests.put(url + card_accounts + '/' + str(cardID), data=json.dumps(parameters), headers=headers,
                         verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result36 = 'PASS'
else:
    result36 = 'FAIL'


print("Verify User is NOT able to PUT Update Card Account without permission")
parameters = {
    "accountCode": "Acc256",
    "accountNumber": "326547891",
    "days": 10,
    "enabled": true
}
response = requests.put(url + card_accounts + '/' + str(cardID), data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result37 = 'PASS'
else:
    result37 = 'FAIL'


print("Verify User is NOT able to PUT Update Card Account with expired token")
parameters = {
    "accountCode": "Acc256",
    "accountNumber": "326547891",
    "days": 10,
    "enabled": true
}
response = requests.put(url + card_accounts + '/' + str(cardID), data=json.dumps(parameters), headers=expired_header,
                         verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result38 = 'PASS'
else:
    result38 = 'FAIL'



print("Verify User is NOT able to PUT Update Card Account without mandatory fields")
parameters = {
    "accountCode": "",
    "accountNumber": "",
    "days": 0,
    "enabled": true
}
response = requests.put(url + card_accounts + '/' + str(cardID), data=json.dumps(parameters), headers=headers,
                         verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result39 = 'PASS'
else:
    result39 = 'FAIL'


print("Verify User is NOT able to PUT Update Card Account with negative validity of days")
parameters = {
    "accountCode": "Acc256999",
    "accountNumber": "326547891",
    "days": -10,
    "enabled": true
}
response = requests.put(url + card_accounts + '/' + str(cardID), data=json.dumps(parameters), headers=headers,
                         verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result40 = 'PASS'
else:
    result40 = 'FAIL'



# DELETE CARD ACCOUNT ID
print("Delete Card Account")
response = requests.delete(url + card_accounts + '/' + str(cardID), headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result41 = 'PASS'
else:
    result41 = 'FAIL'


print("Verify User is NOT able to Delete Card Account without permission")
response = requests.delete(url + card_accounts + '/' + str(cardID), headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result42 = 'PASS'
else:
    result42 = 'FAIL'


print("Verify User is NOT able to Delete Card Account with expired token")
response = requests.delete(url + card_accounts + '/' + str(cardID), headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result43 = 'PASS'
else:
    result43 = 'FAIL'


print("Verify User is NOT able to Delete Card Account with Invalid TenantID")
response = requests.delete(url + card_accounts + '/' + str(Invalid), headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode400:
    result44 = 'PASS'
else:
    result44 = 'FAIL'



print("RESULTS: ")
print("POST Add General Setup: " + result1)
print("Verify User NOT able to Post Add General Setup without permission: " + result2)
print("Verify User NOT able to Post Add General Setup with expired token: " + result3)
print("Verify User NOT able to Post Add General Setup without mandatory fields: " + result4)

print("GET General setup details: " + result5)
print("Verify User NOT able to GET General Setup with expired token: " + result6)
print("Verify User NOT able to GET General Setup without permission: " + result7)

print("POST Add Bank Account: " + result8)
print("Verify User is NOT able to Post Add Bank Account without permision: " + result9)
print("Verify User is NOT able to Post Add Bank Account with expired token: " + result10)
print("Verify User is NOT able to Post Add Bank Account without mandatory fields: " + result11)
print("Verify User is NOT able to Post Add Bank Account with Invalid Routing code field: " + result12)
print("Verify User is NOT able to Post Add Bank Account with Invalid Routing code field: " + result13)


print("Get Bank Account: " + result14)
print("Verify User is NOT able to Get Bank Account without permission: " + result15)
print("Verify User is NOT able to Get Bank Account with expired token: " + result16)

print("Put Update Bank Account: " + result17)
print("Verify User is NOT able to Put Update Bank Account without permission: " + result18)
print("Verify User is NOT able to Put Update Bank Account with expired token: " + result19)
print("Verify User is NOT able to Put Update Bank Account without mandatory fields: " + result20)
print("Verify User is NOT able to Put Update Bank Account with Invalid account ID: " + result21)
print("Verify User is NOT able to Put Update Bank Account with Invalid default format code: " + result22)
print("Verify User is NOT able to Put Add Bank Account with Invalid Routing code field: " + result23)

print("Delete Bank Account: " + result24)
print("Verify User is NOT able to Delete Bank Account without permission: " + result25)
print("Verify User is NOT able to Delete Bank Account with expired token: " + result26)
print("Verify User is NOT able to Delete Bank Account with Invalid accountID: " + result27)

print("Post Add Card Account: " + result28)
print("Verify User NOT able to Post Add Card Account without permission: " + result29)
print("Verify User NOT able to Post Add Card Account with expired token: " + result30)
print("Verify user NOT able to Post Add Card Account with negative validity of days: " + result31)
print("Verify user NOT able to Post Add Card Account without mandatory fields: " + result32)


print("Get Card Account: " + result33)
print("Verify User is NOT able to Get Card Account without permission: " + result34)
print("Verify User is NOT able to Get Card Account with expired token: " + result35)


print("PUT Update Card Account: " + result36)
print("Verify User is NOT able to PUT Update Card Account without permission: " + result37)
print("Verify User is NOT able to PUT Update Card Account with expired token: " + result38)
print("Verify User is NOT able to PUT Update Card Account without mandatory fields: " + result39)
print("Verify User is NOT able to PUT Update Card Account with negative validity of days: " + result40)

print("Delete Card Account: " + result41)
print("Verify User is NOT able to Delete Card Account without permission: " + result42)
print("Verify User is NOT able to Delete Card Account with expired token: " + result43)
print("Verify User is NOT able to Delete Card Account with Invalid TenantID: " + result44)