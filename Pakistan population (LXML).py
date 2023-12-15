#!/usr/bin/env python
# coding: utf-8

# # Pakistan Population 

# #### In this Case we cover  a pakistan population. How much  pakistan population increase yearly.

# - The current population of Pakistan is 242,305,779 as of Monday, November 20, 2023, based on Worldometer elaboration of the . . - latest United Nations data 1.
# - Pakistan 2023 population is estimated at 240,485,658 people at mid year.
# - Pakistan population is equivalent to 2.99% of the total world population.
# - Pakistan ranks number 5 in the list of countries (and dependencies) by population.
# - The population density in Pakistan is 312 per Km2 (808 people per mi2).
# - The total land area is 770,880 Km2 (297,638 sq. miles)
# - 34.7 % of the population is urban (83,500,516 people in 2023)
# - The median age in Pakistan is 20.6 years.

# ##### we discuss the some  topics 

# - **Yearly Population Growth Rate**
# - **Population of Pakistan (2023 and historical)**
# - **Pakistan Population Forecast**
# - **Main Cities by Population in Pakistan**

# .

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from lxml import etree


# In[3]:


url = 'https://www.worldometers.info/world-population/pakistan-population/'

response = requests.get(url)
content = response.content 

# parse the HTML content using LXML

tree= etree.HTML(content)

# get all tables from the website

tables = tree.xpath('//table')

# print each table as a string 
for table in tables:
    print(etree.tostring(table, pretty_print=True))


# In[4]:


def clean_HTML_table(html_table):
    # parse HTML table into on etree object
    
    tree= etree.HTML(html_table)
    
    # extract table data into a pandas DataFrame
    
    df= pd.DataFrame(columns=[])
    
    for row in tree.xpath('//tr'):
        data =[]
        for cell in row.xpath('//td'):
            data.append(cell.text)
        df.loc[len(df)] = data
        
        # convert the datafram to plain text
        
        text = df.to_string(index=False)
        
        return text.strip()
    
    def scrape_website(url):
        respose = requests.get(url)
        content = response.content
        
        # parse the html content using lxml
        
        tree = etree.HTML(content)
        
        # Get all tables from the website
        
        tables = tree.xpath('//table')
        
        # Clean and print each table as plane text 
        
        for table in tables:
            clean_tables_text = clean_html_table(etree.tostring(table, encoding= 'unicode'))
            print (clean_table_text)
            
    # Example usage 
    url = "https://www.worldometers.info/world-population/pakistan-population/"
    scrape_website(url)


# In[5]:


print(table)


# In[6]:


def clean_html_table(html_table):
    try:
        # Parse the HTML table into an etree object
        tree = etree.HTML(html_table)

        # Extract table data into a pandas DataFrame
        df = pd.DataFrame(columns=[])
        for row in tree.xpath('//tr'):
            data = []
            for cell in row.xpath('//td'):
                data.append(cell.text)
            df.loc[len(df)] = data

        # Convert the DataFrame to plain text
        text = df.to_string(index=False)

        return text.strip()
    except Exception as e:
        print(f"Error cleaning table: {e}")
        return None

def scrape_website(url):
    try:
        response = requests.get(url)
        content = response.content

        # Parse the HTML content using lxml
        tree = etree.HTML(content)

        # Get all tables from the website
        tables = tree.xpath('//table')

        # Clean and print each table as plain text
        for table in tables:
            clean_table_text = clean_html_table(etree.tostring(table, encoding='unicode'))
            print(clean_table_text)
    except Exception as e:
        print(f"Error scraping website: {e}")

# Example usage
url = "https://www.worldometers.info/world-population/pakistan-population/"
scrape_website(url)


# In[7]:


def clean_html_table(html_table):
    try:
        # Parse the HTML table into an etree object
        tree = etree.HTML(html_table)

        # Extract table data into a list of lists
        data = []
        for row in tree.xpath('//tr'):
            row_data = []
            for cell in row.xpath('//td'):
                row_data.append(cell.text)
            data.append(row_data)

        # Check if the data is empty
        if not data:
            return None

        # Create a pandas DataFrame from the data
        df = pd.DataFrame(data)

        # Convert the DataFrame to plain text
        text = df.to_string(index=False)

        return text.strip()
    except Exception as e:
        print(f"Error cleaning table: {e}")
        return None

