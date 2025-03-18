import pandas

data_csv_file = 'squirrel_data.csv'
colors = ['Gray', 'Black', 'Cinnamon']
final_dict = {}

squirrel_data = pandas.read_csv(data_csv_file)
s_primary_fur_color = squirrel_data['Primary Fur Color']


for color in colors:
    color_count = len(squirrel_data[s_primary_fur_color == color])
    print(f'With {color} there are {color_count} squirrels')

    final_dict[color] = color_count

print(final_dict)

pandas.DataFrame(list(final_dict.items()), columns=['Color', 'Count']).to_csv('new_csv.csv')
