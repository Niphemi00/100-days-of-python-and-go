# DAY 25: WORKING WITH PANDAS AND IT LIBRARY
# import csv
# temp_list = []
# with open("weather_data.csv") as datafile:
#     data = csv.reader(datafile)
#     next(data)
#     for row in data:
#         temp_list.append(int(row[1]))
#     print(temp_list)
    
# To activate the virtual enviroment use the ".venv\Scripts\Activate" command 
# to deactivate it use "deactivate"
import pandas as pd
# data = pd.read_csv("weather_data.csv")

# # print(data['temp']) 


# # When working with pandas always look up the documentation
# # in panda we have two sets of data

#     # 1. the series data set which seems like a list data type
#     # 2. the dataframe data set which works like a dictionary datatypes
# # data = data.to_dict()
# # print(data)

# # calculating average temprature
# temp_data = data['temp']
# # print(temp_data.max())

# monday = data[data.day == "Monday"]

# monday_temp_in_farhenheit = (monday.temp * 1.8) + 32
# print(monday_temp_in_farhenheit)



# # creating a dataframe from scratch 
# data_dict = {
#     "Id" : [1, 2, 3],
#     "Students" : ['john', 'liam', 'jane'],
#     "marks" : [32, 83, 73]
# }

# df = pd.DataFrame(data_dict, index=data_dict['Id'])
# df.to_csv("df.csv")
# print(df)


# Squirell project challenge
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250214.csv")
df = {
    "Colors": ['Gray', 'Cinnamon', 'Black'],
    "Count": []
}
for color in df["Colors"]:
    colors_count = len(data[data["Primary Fur Color"] == color])
    df["Count"].append(colors_count)
print(df)
df = pd.DataFrame(df)
df.to_csv("squirrel_count.csv")
# print(grey_colors)