def scrape_website(url):
    try:
        response = requests.get(url)
        content = response.content

        # Parse the HTML content using lxml
        tree = etree.HTML(content)

        # Get all tables from the website
        tables = tree.xpath('//table')

        # Clean and print each table as plain text
        for table in tables:
            clean_table_text = clean_html_table(etree.tostring(table, encoding='unicode'))
            print(clean_table_text)
    except Exception as e:
        print(f"Error scraping website: {e}")

# Example usage
url = "https://www.worldometers.info/world-population/pakistan-population/"
scrape_website(url)


# In[8]:


# Replace the placeholder URL with the actual URL of the webpage you want to scrape
url = "https://www.worldometers.info/world-population/pakistan-population/"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    html_content = response.content.decode("utf-8")
    
    # Create a Pandas DataFrame from the HTML content
    df = pd.read_html(html_content)[0]
    
    # Print the DataFrame in table format
    print(df)
else:
    print("Error scraping webpage:", response.status_code)


# In[9]:


url = "https://www.worldometers.info/world-population/pakistan-population/"

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content.decode("utf-8")

    # Extract all tables using Pandas read_html()
    tables = pd.read_html(html_content)

    # Iterate over each table and convert it to plain text
    for table in tables:
        print(table.to_string(index=False))
else:
    print("Error scraping webpage:", response.status_code)


# In[10]:


url = "https://www.worldometers.info/world-population/pakistan-population/"

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content.decode("utf-8")

    # Extract all tables using Pandas read_html()
    tables = pd.read_html(html_content)

    # Create a dictionary to store tables with descriptive names
    table_dict = {}
    table_dict['Pakistan Population (1950 - 2023)'] = tables[0]
    table1= table_dict['Yearly Population Growth Rate (%)'] = tables[1]
    table2= table_dict[' Year  Population Yearly '] = tables[2]
    table3= table_dict[' CITY NAME  POPULATION '] = tables[3]

    # Iterate over the dictionary and print each table
    for table_name, table in table_dict.items():
        print(f'\nTable: {table_name}\n')
        print(table.to_string(index=False))
else:
    print("Error scraping webpage:", response.status_code)


# In[11]:


table1


# In[12]:


table2


# In[13]:


table3


# In[14]:


table1


# In[15]:


table1.shape


# In[16]:


table1.info()


# In[17]:


table1.size


# In[18]:


('diminsion:',table1.ndim)


# In[19]:


('Data type:', table1.dtypes)


# In[20]:


table1.columns


# In[21]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
table1.describe()


# In[22]:


table1[["Year" , "Population" , "Migrants (net)" , "Urban Population" , "World Population"]]


# In[23]:


#import matplotlib.pyplot as plt
#import pandas as pd

# Assuming 'table1' is a pandas DataFrame containing the data
data_dict = {
    "Year": [2023, 2022, 2020, 2015, 2010],
    "Population": [240485658, 235824862, 227196741, 210969298, 194454498],
    "Migrants (net)": [-165988, -165988, -588736, -2172159, -431891],
    "Urban Population": [83500516, 81432849, 77437729, 68226783, 59691513],
    "World Population": [8045311447, 7975105156, 7840952880, 7426597537, 6985603105]
}

df = pd.DataFrame(data_dict)

# Create a bar plot with customized style
plt.figure(figsize=(12, 6))
bar_width = 0.35  # Adjust bar width for better spacing
index = range(len(df['Year']))  # Create index for bar positions

plt.bar(index, df['Population'], bar_width, label='Population', color='skyblue', alpha=0.7)
plt.bar([i + bar_width for i in index], df['Urban Population'], bar_width, label='Urban Population', color='gold', alpha=0.7)
plt.bar([i + 2 * bar_width for i in index], df['Migrants (net)'], bar_width, label='Migrants (net)', color='red', alpha=0.7)

plt.xlabel('Year', fontsize=14, weight='bold')
plt.ylabel('Count', fontsize=14, weight='bold')
plt.title('Population Trends (2010-2023)', fontsize=16, weight='bold')
plt.xticks([i + bar_width / 2 for i in index], df['Year'], fontsize=12)  # Adjust tick positions

plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust margins and add padding for labels
plt.tight_layout(pad=2)

plt.show()


# In[24]:


