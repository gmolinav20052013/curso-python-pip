import matplotlib.pyplot as plt
import readcsv
import pandas as pd


def generate_bar_chart(labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    # ax.pie(values, labels=labels, autopct='%1.1f')
    # plt.show()
    plt.savefig('pie.png')
    plt.close()


def get_population(country_dict):
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population']),
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def population_by_country(data,country):
    result = list(filter(lambda item: item['Country/Territory'] == country,data))
    return result

df = pd.read_csv('./wpopulation.csv')
df = df[df['Continent'] == 'South America']
print(df)

countries = df['Country/Territory'].values
percentages = df['World Population Percentage'].values

generate_pie_chart(countries,percentages)





# data = readcsv.read_csv('./wpopulation.csv')
'''
country = input('Digite el pais => ')
result = population_by_country(data,country)

if len(result) > 0:
    country = result[0]
    labels, values = get_population(country)
    generate_bar_chart(labels, values)
'''

# labels = ['a','b','c']
# values = [100,200,380]
# generate_bar_chart(labels,values)
# generate_pie_chart(labels,values)

