#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
data_manager.setup_locations()

flights = data_manager.get_valid_flights()
print(flights)
#notification_manager = NotificationManager(flights)