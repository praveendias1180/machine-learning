import matplotlib.pyplot as plt

# Training Data Examples for rain and no_rain
rain_temp,rain_humidity = [45,55,55],[60,65,55]
no_rain_temp,no_rain_humidity=[35,50,40],[45,30,35]
# Unknown new data point that needs to be labeled for rain or no rain
new_data_temp,new_data_humidity=40,50

# Simple distance based approach to lable the unknown new data point
rain=0
no_rain=0
sz=len(rain_temp)
for i in range(sz):
  rain+=abs(rain_temp[i]-new_data_temp)**2
  rain+=abs(rain_humidity[i]-new_data_humidity)**2
  no_rain+=abs(no_rain_temp[i]-new_data_temp)**2
  no_rain+=abs(no_rain_humidity[i]-new_data_humidity)**2
print("Distance to Rain data =", rain)
print("Distance to No Rain data = ", no_rain)

# Print the label of unknown new data point based on the total distance to each group
if rain < no_rain: 
  print("It is going to RAIN")
else:
  print("It is NOT going to Rain")

# Plot the data points for rain / no_rain and unknown new data
plt.scatter(rain_temp,rain_humidity,marker='^')
plt.scatter(no_rain_temp,no_rain_humidity,marker='o')
plt.scatter(new_data_temp,new_data_humidity,marker='x')
plt.legend(["rain","no_rain","new data"])
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.show()  