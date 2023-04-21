# CIS-117 Lab 4
# Reads a CSV file containing information on countries and splits the countries by region,
# generating one file per region.
# Group 3
# Henry Penas, James Loft

import csv

region_countries = {}

try:
    with open('country_full.csv', 'r') as input_file:
        reader = csv.DictReader(input_file)

        for row in reader:
            region = row['region']
            country = row['name']

            if not region:
                region = "Not Listed"

            if region in region_countries:
                region_countries[region].append(country)
            else:
                region_countries[region] = [country]

    for region, countries in region_countries.items():
        with open(region + '.csv', 'w') as region_file:
            writer = csv.writer(region_file)
            writer.writerow(['Country'])
            for country in countries:
                writer.writerow([country])

except Exception as e:
    print("An error occurred: ", str(e))
