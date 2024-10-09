import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class ExtractCategoryLinks:
    def __init__(self):
        self.home_page_url = "http://books.toscrape.com/"
        self.response = requests.get(self.home_page_url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.links = {}

    def extract_category_links(self):
        #links = {}
        # Locate the 'side_categories' div
        link_containers = self.soup.find('div', class_='side_categories')
        
        # Find all 'a' tags within 'side_categories' that point to category links
        for link_tag in link_containers.find_all('a'):
            # Extract the name and URL of the category
            name = link_tag.text.strip()  # Strip to remove leading/trailing whitespace
            link_url = urljoin(self.home_page_url, link_tag['href'])  # Build absolute URL
            
            # Add the category to the dictionary
            self.links[name] = link_url
        
        # Print all the category links
        for name, url in self.links.items():
            print(f"{name}: {url}")
        
    def select_category(self):
        # Prompt the user to select a category by name
        selected_category = input("\nEnter the name of the category: ")
        
        # Check if the category exists in the dictionary
        if selected_category in self.links:
            print(f"You selected: {selected_category}")
            print(f"Category URL: {self.links[selected_category]}")
            return selected_category, self.links[selected_category]
        else:
            print("Category not found. Please try again.")
            return None, None
    
    def run(self):
        self.extract_category_links() 
        category_name, category_url = self.select_category()
        return category_name, category_url

if __name__ == '__main__':
    extraction = ExtractCategoryLinks()
    extraction.run()
