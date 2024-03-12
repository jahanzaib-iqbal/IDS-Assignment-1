# 3/12/2024
# CSC461 – Assignment1 – IDS – Web Scraping
# JAHANZAIB IQBAL
# FA20-BSE-091
# code for a web scraper in Python  to extract the ‘title’, ‘year’, ‘duration’, and ‘IMDB rating’ for all-time top 250 movies from the IMDB website and export it to a CSV file (tabular format).


import requests
from bs4 import BeautifulSoup
import csv
import os

url = 'https://www.imdb.com/chart/top/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f"Error: {response.status_code}")

containers = soup.find_all('li', class_='ipc-metadata-list-summary-item')

movie_title = []
movie_ratings = []
release_year = []
movie_duration = []

# Extract Movie information
for container in containers:
    # Extracting movie title
    title = container.find('h3', class_='ipc-title__text').text.strip().split('.')[1]
    movie_title.append(title)

    # Extracting movie Ratings
    stars = container.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.strip()[0:4]
    movie_ratings.append(stars)

    # Extracting movie release year
    year = container.find('span', class_='sc-b0691f29-8 ilsLEX cli-title-metadata-item').text
    release_year.append(year)

    # Extracting movie duration
    duration = container.find_all('span', class_='sc-b0691f29-8 ilsLEX cli-title-metadata-item')[1].text
    movie_duration.append(duration)

data = {"movie_title": movie_title,
        "movie_ratings": movie_ratings,
        "release_year": release_year,
        "movie_duration": movie_duration}



csv_file_path = "Movies_Data.csv"

# Writing data to CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:  # Change encoding to 'utf-8-sig'
    fieldnames = ['movie_title', 'movie_ratings', 'release_year', 'movie_duration']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()
    # Write rows
    for i in range(len(movie_title)):
        writer.writerow({'movie_title': movie_title[i],
                         'release_year': release_year[i],
                         'movie_duration': movie_duration[i],
                         'movie_ratings': movie_ratings[i]})

print("Data has been saved to", csv_file_path)
