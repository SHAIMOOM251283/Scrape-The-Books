import extract_links
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import json
import os

class BookScraper:

    def __init__(self):
        select_category_instance = extract_links.ExtractCategoryLinks()
        self.category_name, category_url = select_category_instance.run()
        self.base_url = category_url
        self.multi_page = False
        self.page_url_format = None
        self.books_data = []
    
    def detect_if_multi_page(self):
        """Detects if the URL contains multiple pages"""
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for pagination
        pager = soup.find('li', class_='current')
        if pager:
            self.multi_page = True
            self.page_url_format = self.base_url.replace('index.html', f'page-{{page}}.html')

    def extract_data_from_page(self, url):
        """Extracts data from a single page"""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        books = []
        # Find all book items
        book_items = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
        for book in book_items:
            
            # Extract image URL
            image_tag = book.find('div', class_='image_container').a.img
            if image_tag:
                image = image_tag['src']

            # Extract book title and URL
            title_tag = book.h3.a
            if title_tag:
                title = title_tag['title']
                book_url = title_tag['href']

            # Extract price
            price_tag = book.find('p', class_='price_color')
            if price_tag:
                price = price_tag.text

            # Extract stock status
            stock_tag = book.find('p', class_='instock availability')
            if stock_tag:
                stock = stock_tag.text.strip()

            # Extract rating
            rating_tag = book.find('p', class_='star-rating')
            if rating_tag:
                rating_classes = rating_tag['class']
                rating = rating_classes[1] if len(rating_classes) > 1 else None

            books.append({
                'image': image,
                'title': title,
                'url': book_url,
                'price': price,
                'stock': stock,
                'rating': rating
            })
        
        return books

    def extract_data_from_multiple_pages(self):
        """Extracts data from all pages for a multi-page URL"""
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the number of pages from pagination
        page_count = 1
        pager = soup.find('li', class_='current')
        if pager:
            page_count = int(pager.text.strip().split()[-1])
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            print(f"Detected multiple pages. Scraping all pages.")
            for page in range(1, page_count + 1):
                print(f"Processing page {page} of {page_count}")
                page_url = self.page_url_format.format(page=page)
                futures.append(executor.submit(self.extract_data_from_page, page_url))

            for future in futures:
                self.books_data.extend(future.result())

    def extract_data_from_single_page(self):
        """Extracts data from a single-page URL"""
        self.books_data.extend(self.extract_data_from_page(self.base_url))
        print(f"Detected a single page. Scraping this page only.")

    def save_data(self):
        while True:
            select = input("\nSelect json or csv: ").lower().strip()
            if select in ['json', 'csv']:
                break  # Exit the loop when the input is valid
            else:
                print("Invalid input. Please select 'json' or 'csv'.")

        if select == 'json':
            os.makedirs("data_json", exist_ok=True)
            self.filename = f"data_json/{self.category_name}.json"
            with open(self.filename, 'w') as json_file:
                json.dump(self.books_data, json_file, indent=4)
        
        else:
            os.makedirs("data_csv", exist_ok=True)
            df = pd.DataFrame(self.books_data)
            self.filename = f"data_csv/{self.category_name}.csv"
            df.to_csv(self.filename, index=False)

    def run(self):
        """Runs the scraper based on whether the URL has multiple pages or not"""
        self.detect_if_multi_page()
        if self.multi_page:
            self.extract_data_from_multiple_pages()
        else:
            self.extract_data_from_single_page()
            
        self.save_data()
        print(f"Scraping completed and data saved to '{self.filename}'.")

if __name__ == '__main__':
    while True:
        scraper = BookScraper()
        scraper.run()

        another = input("\nDo you want to scrape another category? (yes/no): ").strip().lower()
        print()
        
        if another != 'yes':
            print("Exiting the scraper.")
            break 
