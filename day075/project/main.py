import pandas as pd
import matplotlib.pyplot as plt

df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')


# Challenge:
#     What are the shapes of the dataframes?
#     How many rows and columns?
#     What are the column names?
#     Complete the f-string to show the largest/smallest number in the search data column
#     Try the .describe() function to see some useful descriptive statistics
#     What is the periodicity of the time series data (daily, weekly, monthly)?
#     What does a value of 100 in the Google Trend search popularity actually mean?
dfs = [df_tesla, df_unemployment, df_btc_price, df_btc_search]

for df in dfs:
  print("DATAFRAME")
  print(f"shape: {df.shape}")
  print(f"rows: {df.shape[0]}")
  print(f"columns: {df.shape[1]}")
  print(f"column names: {df.columns}")
  max = df[df.columns[1]].max()
  print(f"max: {max}")
  min = df[df.columns[1]].min()
  print(f"min: {min}")
  print(f"desc: {df.describe()}")
  print(f"periodicity: {df.columns[0]}")
  print("==========\n")

max = df_tesla['TSLA_WEB_SEARCH'].max()
min = df_tesla['TSLA_WEB_SEARCH'].min()
print(f'Largest value for Tesla in Web Search: {max}')
print(f'Smallest value for Tesla in Web Search: {min}')

max = df_unemployment['UE_BENEFITS_WEB_SEARCH'].max()
print('Largest value for "Unemployemnt Benefits" in Web Search: {max}')

max = df_btc_search['BTC_NEWS_SEARCH'].max()
print(f'largest BTC News Search: {max}')

# Challenge: Are there any missing values in any of the dataframes? If so, which row/rows have missing values? How many missing values are there?
tesla_nan = len(df_tesla) * len(df_tesla.columns) - df_tesla.count().sum()
ue_nan = len(df_unemployment) * len(df_unemployment.columns) - df_unemployment.count().sum()
btc_nan = len(df_btc_search) * len(df_btc_search.columns) - df_btc_search.count().sum()
print(f'Missing values for Tesla?: {tesla_nan}')
print(f'Missing values for U/E?: {ue_nan}')
print(f'Missing values for BTC Search?: {btc_nan}')

btcp_nan = len(df_btc_price) * len(df_btc_price.columns) - df_btc_price.count().sum()
print(f'Missing values for BTC price?: {btcp_nan}')

total_nan = tesla_nan + ue_nan + btc_nan + btcp_nan
print(f'Number of missing values: {total_nan}')

# Challenge: Remove any missing values that you found.
df_btc_price.dropna(inplace=True)

# Challenge: Check the data type of the entries in the DataFrame MONTH or DATE columns. Convert any strings in to Datetime objects. Do this for all 4 DataFrames. Double check if your type conversion was successful.
df_tesla['MONTH'] = pd.to_datetime(df_tesla['MONTH'])
df_unemployment['MONTH'] = pd.to_datetime(df_unemployment['MONTH'])
df_btc_price['DATE'] = pd.to_datetime(df_btc_price['DATE'])
df_btc_search['MONTH'] = pd.to_datetime(df_btc_search['MONTH'])

print(type(df_tesla['MONTH'][0]))
print(type(df_unemployment['MONTH'][0]))
print(type(df_btc_price['DATE'][0]))
print(type(df_btc_search['MONTH'][0]))

# Converting from Daily to Monthly Data
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()

# Create locators for ticks on the time axis
import matplotlib.dates as mdates

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)

plt.show()


# Bitcoin (BTC) Price v.s. Search Volume
plt.figure(figsize=(14, 8), dpi=120)

plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])

# Experiment with the linestyle and markers
ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE,
         color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH,
         color='skyblue', linewidth=3, marker='o')

plt.show()


# Unemployement Benefits Search vs. Actual Unemployment in the U.S.
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])

# Show the grid lines as dark grey lines
ax1.grid(color='grey', linestyle='--')

# Change the dataset used
ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE,
         color='purple', linewidth=3, linestyle='--')
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH,
         color='skyblue', linewidth=3)

plt.show()

# Challenge: Calculate the 3-month or 6-month rolling average for the web searches. Plot the 6-month rolling average search data against the actual unemployment. What do you see in the chart? Which line moves first?
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH[0], df_unemployment.MONTH.max()])

# Calculate the rolling average over a 6 month window
roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()

ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, 'purple', linewidth=3, linestyle='-.')
ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

plt.show()


# Including 2020 in Unemployment Charts
df_ue_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)

plt.figure(figsize=(14, 8), dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])

ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=3)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

plt.show()
