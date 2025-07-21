import requests
from datetime import datetime
from config import send_mail
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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
hour = time_now.hour
def location(lat, lng):
    if lat == MY_LAT and lng == MY_LONG:
        return True
    if lat + 5 == MY_LAT or lat - 5 == MY_LAT and lng + 5 == MY_LONG or lng - 5 == MY_LONG:
        return True
    return False

is_close = location(lat = iss_latitude, lng = iss_longitude)

print(sunset)
#If the ISS is close to my current position
if is_close and 21 >= sunset: 
# and it is currently dark
# Then send me an email to tell me to look up.
    send_mail()
# BONUS: run the code every 60 seconds.



