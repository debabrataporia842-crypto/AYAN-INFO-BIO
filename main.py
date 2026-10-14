import os
import requests

# Secrets থেকে ACCESS_TOKEN নেওয়া
access_token = os.environ.get("ACCESS_TOKEN")

# আপনার লং বায়ো
long_bio = "[FFFFFF]LIKE & OTHERS [FFD700]SELLER\n[FFFF00]TG - [7FFF00]@Ayan202\n[FF4500]INST - redeem_code_ullimited_\n[FFD700]DEVELOPER - [00FF00]AYAN !"

url = "https://clientbp.ggservices.com/Client/SetSignature"

headers = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; M2007J20CG Build/RKQ1.200826.002)",
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "signature": long_bio
}

if access_token:
    print("Sending request to Free Fire server...")
    response = requests.post(url, headers=headers, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code != 200:
        raise Exception("Failed to update bio!")
else:
    raise Exception("ACCESS_TOKEN secret missing!")
