import csv

def read_csv(filename):
    data = []
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        # print(header)
        # print(type(header))
        for row in reader:
            iteralble = zip(header,row)
            country_dict = {key: value for key, value in iteralble}
            data.append(country_dict)
    return data

# datos = read_csv('wpopulation.csv')

# print(datos)