df = table1
df.plot(kind = "bar", x= "Year" , y= ["Population","Urban Population","Migrants (net)"])
sns.set(rc={'figure.figsize':(8,5)})
plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('Pakistan population 1955 TO 2023')
plt.show()


# In[25]:


df = table1

df.plot(kind = "box", x= "Year" , y= ["Population","Urban Population","Migrants (net)"])
plt.title('Pakistan population 1955 TO 2023')
plt.show()


# In[26]:


df = table1

df.plot(kind = "line", x= "Year" , y= ["Population","Urban Population","Migrants (net)"])
plt.title('Pakistan population 1955 TO 2023')
plt.show()


# In[27]:


table2


# In[28]:


table2.shape


# In[29]:


table2.ndim


# In[30]:


table2.describe()


# In[31]:


table2.columns


# In[32]:


table2.info()


# In[33]:


table2.dtypes


# In[34]:


table2.dropna(inplace=True)


# In[35]:


table2


# In[36]:


table2[['Year','Migrants (net)','Median Age','Urban Population','World Population']]


# In[37]:


df= table2

df.plot(kind='line', x='Year', y= ['Migrants (net)','Median Age','Urban Population','World Population'])
plt.title('Pakistan population estemate 2025 To 2045')
plt.show()


# In[38]:


df= table2

df.plot(kind='bar', x='Year', y= ['Migrants (net)','Median Age','Urban Population','World Population'])
sns.set(rc={'figure.figsize':(8,8)})
plt.title('Pakistan population estemate 2025 To 2045')
plt.show()


# In[39]:


df= table2

df.plot(kind='box', x='Year', y= ['Migrants (net)','Median Age','Urban Population','World Population'])
plt.title('Pakistan population estemate 2025 To 2045')
plt.show()


# In[40]:


df = pd.DataFrame(table2)

# Create a bar plot with customized style
plt.figure(figsize=(12, 6))
bar_width = 0.35  # Adjust bar width for better spacing
index = range(len(df['Year']))  # Create index for bar positions

plt.bar(index, df['Population'], bar_width, label='Population', color='blue', alpha=0.7)
plt.bar([i + bar_width for i in index], df['Urban Population'], bar_width, label='Urban Population', color='green', alpha=0.7)
plt.bar([i + 2 * bar_width for i in index], df['Migrants (net)'], bar_width, label='Migrants (net)', color='red', alpha=0.7)
plt.bar(index, df['World Population'], bar_width, label='World Population', color='gold', alpha=0.7)

plt.xlabel('Year', fontsize=14, weight='bold')
plt.ylabel('Count', fontsize=14, weight='bold')
plt.title('Population Trends (2025-2045)', fontsize=16, weight='bold')
plt.xticks([i + bar_width / 2 for i in index], df['Year'], fontsize=12)  # Adjust tick positions

plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust margins and add padding for labels
plt.tight_layout(pad=2)

plt.show()


# In[41]:


table3


# In[42]:


table3.shape


# In[43]:


table3.size


# In[44]:


table3.dtypes


# In[45]:


table3.describe()


# In[46]:


table3.info()


# In[47]:


table3.head(10)


# In[48]:


table3.tail(10)


# In[49]:


df= table3

df.plot(kind='bar', x='CITY NAME',  y ='POPULATION')
sns.set(rc={'figure.figsize':(15,8)})
plt.title('Pakistan population estemate City wise')
plt.show()


# In[50]:


df= table3

df.plot(kind='line', x='CITY NAME',  y ='POPULATION')
plt.title('Pakistan population estemate City wise')
plt.show()


# In[51]:


ax = sns.barplot(data = df, x = 'POPULATION', hue='POPULATION', y = 'CITY NAME')

sns.set(rc={'figure.figsize':(20,20)})

plt.title(' city wise population of Pakistan')

for bars in ax.containers:
    ax.bar_label(bars)


# In[52]:


df= table3
df.plot(kind= 'hist' , x="CITY NAME",y="POPULATION")
sns.set(rc={'figure.figsize':(8,8)})
plt.show()


# In[53]:


#import matplotlib.pyplot as plt

# Set the data values
world_population = 8045311447
pakistan_population = 240485658

# Calculate the percentage of Pakistan population in world population
pakistan_population_percentage = (pakistan_population / world_population) * 100

