# Credentials/Input to get the token
from random import randint

#
token_url = 'https://identity.qa-regalpay.io/connect/token'
Username = 'ruchita@regal-us.com'
Password = 'Ruchita@1234'
INC_client_id = 'WellsFargoConnectApp'
INC_client_secret = 'QN9wyWRJPdr2KTYp'
grant_type = 'password'
INC_Scope = 'i'
tenantId = '8e2c92e8-b3e8-468b-800b-08d8f4145c92'
ACR_VALUES = "tenant:8e2c92e8-b3e8-468b-800b-08d8f4145c92"

#urls

url = 'https://api.qa-regalpay.io'
payments = '/wellsfargo-connect/payments'
setup = '/wellsfargo-connect/setup'
credentials = '/wellsfargo-connect/credentials'
vendors = '/wellsfargo-connect/vendors'

random_value1 = randint(11111, 99999)
ExpectedCode201 = 201
ExpectedCode200 = 200

#

vendorType= 'Single Location'
companyId = 'companyId'
dateFormat = 'yyyy-MM-dd'
credentialName = 'credentialName'
password = 'Atlanta2009!'
userId ='admin'
Start_date = ''
End_date = ''