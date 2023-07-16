import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(squirrel_data.info())

### Find number of distinct 'Primary Fur Color'
primary_fur_colors = squirrel_data['Primary Fur Color'].unique()
num_p_fur_colors = []
for color in primary_fur_colors[1:]:
    num_color = len(squirrel_data[squirrel_data['Primary Fur Color'] == color])
    num_p_fur_colors.append(num_color)
    print(f"There are {num_color} of {color} squirrel(s) in the set!")

color_df = pd.DataFrame({'Fur Color': primary_fur_colors[1:], 'Count': num_p_fur_colors})
color_df.to_csv('squirrel_colors.csv')
