#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


# Load the CSV file into a pandas DataFrame
df = pd.read_csv("villagers.csv")

# Display the first few rows of the dataset to verify it was loaded correctly
df.head()


# In[4]:


import pandas as pd

# Load the CSV file directly from the URL
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Display the first few rows to verify it was loaded correctly
df.head()


# In[5]:


import pandas as pd

# Load the CSV file directly from the URL
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Get the number of rows and columns in the DataFrame
rows, columns = df.shape

# Print the shape
print(f"The dataset contains {rows} rows and {columns} columns.")


# In[6]:


import pandas as pd

# Load the CSV file directly from the URL
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print("First five rows of the dataset:")
print(df.head())


# In[7]:


# Get the number of rows and columns
rows, columns = df.shape
print(f"\nThe dataset contains {rows} rows and {columns} columns.")

# Display a summary of the dataset
print("\nSummary statistics for the dataset:")
print(df.describe(include='all'))


# In[8]:


# Check for missing data
missing_data = df.isnull().sum()

# Display columns with missing data
print("\nMissing data in each column:")
print(missing_data[missing_data > 0])


# In[9]:


# Display column names and data types
print("\nData types and columns:")
print(df.info())


# In[10]:


import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Briefly analyze the data
print("First five rows of the dataset:")
print(df.head())

# Structure and summary of the dataset
rows, columns = df.shape
print(f"\nThe dataset contains {rows} rows and {columns} columns.")

# Summary statistics
print("\nSummary statistics for the dataset:")
print(df.describe(include='all'))

# Missing data analysis
missing_data = df.isnull().sum()
print("\nMissing data in each column:")
print(missing_data[missing_data > 0])

# Information about data types
print("\nData types and columns:")
print(df.info())


# In[11]:


import pandas as pd

# Load the dataset from the URL
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Get the size (dimensions) of the dataset
rows, columns = df.shape

# Display the size of the dataset
print(f"The dataset contains {rows} rows and {columns} columns.")


# In[12]:


import pandas as pd

# Load the dataset from the URL
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Step 1: Delete the 'song' column (as an example) because it contains missing data
# Identify the columns with missing data first, then decide which one to delete
print("\nColumns with missing data before deletion:")
print(df.isnull().sum())

# Delete the 'song' column (which has missing values)
del df['song']

# Step 2: Drop rows with any remaining missing data
df_cleaned = df.dropna()

# Display the DataFrame after deletion and cleaning
print("\nColumns with missing data after 'song' deletion and dropping rows with missing data:")
print(df_cleaned.isnull().sum())

# Display the cleaned DataFrame's dimensions
print(f"\nThe cleaned dataset contains {df_cleaned.shape[0]} rows and {df_cleaned.shape[1]} columns.")


# In[13]:


import pandas as pd

# Load the dataset from the URL
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Option 1: Display the first 5 rows (default behavior)
print("First 5 rows of the dataset (default):")
print(df.head())

# Option 2: Display the first 10 rows (specifying the number of rows)
print("\nFirst 10 rows of the dataset:")
print(df.head(10))

# Option 3: Adjust pandas settings to display more rows (e.g., show 20 rows by default)
pd.set_option('display.max_rows', 20)

# Display the entire DataFrame or up to 20 rows based on the new setting
print("\nDataset display adjusted to show up to 20 rows:")
print(df)

# To reset pandas settings to default (if needed):
# pd.reset_option('display.max_rows')


# In my opinion, observation means to observe every specific data, and the observation value represents the sample data. Variables means characteristics and characteristics, which means that every sample will be almost different, and I think variables should be the focus of our data analysis.
# 
# I think df . shape display all data, whether it exists or not. df . describe() will show all data except missing data.
# 
# Count   Data values in each column without missing data
# Mean    The average of a column without missing data
# 
# Std is standard deviation, if placed in the axis, will have an average line, and then observe the convergence of nearby points to the average line, to judge the data
# 
# Min is minimum, which means the smallest in that column.
# Max is Maximum, which means the largest in that column
# 25% means the 25% data lower than this number
# 50% means the middle number in these data
# 75% means the 75% data lower than this number
# 
# 7.1 This is a good option when I need to delete an entire column, for example, if I want to delete all ages
# 
# 7.2 if I need to delete some useless rows, but need to keep some of the data in the column, such as when I need to delete other information about a person and keep only the age
# 
# 7.3 del df['col'] can help us delete a complete line and avoid the impact of missing data
# 
# 8.3 I think ChatGPT did not take into account the problem that my data had many lines in the process of helping me, until I found that my code running found very little missing data, I checked carefully and found that the code provided by chatGPT could only analyze the first few lines of code, I asked it to modify this error again

# [Chat with GPT](https://chatgpt.com/share/0bcaafd2-f46d-4d42-80ab-e643af2701e0)
# 

# # My Notes - Analysis of Dataset
# 
# You can view the chat and analysis in the conversation at the following link:
# 
# [Chat with GPT](https://chatgpt.com/share/0bcaafd2-f46d-4d42-80ab-e643af2701e0)
# 

# 9. yes, I read the textbook and go the every lecture and tut.

# In[ ]:




