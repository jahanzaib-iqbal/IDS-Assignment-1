# 3/12/2024
# CSC461 – Assignment1 – IDS – Web Scraping
# JAHANZAIB IQBAL
# FA20-BSE-091
# code for a web scraper in Python  to extract the MARS PLANET PROFILE from the given website and export it to a CSV file (tabular format).


import requests
from bs4 import BeautifulSoup
import csv

url = "https://space-facts.com/mars/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"id": "tablepress-p-mars-no-2"})

data = []

# Loop through each row in the table
for row in table.find_all("tr"):
    columns = row.find_all("td", class_=["column-1", "column-2"])
    if columns:
        # Extract text from column 1 and column 2
        column1_data = columns[0].get_text(strip=True)
        column2_data = columns[1].get_text(strip=True)
        data.append([column1_data, column2_data])

csv_file_path = "mars_facts.csv"

# Write data to the CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['MARS PLANET PROFILE',''])
    writer.writerow(['Attribute', 'Value'])
    # Write data rows
    writer.writerows(data)

print("Data has been saved to", csv_file_path)
