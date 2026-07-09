import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSVs
sold = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSSold.csv")
listing = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSListing.csv")



# Create environments

# Create an environment for numeric distribution summaries

def summary(df, column):
    summary = df[column].describe()
    return summary

# Environment to create a histogram

def histogram(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    df = df[df[column].between(lower_bound, upper_bound)]

    plt.hist(df[column], bins = 20, edgecolor = "black")
    plt.title("Distribution of " + column)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

    # Environment to create a boxplot

# Environment to create a boxplot

def boxplot(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    df = df[df[column].between(lower_bound, upper_bound)]

    plt.boxplot(df[column])
    plt.title("Distribution of " + column)
    plt.ylabel(column)
    plt.show()

# Environment to identify extreme outliers

def extreme_outliers(df, column):
    EEQ1 = df[column].quantile(0.25)
    EEQ3 = df[column].quantile(0.75)
    EEIQR = EEQ3 - EEQ1
    
    ee_lower_bound = EEQ1 - (3 * EEIQR)
    ee_upper_bound = EEQ3 + (3 * EEIQR)

    extreme_data = df[
        (df[column] < ee_lower_bound) | 
        (df[column] > ee_upper_bound)
    ]

    extreme_outliers = extreme_data[column]
    return(extreme_outliers)





# Sold analysis

# Dataset understanding

# Identify number of rows and columns
rows = len(sold)
columns = len(sold.columns)

print(rows,"rows in Sold")
print(columns,"columnsin Sold")

# Identify column data types
print("Sold Data Types")
print(sold.dtypes)

# Print null percent for all columns
sold_null_percent = sold.isnull().mean()
print("Sold Percent of null values per columns")
print(sold_null_percent * 100)

#  Identify columns with 90% or more null values
sold_columns_90 = sold_null_percent[sold_null_percent >= 0.9].index

print("Sold Columns with 90%+ missing values")
print(sold_columns_90)

# Remove columns

# Remove columns with 90% or higher null
sold = sold.drop(columns=sold_columns_90)
lenafter90 = len(sold.columns)
print(lenafter90,"columns after removing 90% null Sold columns")

# Numeric distribution summaries for columns

print("Sold Numeric Distribution Summary for ClosePrice:")
print(summary(sold,"ClosePrice"))

print("Sold Numeric Distribution Summary for LivingArea:")
print(summary(sold,"LivingArea"))

print("Sold Numeric Distribution Summary for DaysOnMarket:")
print(summary(sold,"DaysOnMarket"))








# Listing analysis

# Dataset understanding

# Identify number of rows and columns
rows = len(listing)
columns = len(listing.columns)

print(rows,"rows in Listing")
print(columns,"columns in Listing")

# Identify column data types
print("Listing Data Types")
print(listing.dtypes)

# Print null percent for all columns
listing_null_percent = listing.isnull().mean()
print("Listing Percent of null values per columns")
print(listing_null_percent * 100)

#  Identify columns with 90% or more null values
listing_columns_90 = listing_null_percent[listing_null_percent >= 0.9].index

print("Listing Columns with 90%+ missing values")
print(listing_columns_90)

# Remove columns

# Remove columns with 90% or higher null
listing = listing.drop(columns=listing_columns_90)
lenafter90 = len(listing.columns)
print(lenafter90,"columns after removing 90% null Listing columns")

# Numeric distribution summaries for columns

print("Listing Numeric Distribution Summary for ClosePrice:")
print(summary(listing,"ClosePrice"))

print("Listing Numeric Distribution Summary for LivingArea:")
print(summary(listing,"LivingArea"))

print("Listing Numeric Distribution Summary for DaysOnMarket:")
print(summary(listing,"DaysOnMarket"))

soldmain = sold.copy()
listingmain = listing.copy()

soldmain.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSSold2.csv', index=False)
listingmain.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSListing2.csv', index=False)
