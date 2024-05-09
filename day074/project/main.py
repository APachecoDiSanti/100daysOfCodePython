# Import statements
import pandas as pd
import matplotlib.pyplot as plt

# Challenge: How many different colours does the LEGO company produce? Read the colors.csv file in the data folder and find the total number of unique colours. Try using the .nunique() method to accomplish this.
colors = pd.read_csv('data/colors.csv')
colors.head()

colors.shape

colors['rgb'].nunique()

# Challenge: Find the number of transparent colours where is_trans == 't' versus the number of opaque colours where is_trans == 'f'. See if you can accomplish this in two different ways.
colors[(colors['is_trans'] == 't')].count()

colors['is_trans'].value_counts()

# Challenge: Read the sets.csv data and take a look at the first and last couple of rows.
sets = pd.read_csv('data/sets.csv')
sets.head()

sets.tail()

# Challenge: In which year were the first LEGO sets released and what were these sets called?
min_year = sets['year'].idxmin()
sets[sets['year'] == sets['year'][min_year]]


# Challenge: How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?
sets.groupby('year').count()

# Challenge: Find the top 5 LEGO sets with the most number of parts.
sets.sort_values('num_parts', ascending=False).head()

# Challenge: Use .groupby() and .count() to show the number of LEGO sets released year-on-year. How do the number of sets released in 1955 compare to the number of sets released in 2019?
sets_by_year = sets.groupby('year').count()['set_num']
sets_by_year[1955]
sets_by_year[2019]


# Challenge: Show the number of LEGO releases on a line chart using Matplotlib.
plt.plot(sets_by_year[:-2])

# Let's work out the number of different themes shipped by year. This means we have to count the number of unique theme_ids per calendar year.
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})


# Challenge: Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 2020 and 2021).
plt.plot(themes_by_year[:-2])

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year[:-2], color='g')
ax2.plot(themes_by_year[:-2])

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')


# Challenge: Use the .groupby() and .agg() function together to figure out the average number of parts per set. How many parts did the average LEGO set released in 1954 compared to say, 2017?
avg_parts_by_year = sets.groupby('year').agg({'num_parts': pd.Series.mean})
avg_parts_by_year['num_parts'][1954]
avg_parts_by_year['num_parts'][2017]


# Challenge: Has the size and complexity of LEGO sets increased over time based on the number of parts? Plot the average number of parts over time using a Matplotlib scatter plot. See if you can use the scatter plot documentation before I show you the solution. Do you spot a trend in the chart?
plt.scatter(x=avg_parts_by_year.index[:-2], y=avg_parts_by_year[:-2])

# LEGO has licensed many hit franchises from Harry Potter to Marvel Super Heros to many others. But which theme has the largest number of individual sets?
sets_per_theme = sets['theme_id'].value_counts()
theme_id_max_sets = sets_per_theme[sets_per_theme.idxmax()]

# Challenge: Explore the themes.csv. How is it structured? Search for the name 'Star Wars'. How many ids correspond to this name in the themes.csv? Now use these ids and find the corresponding the sets in the sets.csv (Hint: you'll need to look for matches in the theme_id column)
themes = pd.read_csv('data/themes.csv')
themes.head()

star_wars_themes = themes[(themes['name'] == 'Star Wars')]
star_wars_themes_ids = star_wars_themes['id']

sets[sets['theme_id'].isin(star_wars_themes_ids)]

sets[sets['theme_id'].isin(star_wars_themes_ids)].groupby('theme_id').count()


# Merging (i.e., Combining) DataFrames based on a Key
set_theme_count = sets['theme_id'].value_counts()
set_theme_count = pd.DataFrame({
    'id': set_theme_count.index,
    'set_count': set_theme_count.values
})
set_theme_count.head()

merged_df = pd.merge(set_theme_count, themes, on='id')
merged_df.head()

plt.bar(merged_df['name'][:10], merged_df['set_count'][:10])

plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df['name'][:10], merged_df['set_count'][:10])
