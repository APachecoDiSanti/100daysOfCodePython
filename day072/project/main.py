import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
df.head()

df.shape

df.columns

df.isna()

clean_df = df.dropna()
clean_df.tail()

highest_starting_median_salary = clean_df['Starting Median Salary'].idxmax()

clean_df['Undergraduate Major'].loc[highest_starting_median_salary]

clean_df.loc[highest_starting_median_salary]

# What college major has the highest mid-career salary?
# How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
highest_mid_career_salary = clean_df['Mid-Career Median Salary'].idxmax()
clean_df.loc[highest_mid_career_salary]

# Which college major has the lowest starting salary and how much do graduates earn after university?
lowest_starting_salary = clean_df['Starting Median Salary'].idxmin()
clean_df.loc[lowest_starting_salary]

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
lowest_mid_career_salary = clean_df['Mid-Career Median Salary'].idxmin()
clean_df.loc[lowest_mid_career_salary]

# Low risk careers
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

# Find the top 5 degrees with the highest values in the 90th percentile.
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

# the degrees with the greatest spread in salaries
highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

clean_df.groupby('Group').count()

# Remove Undergraduate Major column
pd.options.display.float_format = '{:,.2f}'.format
clean_df.loc[:, clean_df.columns!='Undergraduate Major'].groupby('Group').mean()
