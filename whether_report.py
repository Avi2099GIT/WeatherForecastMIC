# write a python code to print the weather report from API site openwhethermap.org using the city name given by the user as input
# import required modules
import requests, json
import os
city= input("enter your city:")
apiid="28a0c58572afdcd5aa1ee5f18d2f9d2a"
website="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiid
# get method of requests module
# return response object
response = requests.get(website)
# json method of response object convert
# json format data into python format data
x = response.json()
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
    # store the value of "main"
    # key in variable y
    y = x["main"]
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
    # store the value corresponding
    # to the "humidity" key of y
    current_humidiy = y["humidity"]
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))