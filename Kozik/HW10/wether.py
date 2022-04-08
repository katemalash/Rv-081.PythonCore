from pyowm import OWM

city = input('Enter city: ')
owm = OWM('42c78f34ac2388b0f8d5bbde901659ec')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather

print(f"In {city} city is temperature of the air - {w.temperature('celsius')['temp']} for the Celsius.")
print(f"In this city {w.detailed_status}.")
