# Costco Financial Analysis (1997-2007)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Import the Excel file
try:
    df = pd.read_excel('costcoBook.xlsx')
    print("Data imported successfully. Shape:", df.shape)
    print("\nFirst few rows of the data:")
    print(df.head())
    print("\nColumn names:")
    print(df.columns)
except FileNotFoundError:
    print("Error: The file 'costcoBook.xlsx' was not found in the current directory.")
    print("Please ensure the file is in the same directory as this Jupyter Notebook.")
except Exception as e:
    print(f"An error occurred while trying to read the file: {e}")
    print("Please check the file format and contents.")

# Function to create and save a line plot
def create_line_plot(x, y, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

# Ensure 'Year' column exists and is set as index
if 'Year' not in df.columns:
    print("Warning: 'Year' column not found. Using default index as years.")
else:
    df.set_index('Year', inplace=True)

# Calculate ROA and ROE
df['ROA'] = df['Net Income'] / df['Total Assets']
df['ROE'] = df['Net Income'] / df['Shareholders Equity']

# Create ROA and ROE trend plots
create_line_plot(df.index, df['ROA'], 'Costco ROA Trend', 'Year', 'ROA', 'costco_roa_trend.png')
create_line_plot(df.index, df['ROE'], 'Costco ROE Trend', 'Year', 'ROE', 'costco_roe_trend.png')

# DuPont Analysis
df['Profit Margin'] = df['Net Income'] / df['Sales']
df['Asset Turnover'] = df['Sales'] / df['Total Assets']
df['Financial Leverage'] = df['Total Assets'] / df['Shareholders Equity']

# Create DuPont Analysis plots
create_line_plot(df.index, df['Profit Margin'], 'Costco Profit Margin Trend', 'Year', 'Profit Margin', 'costco_profit_margin_trend.png')
create_line_plot(df.index, df['Asset Turnover'], 'Costco Asset Turnover Trend', 'Year', 'Asset Turnover', 'costco_asset_turnover_trend.png')
create_line_plot(df.index, df['Financial Leverage'], 'Costco Financial Leverage Trend', 'Year', 'Financial Leverage', 'costco_financial_leverage_trend.png')

# Function to predict future values using linear regression
def predict_future(data, years_to_predict=5):
    x = np.arange(len(data))
    slope, intercept, _, _, _ = stats.linregress(x, data)
    future_x = np.arange(len(data), len(data) + years_to_predict)
    future_y = slope * future_x + intercept
    return future_y

# Predict future values for key metrics
last_year = df.index[-1]
future_years = range(last_year + 1, last_year + 6)
future_roa = predict_future(df['ROA'])
future_roe = predict_future(df['ROE'])

# Create plots with future predictions
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['ROA'], marker='o', label='Historical ROA')
plt.plot(future_years, future_roa, marker='o', linestyle='--', label='Predicted ROA')
plt.title('Costco ROA Trend with Future Predictions')
plt.xlabel('Year')
plt.ylabel('ROA')
plt.legend()
plt.grid(True)
plt.savefig('costco_roa_prediction.png')
plt.close()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['ROE'], marker='o', label='Historical ROE')
plt.plot(future_years, future_roe, marker='o', linestyle='--', label='Predicted ROE')
plt.title('Costco ROE Trend with Future Predictions')
plt.xlabel('Year')
plt.ylabel('ROE')
plt.legend()
plt.grid(True)
plt.savefig('costco_roe_prediction.png')
plt.close()

# Print summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Additional analysis for third-level insights
print("\nYear-over-Year Growth Rates:")
for column in ['Sales', 'Net Income', 'Total Assets', 'Shareholders Equity']:
    df[f'{column} YoY Growth'] = df[column].pct_change() * 100
    print(f"\n{column} YoY Growth:")
    print(df[f'{column} YoY Growth'])

# Analyze membership fees contribution
if 'Membership Fees' in df.columns:
    df['Membership Fees % of Revenue'] = df['Membership Fees'] / df['Sales'] * 100
    print("\nMembership Fees as % of Revenue:")
    print(df['Membership Fees % of Revenue'])

# Analyze operating efficiency
if 'Operating Expenses' in df.columns:
    df['Operating Expense Ratio'] = df['Operating Expenses'] / df['Sales'] * 100
    print("\nOperating Expense Ratio:")
    print(df['Operating Expense Ratio'])

# Analyze debt management
df['Debt to Equity Ratio'] = (df['Total Assets'] - df['Shareholders Equity']) / df['Shareholders Equity']
print("\nDebt to Equity Ratio:")
print(df['Debt to Equity Ratio'])

# You may need to add or modify these calculations based on the actual columns in your Excel file
