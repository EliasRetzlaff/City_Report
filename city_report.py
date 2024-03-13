# city_report.py
# Written by Elias Retzlaff

import random

cities = ['Chicago', 'New York', 'Los Angeles', 'Houston']

def city_select(city_list):

    for city in city_list:

        if random.random() < 0.4:

            return city

    return 'Utopia'

def generate_counts(city_list, num_trials):

    count_table = dict()

    for i in range(num_trials):

        selection = city_select(city_list)

        count_table[selection] = count_table.get(selection, 0) + 1

    return count_table

def city_report(city_list, num_trials):

    count_table = generate_counts(city_list, num_trials)

    for city in city_list:

        count = count_table.get(city, 0)

        percentage = count / num_trials * 100

        print(f"City: {city} - Count: {count} - Percentage: {percentage}%")

    max_city = max(count_table, key=count_table.get)

    max_count = count_table[max_city]

    max_percentage = max_count / num_trials * 100

    print(f"City with the most selections: {max_city}")
