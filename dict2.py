weather = {
    "city": "Москва",
    "temperature": "20"
}
weather["temperature"]= int(weather["temperature"]) - 5
print(weather.get("country","russia"))
weather["date"] = "27.05.2019"
print(weather)
print(len(weather))
print("country" in weather)