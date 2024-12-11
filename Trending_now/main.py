# Web Scraping
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv_to_html

# website URL
url = "https://www.ikea.com/us/en/cat/duvet-cover-sets-10680/"
# sending the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # finding the main container
    divs = soup.find('div', class_='plp-product-list__products').find_all('div', class_='plp-fragment-wrapper')

    # extracting data by elements
    # print(divs[0].find('div', class_='plp-mastercard').get('data-ref-id'))
    # print(divs[0].find('div', class_='plp-mastercard').get('data-product-name'))
    # print(divs[0].find('span', class_='plp-price-module__description').text.strip())
    # print(divs[0].find('div', class_='plp-mastercard').get('data-price'))
    # print(divs[0].find('div', class_='plp-mastercard').get('data-currency'))
    # print(divs[0].find('span', class_='plp-text plp-text--body-m plp-icon-text__text').text.strip())
    # print(divs[0].find('a', class_='plp-product__image-link').get('href'))
    # print(divs[0].find('img', class_='plp-image plp-product__image').get('src'))

    # divs[0].find('div', class_='ActualPrice').text.strip()
    # divs[0].find('h5', class_='ProductDetails').find('a').get('href')
    # divs[0].find('img', class_='img-responsive').get('data-src')
    # divs[0].find('span', class_='total_sold_count').get('data-product_id')

    # creating a DataFrame using pandas
    dataFrame = pd.DataFrame(columns=['Product ID', 'Name', 'Description', 'Price', 'Currency', 'Material', 'URL', 'IMG'])
    # collecting all available data in a loop
    for div in divs:
        new_data = {'Product ID': div.find('div', class_='plp-mastercard').get('data-ref-id'),
                    'Name': div.find('div', class_='plp-mastercard').get('data-product-name'),
                    'Description': div.find('span', class_='plp-price-module__description').text.strip(),
                    'Price': div.find('div', class_='plp-mastercard').get('data-price'),
                    'Currency': div.find('div', class_='plp-mastercard').get('data-currency'),
                    'Material': div.find('span', class_='plp-text plp-text--body-m plp-icon-text__text').text.strip(),
                    'URL': div.find('a', class_='plp-product__image-link').get('href'),
                    'IMG': div.find('img', class_='plp-image plp-product__image').get('src')}

        # append those data to new dataFrame
        new_df = pd.DataFrame([new_data])
        dataFrame = pd.concat([dataFrame, new_df], ignore_index=True)
        # saving the file to CSV format
        dataFrame.to_csv('product_data.csv')
        # csv_to_html.index()

    print("The data has been successfully saved to product_data.csv.")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)