# Create the pie chart
plt.figure(figsize=(5, 5))
labels = ['World Population', 'Pakistan Population']
sizes = [world_population, pakistan_population]
colors = ['skyblue', 'green']  # Assign colors to the slices
explode = (0.1, 0)  # Explode the Pakistan population slice for emphasis

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140, shadow=True, colors=colors)
plt.title('World Population vs. Pakistan Population (2023)')

# Add a legend
plt.legend(labels, loc='upper right')

plt.axis('equal')  # Equal aspect ratio ensures a circular pie chart

plt.show()



# In[54]:


# import matplotlib.pyplot as plt
# import pandas as pd

# Create a list of the largest cities in Pakistan and their populations
cities = ['Karachi', 'Lahore', 'Faisalabad', 'Rawalpindi', 'Gujranwala']
populations = [16055235, 11126800, 3890000, 3510212, 2960160]

# Create a DataFrame from the data
data = pd.DataFrame({'City': cities, 'Population': populations})

# Calculate the total population of the cities
total_population = data['Population'].sum()

# Calculate the percentage of each city's population in the total population
data['Percentage'] = (data['Population'] / total_population) * 100

# Create a pie chart using Matplotlib
plt.figure(figsize=(10, 6))
plt.pie(data['Percentage'], labels=data['City'], autopct='%1.1f%%', startangle=140, shadow=True)
plt.title('Population of Pakistan\'s Largest Cities')

# Assign different colors to the city slices
colors = ['skyblue', 'gold', 'lightcoral', 'lightgreen', 'lightpink']


# Add a legend
plt.legend(data['City'], loc='upper left')

# Equal aspect ratio ensures a circular pie chart
plt.axis('equal')  

plt.show()


# ## Documentation on Pakistan Population Data November 2023
# 
# **1. Introduction**
# 
# This document provides an overview of the current population of Pakistan, based on data as of November 20, 2023, and sourced from Worldometer's elaboration of the latest United Nations data. It covers key statistics such as population size, growth rate, demographics, and density.
# 
# **2. Population Size:**
# 
# * **Current Population:** 242,305,779 (as of November 20, 2023)
# * **Estimated Mid-Year Population:** 240,485,658 (as of mid-year 2023)
# * **World Population Share:** 2.99% (as of 2023)
# * **Global Rank:** 5th (as of 2023)
# 
# **3. Population Growth:**
# 
# * **Estimated Yearly Increase:** 1,820,121 (calculated by subtracting mid-year 2023 population from November 2023 population)
# 
# **4. Demographics:**
# 
# * **Urban Population:** 34.7% (83,500,516 people in 2023)
# * **Rural Population:** 65.3% (158,805,263 people in 2023)
# * **Median Age:** 20.6 years
# 
# **5. Land Area and Density:**
# 
# * **Total Land Area:** 770,880 Km2 (297,638 sq. miles)
# * **Population Density:** 312 per Km2 (808 people per mi2)
# 
# **6. Data Sources:**
# 
# * Worldometer elaboration of the latest United Nations data
# 
# **7. Data Limitations:**
# 
# * The provided data is an estimate and may not reflect the exact population size.
# * The information does not include details about birth rates, death rates, or migration patterns.
# * The data may not be representative of all regions within Pakistan.
# 
# **8. Potential Uses of the Data:**
# 
# * This information can be used for research, policymaking, and development planning related to population growth, urbanization, and demographic trends in Pakistan.
# * The data can be used to inform studies on public health, education, and resource allocation.
# * The population statistics can be used for comparative analysis with other countries and regions.
# 
# **9. Additional Considerations:**
# 
# * It is important to acknowledge the dynamic nature of population data and to use the latest available information whenever possible.
# * A more comprehensive understanding of the population requires additional data on factors such as birth rates, death rates, and migration patterns.
# * Disaggregation of data by region, gender, and age can provide deeper insights into the population dynamics of Pakistan.
# 
# I hope this detailed documentation provides a valuable overview of the current population of Pakistan based on the provided data. Please let me know if you have any further questions or require additional information.
# 
# **Note:** This documentation can be further expanded by including:
# 
# * Visualizations of the data such as charts and graphs.
# * Links to additional resources about Pakistan's population.
# * Information about the methodology used to collect and estimate the data.
# * A discussion of the potential challenges and opportunities associated with Pakistan's population growth.
# 
# 

# #### Data Analysis and Data Visualization  by  **SAIFULLAH ALEEM**  (Python Programmer)
