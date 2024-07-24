import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

data = pd.read_csv('cost_revenue_dirty.csv')



# Challenge: Answer these questions about the dataset:
# How many rows and columns does the dataset contain?
data.shape
# Are there any NaN values present?
data.isna().sum()
# Are there any duplicate rows?
data.duplicated().sum()
# What are the data types of the columns?
data.dtypes


# Challenge: Convert the USD_Production_Budget, USD_Worldwide_Gross, and USD_Domestic_Gross columns to a numeric format by removing $ signs and ,.
columns = ['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']
for col in columns:
  data[col] = data[col].replace('\$|,', '', regex=True)
  data[col] = pd.to_numeric(data[col])
data.dtypes


# Challenge: Convert the Release_Date column to a Pandas Datetime type.
# mm/dd/yyyy
data['Release_Date'] = pd.to_datetime(data['Release_Date'])
data.info()


# Challenge:
# What is the average production budget of the films in the data set?
desc = data.describe()
desc
print(desc['USD_Production_Budget']['mean'])

# What is the average worldwide gross revenue of films?
print(desc['USD_Worldwide_Gross']['mean'])

# What were the minimums for worldwide and domestic revenue?
print(desc['USD_Domestic_Gross']['min'])
print(desc['USD_Worldwide_Gross']['min'])

# Are the bottom 25% of films actually profitable or do they lose money?
gross = desc['USD_Worldwide_Gross']['25%'] + desc['USD_Domestic_Gross']['25%']
budget = desc['USD_Production_Budget']['25%']
print(f'budget: {budget}')
print(f'gross: {gross}')
print(gross > budget)

# What are the highest production budget and highest worldwide gross revenue of any film?
print(desc['USD_Production_Budget']['max'])
print(desc['USD_Worldwide_Gross']['max'])

# How much revenue did the lowest and highest budget films make?
lowest_budget = data[data['USD_Production_Budget'] == desc['USD_Production_Budget']['min']]
lowest_budget_gross = lowest_budget['USD_Worldwide_Gross'] + lowest_budget['USD_Domestic_Gross']
print(f'lowest_budget_gross: {lowest_budget_gross}')
highest_budget = data[data['USD_Production_Budget'] == desc['USD_Production_Budget']['max']]
highest_budget_gross = highest_budget['USD_Worldwide_Gross'] + highest_budget['USD_Domestic_Gross']
print(f'lowest_budget_gross: {highest_budget_gross}')


# Challenge How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that grossed nothing?
zero_domestic = data[data['USD_Domestic_Gross'] == 0]
len(zero_domestic)
zero_domestic.sort_values(by='USD_Production_Budget', ascending=False).head()

# Challenge: How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally?
zero_worldwide = data[data['USD_Worldwide_Gross'] == 0]
len(zero_worldwide)
zero_worldwide.sort_values(by='USD_Production_Budget', ascending=False).head()


# Challenge: Use the .query() function to accomplish the same thing. Create a subset for international releases that had some worldwide gross revenue, but made zero revenue in the United States.
data.query('USD_Worldwide_Gross > 0 and USD_Domestic_Gross == 0')

# Challenge:
# Identify which films were not released yet as of the time of data collection (May 1st, 2018).
scrape_date = pd.Timestamp('2018-5-1')
# How many films are included in the dataset that have not yet had a chance to be screened in the box office?
data.query('Release_Date > @scrape_date')
# Create another DataFrame called data_clean that does not include these films.
clean_data = data.query('Release_Date < @scrape_date')


# Challenge: What is the percentage of films where the production costs exceeded the worldwide gross revenue?
budget_over_gross = clean_data.query('USD_Production_Budget > USD_Worldwide_Gross')
(len(budget_over_gross)/len(clean_data))*100


#
sns.scatterplot(data=clean_data,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross')

plt.figure(figsize=(8, 4), dpi=200)
ax = sns.scatterplot(data=clean_data,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross')
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')
plt.show()


# Challenge: Try to create the following Bubble Chart:
plt.figure(figsize=(8, 4), dpi=200)
ax = sns.scatterplot(data=clean_data,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     hue='USD_Worldwide_Gross',  # colour
                     size='USD_Worldwide_Gross', )  # dot size
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions', )
plt.show()

plt.figure(figsize=(8, 4), dpi=200)

# set styling on a single chart
with sns.axes_style('darkgrid'):
    ax = sns.scatterplot(data=clean_data,
                         x='USD_Production_Budget',
                         y='USD_Worldwide_Gross',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross')
    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')

plt.figure(figsize=(8, 4), dpi=200)

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=clean_data,
                         x='Release_Date',
                         y='USD_Production_Budget',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross', )
    ax.set(ylim=(0, 450000000),
           xlim=(clean_data.Release_Date.min(), clean_data.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')


# Challenge: Create a column in data_clean that has the decade of the release.
dt_index = pd.DatetimeIndex(clean_data.Release_Date)
years = dt_index.year
decades = years//10*10
clean_data['Decade'] = decades

# Challenge: Create two new DataFrames: old_films and new_films
# old_films should include all the films before 1969 (up to and including 1969)
old_films = clean_data[clean_data.Decade <= 1960]
# new_films should include all the films from 1970 onwards
new_films = clean_data[clean_data.Decade > 1960]
# How many films were released prior to 1970?
len(old_films)
# What was the most expensive film made prior to 1970?
old_films.sort_values(by='USD_Production_Budget', ascending=False).head(1)



sns.regplot(data=old_films,
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
  sns.regplot(data=old_films,
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})


# Challenge: Use Seaborn's .regplot() to show the scatter plot and linear regression line against the new_films.
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style('darkgrid'):
    ax = sns.regplot(data=new_films,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     color='#2f4b7c',
                     scatter_kws={'alpha': 0.3},
                     line_kws={'color': '#ff7c43'})
    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')


regression = LinearRegression()
# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])
# Find the best-fit line
regression.fit(X, y)
# R-squared
regression.score(X, y)


# Challenge: Run a linear regression for the old_films. Calculate the intercept, slope and r-squared. How much of the variance in movie revenue does the linear model explain in this case?
X = pd.DataFrame(old_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])
regression.fit(X, y)
coef = regression.coef_[0]
intercept = regression.intercept_[0]
score = regression.score(X, y)
print(f'coef: {coef}, intercept: {intercept}, score: {score}')


# Challenge: How much global revenue does our model estimate for a film with a budget of $350 million?
budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')
