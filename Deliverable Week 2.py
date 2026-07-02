import pandas as pd

# Import CSV
sold = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold.csv")
sold = sold[sold["PropertyType"] == "Residential"]

print("Sold Report")

nullcount = sold.isnull().sum()
print("Count of null values")
print(nullcount)

#Print column types
types = sold.dtypes
print("Column types")
print(types)

# Percentage of null columns
nullcolumns = sold.isnull().mean()*100
print("Percent of null values within columns:")
print(nullcolumns)

# Flag columns with null values over 90%
flaggedcols = sold.isnull().mean() >= 0.9
flags = sold.columns[flaggedcols]
print("Flagged columns (over 90% null):")
print(flags)

# Numeric distribution summaries
ClosePriceSummary = sold["ClosePrice"].describe()
LivingAreaSummary = sold["LivingArea"].describe()
DaysOnMarketSummary = sold["DaysOnMarket"].describe()
print("Close Price Numeric Distribution Summary:", ClosePriceSummary)
print("Living Area Numeric Distribution Summary:", LivingAreaSummary)
print("Days On Market Numeric Distribution Summary:", DaysOnMarketSummary)

# Create a copy
mainsold = sold.copy()

# Export as sold CSV
# mainsold.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold2.csv', index=False)

# Import CSV
listing = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing.csv")
listing = listing[listing["PropertyType"] == "Residential"]

# print("Listing Report")

nullcount = listing.isnull().sum()
print("Count of null values")
print(nullcount)

#Print column types
types = listing.dtypes
print("Column types")
print(types)

# Percentage of null columns
nullcolumns = listing.isnull().mean()*100
print("Percent of null values within columns:")
print(nullcolumns)

# Flag columns with null values over 90%
flaggedcols = listing.isnull().mean() >= 0.9
flags = listing.columns[flaggedcols]
print("Flagged columns (over 90% null):")
print(flags)

# Numeric distribution summaries
ClosePriceSummary = listing["ClosePrice"].describe()
LivingAreaSummary = listing["LivingArea"].describe()
DaysOnMarketSummary = listing["DaysOnMarket"].describe()
print("Close Price Numeric Distribution Summary:", ClosePriceSummary)
print("Living Area Numeric Distribution Summary:", LivingAreaSummary)
print("Days On Market Numeric Distribution Summary:", DaysOnMarketSummary)

# Create a copy
mainlisting = listing.copy()

# Export as listing CSV
# mainlisting.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing2.csv', index=False)



#Histograms:

import matplotlib.pyplot as plt

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

# Boxplot:

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


# boxplot(sold, "ClosePrice")

# Percentile summary

def percentile_sumamry(df, column):
    summary = df[column].describe()
    return summary

# print(percentile_sumamry(sold, "ClosePrice"))


# Extreme outliers

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

# print(extreme_outliers(listing, "ClosePrice"))