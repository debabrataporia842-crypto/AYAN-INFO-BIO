import os
import requests

# Render-এর Environment Variable থেকে টোকেন সংগ্রহ করবে
access_token = os.environ.get("ACCESS_TOKEN")

# আপনার পছন্দমতো লং বায়ো
long_bio = "[FFFFFF]LIKE&OTHERS[FFD700] SELLER\n[FFFF00]TG-[7FFF00]@Ayan202\n[FF4500]INST-redeem_code_ullimited_\n[FFD700]DEVELOPER-[00FF00]AYAN !"

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
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("Success! Long Bio Successfully Updated.")
    else:
        print(f"Failed! Status Code: {response.status_code}")
        print(response.text)
else:
    print("Error: ACCESS_TOKEN not found in Environment Variables!")

