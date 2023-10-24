import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 14.604806     # <-- here goes your location latitude
MY_LONG = -157.134082  # <-- here goes your location longitude

EMAIL = "abc@gmail.com"         # Your email
PASSWORD = "abcdefghijklmnop"   # your app password


# To check if the ISS is nearby me or not
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    latitude_diff = abs(iss_latitude - MY_LAT)
    longitude_diff = abs(iss_longitude - MY_LONG)

    return True if latitude_diff < 5 and longitude_diff < 5 else False


# To cheque if there is a night or not
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    return True if sunset < current_hour < sunrise else False


# If the both conditions like ISS is overhead and there is a night then both of the functions will return true,
# and now we will email to ourselves to look up in the sky to track the ISS.
while True:
    time.sleep(60)

    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                                from_addr=EMAIL,
                                to_addrs=EMAIL,
                                msg="Subject:Look up 🧑‍🚀🚀\n\n"
                                    "ISS is going to pass through your location in a short period of time".encode("utf-8")
                                )
