import csv
import pandas

csv_file = 'weather_data.csv'
with open(file=csv_file) as file:
    csv_list = file.readlines()

    # print(csv_list)

temp = []
with open(file=csv_file) as file:
    data = csv.reader(file)
    next(data)
    temp = []
    for row in data:
        temp.append(int(row[1]))
        # print(row)

    # print(temp)

data = pandas.read_csv(csv_file)
temp = data['temp']
print(data)
# print(data.to_dict())
# print(temp.to_list())

print(temp.mean())
print(temp.max())
print(temp.min())
print(temp.count())

print(data[data.temp == temp.max()])


data_dict = {
    'students' : ['AAA', 'BBB', 'CCC'],
    'grades' : [100,90,80]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv('new_csv.csv')
