import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

class DataVisualization:

    def __init__(self):
        # Load the CSV file
        self.df = pd.read_csv('data_csv\Books.csv')
        # Clean the price column to convert it to numeric
        self.df['price'] = self.df['price'].replace({'£': '', 'Â': ''}, regex=True).astype(float)
        # Convert stock to a categorical variable for better plotting
        self.df['stock'] = self.df['stock'].astype('category')
        # Convert ratings to a numerical value
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        self.df['rating'] = self.df['rating'].map(rating_map).astype(float)

    def scatter_plot(self):
        fig = px.scatter(self.df, x='price', y='rating', color='stock', hover_data=['title', 'url'])
        fig.update_layout(title='Price vs. Rating Scatter Plot', xaxis_title='Price (£)', yaxis_title='Rating')
        fig.show()

    def histogram(self):
        fig = px.histogram(self.df, x='price', nbins=20, color='stock')
        fig.update_layout(title='Histogram of Book Prices', xaxis_title='Price (£)', yaxis_title='Count')
        fig.show()

    def bar_chart(self):
        price_by_rating = self.df.groupby('rating')['price'].mean().reset_index()
        num_bars = len(price_by_rating)
        bar_colors = px.colors.qualitative.Plotly[:num_bars]
        fig = go.Figure([go.Bar(x=price_by_rating['rating'], y=price_by_rating['price'], marker=dict(color=bar_colors))])
        fig.update_layout(title='Grouped Bar Chart: Average Price by Rating', xaxis_title='Rating', yaxis_title='Average Price (£)')
        fig.show()
    
    def run(self):
        self.scatter_plot()
        self.histogram()
        self.bar_chart()

if __name__ == '__main__':
    visualize = DataVisualization()
    visualize.run()