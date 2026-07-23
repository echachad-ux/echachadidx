import pandas as pd

sold = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSSold3.csv")
listing = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSListing3.csv")

# Sold Analysis

# Convert date fields to datetime format

ColumnsToDateTime = ["CloseDate", "PurchaseContractDate", "ListingContractDate", "ContractStatusChangeDate"]

for column in ColumnsToDateTime:
    sold[column] = pd.to_datetime(sold[column])

# Remove columns over 80% null

# Print null percent for all columns
sold_null_percent = sold.isnull().mean()
print("Sold Percent of null values per columns")
print(sold_null_percent * 100)

#  Identify columns with 80% or more null values
sold_columns_80 = sold_null_percent[sold_null_percent >= 0.8].index

print("Sold Columns with 80%+ missing values")
print(sold_columns_80)

# Remove columns
lenbefore80 = len(sold.columns)
print(lenbefore80,"columns before removing 80% null Sold columns")

# Remove columns with 90% or higher null
sold = sold.drop(columns=sold_columns_80)
lenafter80 = len(sold.columns)
print(lenafter80,"columns after removing 80% null Sold columns")

# Remove additional columns

# Columns for sure to remove:
# +BuyerAgencyCompensationType, +OriginatingSystemSubName, OriginatingSystemName, HighSchoolDistrict, +HighSchool, +MiddleOrJuniorSchool, ListingId
# StreetNumberNumeric, SubdivisionName,+ElementarySchool, MlsStatus, BuyerAgentMlsId, 


ColumnsToRemove = ["HighSchoolDistrict", "ListingId", "StreetNumberNumeric", "SubdivisionName", "MlsStatus", "BuyerAgentMlsId"]

LenBeforeDrop = len(sold.columns)
print(LenBeforeDrop,"columns before removing additional Sold columns")

sold = sold.drop(columns=ColumnsToRemove)

LenAfterDrop = (len(sold.columns))
print(LenAfterDrop,"columns after removing additional Sold columns")

# Change columns to numeric

ColumnsToNumeric = ["OriginalListPrice", "Latitude","Longitude", "LivingArea", "ParkingTotal", "LotSizeAcres", "YearBuilt",
                    "BathroomsTotalInteger", "Stories", "LotSizeArea", "MainLevelBedrooms", "GarageSpaces", "AssociationFee", "LotSizeSquareFeet"]

for column in ColumnsToNumeric:
    sold[column] = pd.to_numeric(sold[column], errors="coerce")

# Remove invalid numeric values

# Ask team: should I also remove these rows if the values are just null?

print(len(sold))

sold = sold[sold["ClosePrice"] > 0]
sold = sold[sold["LivingArea"] > 0]
sold = sold[sold["DaysOnMarket"] > 0]
sold = sold[sold["MainLevelBedrooms"] >= 0]
sold = sold[sold["BathroomsTotalInteger"] >= 0]


print(len(sold))

# Create flags for inconsistent timelines

sold["listing_after_close_flag"] = (sold["ListingContractDate"] > sold["PurchaseContractDate"])
sold["purchase_after_close_flag"] = (sold["PurchaseContractDate"] > sold["CloseDate"])
sold["negative_timeline_flag"] = (sold["listing_after_close_flag"] | sold["purchase_after_close_flag"])

# Geographic data checks

sold["missing_latitude_flag"] = sold["Latitude"].isna()
sold["missing_longitude_flag"] = sold["Longitude"].isna()

sold["null_longitude_latitude_flag"] = ((sold["Latitude"] == 0) 
                                        | (sold["Longitude"] == 0))
sold["longitude_error_flag"] = sold["Longitude"] > 0



















# Listing Analysis

# Convert date fields to datetime format

ColumnsToDateTime = ["CloseDate", "PurchaseContractDate", "ListingContractDate", "ContractStatusChangeDate"]

for column in ColumnsToDateTime:
    listing[column] = pd.to_datetime(listing[column])

# Remove columns over 80% null

# Print null percent for all columns
listing_null_percent = listing.isnull().mean()
print("Listing Percent of null values per columns")
print(listing_null_percent * 100)

#  Identify columns with 80% or more null values
listing_columns_80 = listing_null_percent[listing_null_percent >= 0.8].index

print("Listing Columns with 80%+ missing values")
print(listing_columns_80)

# Remove columns
lenbefore80 = len(listing.columns)
print(lenbefore80,"columns before removing 80% null Listing columns")

# Remove columns with 90% or higher null
Listing = listing.drop(columns=listing_columns_80)
lenafter80 = len(listing.columns)
print(lenafter80,"columns after removing 80% null Listing columns")

# Remove additional columns

# Columns for sure to remove:
# BuyerAgencyCompensationType, HighSchoolDistrict, HighSchool, MiddleOrJuniorSchool, ListingId
# StreetNumberNumeric, SubdivisionName,ElementarySchool, BuyerAgentMlsId, 


ColumnsToRemove = ["BuyerAgencyCompensationType", "HighSchoolDistrict", "HighSchool", "MiddleOrJuniorSchool",
                   "ListingId", "StreetNumberNumeric", "SubdivisionName", "ElementarySchool", "BuyerAgentMlsId",
                   "PropertyType.1", "DaysOnMarket.1", "LivingArea.1", "Longitude.1", "Latitude.1", "ListPrice.1",
                   "ListAgentFirstName.1", "ListAgentLastName.1", "CloseDate.1", "BuyerOfficeName.1", "UnparsedAddress.1"]

LenBeforeDrop = len(listing.columns)
print(LenBeforeDrop,"columns before removing additional Listing columns")

listing = listing.drop(columns=ColumnsToRemove)

LenAfterDrop = (len(listing.columns))
print(LenAfterDrop,"columns after removing additional Listing columns")

# Change columns to numeric

ColumnsToNumeric = ["OriginalListPrice", "Latitude","Longitude", "LivingArea", "ParkingTotal", "LotSizeAcres", "YearBuilt",
                    "BathroomsTotalInteger", "Stories", "LotSizeArea", "MainLevelBedrooms", "GarageSpaces", "AssociationFee", "LotSizeSquareFeet"]

for column in ColumnsToNumeric:
    listing[column] = pd.to_numeric(listing[column], errors="coerce")

# Remove invalid numeric values

# Ask team: should I also remove these rows if the values are just null?

print(len(listing))

listing1 = listing[listing["ClosePrice"] > 0]
listing2 = listing1[listing1["LivingArea"] > 0]
listing3 = listing2[listing2["DaysOnMarket"] > 0]
listing4 = listing3[listing3["MainLevelBedrooms"] >= 0]
listing5 = listing4[listing4["BathroomsTotalInteger"] >= 0]
listing = listing5

print(len(listing))

# Create flags for inconsistent timelines

listing["listing_after_close_flag"] = (listing["ListingContractDate"] > listing["PurchaseContractDate"])
listing["purchase_after_close_flag"] = (listing["PurchaseContractDate"] > listing["CloseDate"])
listing["negative_timeline_flag"] = (listing["listing_after_close_flag"] | listing["purchase_after_close_flag"])


# Geographic data checks

listing["missing_latitude_flag"] = listing["Latitude"].isna()
listing["missing_longitude_flag"] = listing["Longitude"].isna()

listing["null_longitude_latitude_flag"] = ((listing["Latitude"] == 0) 
                                        | (listing["Longitude"] == 0))
listing["longitude_error_flag"] = listing["Longitude"] > 0









# Import as CSVs

clean_sold = sold.copy()
clean_listing = listing.copy()

clean_sold.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSSold5.csv', index=False)
clean_listing.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSListing5.csv', index=False)