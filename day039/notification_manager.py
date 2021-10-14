import smtplib
import os
import json
class NotificationManager:
    ROOT = os.path.dirname(os.path.abspath(__file__))+"/"

    def __init__(self,valid_flights):
        self.load_api_key()
        for flight in valid_flights:
            self.send(flight)
    
    def load_api_key(self):
        with open(f"{self.ROOT}email.key") as email_file:
            self.EMAIL_DATA = json.load(fp=email_file)

    def send(self,flight):
        
        with smtplib.SMTP(self.EMAIL_DATA["Host"]) as smtp:
            smtp.starttls()
            smtp.login(self.EMAIL_DATA["Username"],self.EMAIL_DATA["Password"])
            smtp.sendmail(from_addr=self.EMAIL_DATA["Username"],to_addrs=self.EMAIL_DATA["ToEmail"],msg=f"To: {self.EMAIL_DATA['ToEmail']}\nSubject: Cheap flight to {flight.city_to}\n\nLow price alert! Only £{flight.price} to fly from {flight.city_to}-{flight.to_code} to {flight.city_from}-{flight.from_code} , from {flight.from_date.strftime('%d/%m/%Y')} to {flight.to_date.strftime('%d/%m/%Y')}.".encode("ascii","ignore").decode("ascii"))