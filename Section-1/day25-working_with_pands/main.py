# with open(file="weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import  csv
#
# with  open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempraturs = []
#
#     for row in data:
#         if row[1] != "temp":
#             tempraturs.append(int(row[1]))
#
# print(tempraturs)

import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].tolist()

# print(data["temp"].mean())
# print(data["temp"].nsmallest())
# print("##############")
# print(data["temp"].max())
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
#
# # get data is row
#
# # this will get with old way
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])
#
# # this will get with pands libray
# print(data[data.temp == data["temp"].max()])


# monday = data[data.day == "Monday"]
# monday_temp_f = monday.temp * 1.8 + 32
# print(monday_temp_f)


# create DataFrame from Scratch

# data_dict = {
#     "students" : ["Sushant", "Prashant", "Mahesh", "Ashish"],
#     "scores" : [ 99, 88, 80, 75 ]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("cus_data.csv")


# ////////////////////////////////////////////
# working with nyc open data for analyse

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_colors = data["Primary Fur Color"].filter("Gray")
print(primary_colors)

