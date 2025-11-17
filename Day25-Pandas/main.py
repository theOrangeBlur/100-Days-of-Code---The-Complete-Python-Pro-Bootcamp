#weather_list = []
#with open("Day25-Pandas/weather_data.csv") as file:
#    for line in file.readlines():
#        line = line.replace('\n','')
#        weather_list.append(line)
#
#print(weather_list)

#print(temperatures)

import pandas

#data = pandas.read_csv("Day25-Pandas/weather_data.csv")
#print(f"Average temp: {data["temp"].mean()}")
#print(f"Max temp: {data["temp"].max()}")
#print(data[data.temp == 14])
#temp_C = data[data.day == "Monday"].temp
#print(f"{temp_C[0]}C -> {temp_C.tolist()[0]*9/5 + 32}F")

data = pandas.read_csv("Day25-Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251117.csv")
gray_num = data[data["Primary Fur Color"] == "Gray"].shape[0]
red_num = data[data["Primary Fur Color"] == "Cinnamon"].shape[0]
black_num = data[data["Primary Fur Color"] == "Black"].shape[0]

col_index = ["Fur Color", "Count"]
row_index = ["Gray", "Cinnamon", "Black"]
row_values = [gray_num, red_num, black_num]
my_dict = {
    "Fur Color": row_index,
    "Count": row_values
}
my_db = pandas.DataFrame(my_dict)

my_db.to_csv("Day25-Pandas/Squirrell_count.csv")