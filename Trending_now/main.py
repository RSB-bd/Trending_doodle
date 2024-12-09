# Web Scraping
import pandas as pd
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template

# website URL
url = "https://homeshopping.pk/categories/Mobile-Phones-Price-Pakistan/"
# sending the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # finding the main container
    divs = soup.find('div', class_='row ProductsList').find_all('div', class_='innerp')

    # extracting data by elements
    divs[0].find('h5', class_='ProductDetails').find('a').text.strip()
    divs[0].find('div', class_='ActualPrice').text.strip()
    divs[0].find('h5', class_='ProductDetails').find('a').get('href')
    divs[0].find('img', class_='img-responsive').get('data-src')
    divs[0].find('span', class_='total_sold_count').get('data-product_id')

    # creating a DataFrame using pandas
    dataFrame = pd.DataFrame(columns=['ID', 'Name', 'Price', 'IMG', 'URL'])
    # collecting datas in a loop
    for div in divs:
        new_data = {'ID': div.find('span', class_='total_sold_count').get('data-product_id'),
                    'Name': div.find('h5', class_='ProductDetails').find('a').text.strip(),
                    'Price': div.find('div', class_='ActualPrice').text.strip(),
                    'IMG': div.find('img', class_='img-responsive').get('data-src'),
                    'URL': div.find('h5', class_='ProductDetails').find('a').get('href')}

        # append those data to new dataFrame
        new_df = pd.DataFrame([new_data])
        dataFrame = pd.concat([dataFrame, new_df], ignore_index=True)
        # saving the file to CSV format
        dataFrame.to_csv('product_data.csv')

    print("The data has been successfully saved to product_data.csv.")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)




