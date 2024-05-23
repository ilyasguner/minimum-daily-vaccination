import csv


with open('country_vaccination_stats.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    
    
    data = []
    country_vaccinations = {}
    
    for row in reader:
        country = row[0]
        daily_vaccinations = row[2]
        
        if daily_vaccinations:
            daily_vaccinations = int(daily_vaccinations)
            if country not in country_vaccinations:
                country_vaccinations[country] = []
            country_vaccinations[country].append(daily_vaccinations)
        
        data.append(row)

min_vaccinations = {country: min(vaccinations) if vaccinations else 0 for country, vaccinations in country_vaccinations.items()}


for row in data:
    if row[2] == '':
        country = row[0]
        row[2] = str(min_vaccinations.get(country, 0))


with open('country_vaccination_stats.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)