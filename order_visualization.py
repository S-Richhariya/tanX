import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from order_analysis import load_data, total_revenue_by_month, total_revenue_by_product, total_revenue_by_customer, top_customers_by_revenue

# Function to visualize total revenue by month
def visualize_revenue_by_month(df):
    # Calculate total revenue by month
    revenue_by_month = total_revenue_by_month(df)
    # Convert period index to string for plotting
    revenue_by_month.index = revenue_by_month.index.astype(str)
    
    # Plotting
    plt.figure(figsize=(10, 5))
    sns.barplot(x=revenue_by_month.index, y=revenue_by_month.values, palette="viridis")
    plt.title('Total Revenue by Month')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to avoid clipping
    plt.show()

# Function to visualize total revenue by product
def visualize_revenue_by_product(df):
    # Calculate total revenue by product
    revenue_by_product = total_revenue_by_product(df)
    
    # Plotting
    plt.figure(figsize=(10, 5))
    sns.barplot(x=revenue_by_product.index, y=revenue_by_product.values, palette="coolwarm")
    plt.title('Total Revenue by Product')
    plt.xlabel('Product Name')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45, ha="right")  # Rotate and align x-axis labels
    plt.tight_layout()
    plt.show()

# Function to visualize total revenue by each customer
def visualize_revenue_by_customer(df):
    revenue_by_customer = total_revenue_by_customer(df)
    
    plt.figure(figsize=(10, 5))
    sns.barplot(x=revenue_by_customer.index.astype(str), y=revenue_by_customer.values, palette="cividis")
    plt.title('Total Revenue by Customer')
    plt.xlabel('Customer ID')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to visualize the top N customers by revenue
def visualize_top_customers(df, top_n=10):
    # Calculate total revenue for each customer and get the top N customers
    top_customers = top_customers_by_revenue(df, top_n=top_n)
    
    # Plotting
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_customers.index.astype(str), y=top_customers.values, palette="magma")
    plt.title(f'Top {top_n} Customers by Revenue')
    plt.xlabel('Customer ID')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to load data and create visualizations
def main():
    # File path to the dataset{Use file path according to your file location}
    file_path = "C:\\Users\\91945\\Desktop\\tanX\\orders.csv"
    
    # Load data from the CSV file
    df = load_data(file_path)
    
    # Check if data is loaded successfully
    if df is not None:
        # Visualize total revenue by month
        visualize_revenue_by_month(df)
        # Visualize total revenue by product
        visualize_revenue_by_product(df)
        # Visualize total revenue by customer
        visualize_revenue_by_customer(df)
        # Visualize top N customers by revenue
        visualize_top_customers(df, top_n=10)

# Entry point for the script
if __name__ == "__main__":
    main()
