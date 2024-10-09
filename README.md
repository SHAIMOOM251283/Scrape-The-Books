# Scrape The Books

**Scrape The Books** is a Python project that extracts book data from the **Books to Scrape** website, processes and saves the data, and provides visualizations to analyze various aspects of the scraped information. The project is structured into three main scripts: `extract_links.py`, `extract_data.py`, and `data_visualization.py`.

## Project Structure

- **extract_links.py**: Extracts category links from the homepage and prompts the user to select a category to scrape.
- **extract_data.py**: Scrapes book data (title, price, rating, availability, and more) from the selected category. It handles both single-page and multi-page categories by checking for pagination with BeautifulSoup. If multiple pages are detected, it constructs the URLs and scrapes them concurrently using multithreading with **ThreadPoolExecutor** for enhanced performance. The scraped data is saved in either JSON or CSV format.
- **data_visualization.py**: Reads the saved CSV file and generates visualizations (scatter plot, histogram, and bar chart) to analyze the book data using Plotly. The script provides the following insights:

  - **Scatter Plot**: 
    The scatter plot visualizes the relationship between **book price** and **rating**. Each point represents a book, with the **x-axis** showing the price (in £) and the **y-axis** showing the rating. Additionally, hovering over any point reveals more details such as the book's title and URL. This visualization helps users identify trends, such as whether higher-rated books are typically more expensive.
    ![Scatter Plot](https://github.com/SHAIMOOM251283/scrape_the_books/blob/main/scatter_plot.png)

  - **Histogram**: 
    This histogram shows the **distribution of book prices** across the dataset. The **x-axis** is divided into price ranges (bins), while the **y-axis** shows how many books fall into each price range. This provides an overview of how prices are distributed and whether certain price points are more common.
    ![Histogram](https://github.com/SHAIMOOM251283/scrape_the_books/blob/main/histogram.png)

  - **Bar Chart**: 
    The bar chart presents the **average price of books for each rating category**. The **x-axis** represents the rating (1-star to 5-star), and the **y-axis** shows the **average price** of books within that rating. Each bar is uniquely colored, making it visually easy to compare price differences between ratings. This chart helps answer questions like whether higher-rated books generally have higher average prices.
    ![Bar chart](https://github.com/SHAIMOOM251283/scrape_the_books/blob/main/bar_chart.png)

## Requirements

To run this project, the following Python libraries are required:
- `requests`
- `beautifulsoup4`
- `pandas`
- `plotly`
- `concurrent.futures` (part of Python's standard library)

## Installation

1. **Clone the repository using the terminal**:
   ```bash
   git clone https://github.com/SHAIMOOM251283/scrape_the_books.git
   cd scrape_the_books
   ```

2. **Clone the repository using VS Code's Git integration**:
   - Open **VS Code**.
   - Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) to open the **Command Palette**.
   - Type `Git: Clone` and select the option.
   - Enter the repository URL: `https://github.com/SHAIMOOM251283/scrape_the_books.git`.
   - Choose a local folder to clone the repository into, and select **Open** to load it in VS Code.

3. **Clone the repository using VS Code's Integrated Terminal**:
   - Open **VS Code** and open the integrated terminal by pressing `Ctrl + `` (backtick)` or navigating to **Terminal** > **New Terminal**.
   - Run the following commands:
   ```bash
   git clone https://github.com/SHAIMOOM251283/scrape_the_books.git
   cd scrape_the_books
   ```

4. **Install the required dependencies**:
   Run the following command in the terminal:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Extracting Category Links and Scraping Book Data

To extract book data:
```bash
python extract_data.py
```
This script will:
- Extract category links from the homepage of *Books to Scrape*.
- Prompt you to select a category.
- Detect if the category spans multiple pages and scrape all book data.
- Use **multithreading** with `ThreadPoolExecutor` to scrape multiple pages simultaneously, improving performance.
- Save the scraped data in your preferred format (JSON or CSV).

### 2. Visualizing the Data

Once the data is saved, you can generate visualizations by running:
```bash
python data_visualization.py
```
This script will:
- Load the saved CSV file.
- Generate three interactive visualizations using Plotly:
  - A scatter plot showing the relationship between book price and rating, with stock availability indicated by color.
  - A histogram depicting the distribution of book prices.
  - A bar chart displaying the average price for each book rating.

## Features

- **Web Scraping**: Efficiently scrapes book data using BeautifulSoup, handling both single-page and multi-page categories.
- **Multithreading**: Uses `ThreadPoolExecutor` to handle multiple pages concurrently, significantly reducing scraping time.
- **Data Saving**: Saves the scraped data in either JSON or CSV format for further use.
- **Data Visualization**: Generates dynamic, interactive visualizations using Plotly to analyze book price distribution, rating trends, and availability.

## Project Structure

```
scrape_the_books/
│
├── data_csv/                # Directory for CSV files (auto-generated)
├── data_json/               # Directory for JSON files (auto-generated)
├── data_visualization.py    # Generates visualizations of the scraped data
├── extract_data.py          # Scrapes book data from selected categories with multithreading
├── extract_links.py         # Extracts category links from the homepage
└── requirements.txt         # Python dependencies
```

## Conclusion

This project demonstrates efficient web scraping techniques using Python, BeautifulSoup, and multithreading, along with data visualization using Plotly. By employing **multithreading** with `ThreadPoolExecutor`, the scraper can process multiple pages in parallel, reducing overall execution time. Additionally, the visualizations provide insights into the scraped data, making it easier to analyze price trends, ratings, and availability.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
