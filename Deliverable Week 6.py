import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt


sold = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSSold5.csv")
gdf = gpd.read_file("/Users/eshaanchachad/Desktop/IDXExchange/DistrictAreas2526_-284845464123469011.geojson")

# Fix field types to date_time
sold["PurchaseContractDate"] = pd.to_datetime(sold["PurchaseContractDate"])
sold["ListingContractDate"] = pd.to_datetime(sold["ListingContractDate"])
sold["CloseDate"] = pd.to_datetime(sold["CloseDate"])

# Create Key Metrics

sold["PriceRatio"] = sold["ClosePrice"] / sold["OriginalListPrice"]
sold["PricePerSqFt"] = sold["ClosePrice"] / sold["LivingArea"]
sold["YrMo"] = sold["CloseDate"].dt.to_period("M")
sold["CloseToOriginalListRatio"] = sold["ClosePrice"] / sold["OriginalListPrice"]
sold["ListingToContractDays"] = sold["PurchaseContractDate"] - sold["ListingContractDate"]
sold["ContractToCloseDays"] = sold["CloseDate"] - sold["PurchaseContractDate"]

# Import and format new district names (sold)

gdf = gdf[gdf["DistrictType"] == "Unified"]

sold["Longitude"] = pd.to_numeric(sold["Longitude"], errors="coerce")
sold["Latitude"] = pd.to_numeric(sold["Latitude"], errors="coerce")

enrichedsold = gpd.GeoDataFrame(
    sold,
    geometry=gpd.points_from_xy(
        sold["Longitude"],
        sold["Latitude"]
    ),
    crs = "EPSG:4326"
)

enrichedsold = enrichedsold.to_crs("EPSG:3857")

print(enrichedsold.crs)
print(gdf.crs)

districts = gdf[["DistrictName", "geometry"]]

joinedsold = gpd.sjoin(
    enrichedsold,
    districts,
    how="left",
    predicate="within"
)

soldmain = joinedsold.copy()













listing = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSListing5.csv")

# Fix field types to date_time
listing["PurchaseContractDate"] = pd.to_datetime(listing["PurchaseContractDate"])
listing["ListingContractDate"] = pd.to_datetime(listing["ListingContractDate"])
listing["CloseDate"] = pd.to_datetime(listing["CloseDate"])

# Create Key Metrics
listing["PriceRatio"] = listing["ClosePrice"] / listing["OriginalListPrice"]
listing["PricePerSqFt"] = listing["ClosePrice"] / listing["LivingArea"]
listing["YrMo"] = listing["CloseDate"].dt.to_period("M")
listing["CloseToOriginalListRatio"] = listing["ClosePrice"] / listing["OriginalListPrice"]
listing["ListingToContractDays"] = listing["PurchaseContractDate"] - listing["ListingContractDate"]
listing["ContractToCloseDays"] = listing["CloseDate"] - listing["PurchaseContractDate"]

# Import and format new district names (sold)

listing["Longitude"] = pd.to_numeric(listing["Longitude"], errors="coerce")
listing["Latitude"] = pd.to_numeric(listing["Latitude"], errors="coerce")

enrichedlisting = gpd.GeoDataFrame(
    listing,
    geometry=gpd.points_from_xy(
        listing["Longitude"],
        listing["Latitude"]
    ),
    crs = "EPSG:4326"
)

enrichedlisting = enrichedlisting.to_crs("EPSG:3857")

print(enrichedlisting.crs)
print(gdf.crs)

joinedlisting = gpd.sjoin(
    enrichedlisting,
    districts,
    how="left",
    predicate="within"
)

listingmain = joinedlisting.copy()

print(joinedsold.head())
print(listingmain.head())

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

print(summary(sold, "PropertyType"))

soldmain.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSSold6.csv', index=False)
listingmain.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSListing6.csv', index=False)
