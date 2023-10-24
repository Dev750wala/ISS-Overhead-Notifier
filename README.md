# ISS-Overhead-Notifier
Heyy Astrophile🙋‍♂️, Be ready to observe the ISS in the night sky. The "ISS Overhead Notifier" is a Python script that checks at 60-second intervals whether the International Space Station (ISS) is passing over a user-specified location and if it is nighttime in that area. This project uses real-time ISS location data from the **Open Notify API** and sunrise/sunset information from the Sunrise-Sunset API. When both conditions are met (the ISS is overhead, and it's nighttime), the script sends an email notification to the user.

# Key Features 🗝️:
Continuously monitors the ISS location.
Determines day or night based on sunrise and sunset times.
Sends an email alert when the ISS is overhead and it's nighttime.
Configurable with user-specific latitude, longitude, email, and password.
How It Works:
The script periodically fetches the ISS's latitude and longitude and checks the time of day at the user's specified location. If the ISS is overhead and it's nighttime, an email is sent using the provided Gmail credentials. Users can adapt the code by setting their latitude and longitude for accurate tracking.

# Usage:
Ideal for space enthusiasts, the "ISS Overhead Notifier" allows users to receive email notifications, prompting them to look up at the night sky and witness the ISS's passage through their area. The project offers an automated and convenient way to stay informed about ISS sightings, making it accessible to anyone interested in space exploration.

# Note:
To use this code, users must replace the MY_LAT and MY_LONG variables with their specific coordinates and input their Gmail credentials into the EMAIL and PASSWORD variables. Users may need to configure their Gmail settings to allow less secure apps or use an app password, especially if two-factor authentication is enabled.

Experience the wonder of space by tracking the ISS effortlessly with the "ISS Overhead Notifier."
