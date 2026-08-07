import pandas as pd

sold = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSSold6.csv")
listing = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSListing6.csv")

# Columns to create flags for: ClosePrice, LivingArea, DaysOnMarket




# Sold Flag for ClosePrice

SoldClosePriceQ1 = sold["ClosePrice"].quantile(0.25)
SoldClosePriceQ3 = sold["ClosePrice"].quantile(0.75)
SoldClosePriceIQR = SoldClosePriceQ3 - SoldClosePriceQ1
SoldClosePriceUpper = SoldClosePriceQ3 + 1.5 * SoldClosePriceIQR
SoldClosePriceLower = SoldClosePriceQ1 - 1.5 * SoldClosePriceIQR

sold["ClosePrice_Outlier_Flag"] = (
    (sold["ClosePrice"] > SoldClosePriceUpper) | 
    (sold["ClosePrice"] < SoldClosePriceLower)
)

# Sold Flag for LivingArea

SoldLivingAreaQ1 = sold["LivingArea"].quantile(0.25)
SoldLivingAreaQ3 = sold["LivingArea"].quantile(0.75)
SoldLivingAreaIQR = SoldLivingAreaQ3 - SoldLivingAreaQ1
SoldLivingAreaUpper = SoldLivingAreaQ3 + 1.5 * SoldLivingAreaIQR
SoldLivingAreaLower = SoldLivingAreaQ1 - 1.5 * SoldLivingAreaIQR

sold["LivingArea_Outlier_Flag"] = (
    (sold["LivingArea"] > SoldLivingAreaUpper) | 
    (sold["LivingArea"] < SoldLivingAreaLower)
)

# Sold Flag for DaysOnMarket

SoldDaysOnMarketQ1 = sold["DaysOnMarket"].quantile(0.25)
SoldDaysOnMarketQ3 = sold["DaysOnMarket"].quantile(0.75)
SoldDaysOnMarketIQR = SoldDaysOnMarketQ3 - SoldDaysOnMarketQ1
SoldDaysOnMarketUpper = SoldDaysOnMarketQ3 + 1.5 * SoldDaysOnMarketIQR
SoldDaysOnMarketLower = SoldDaysOnMarketQ1 - 1.5 * SoldDaysOnMarketIQR

sold["DaysOnMarket_Outlier_Flag"] = (
    (sold["DaysOnMarket"] > SoldDaysOnMarketUpper) | 
    (sold["DaysOnMarket"] < SoldDaysOnMarketLower)
)










# Listing Flag for ClosePrice

ListingClosePriceQ1 = listing["ClosePrice"].quantile(0.25)
ListingClosePriceQ3 = listing["ClosePrice"].quantile(0.75)
ListingClosePriceIQR = ListingClosePriceQ3 - ListingClosePriceQ1
ListingClosePriceUpper = ListingClosePriceQ3 + 1.5 * ListingClosePriceIQR
ListingClosePriceLower = ListingClosePriceQ1 - 1.5 * ListingClosePriceIQR

listing["ClosePrice_Outlier_Flag"] = (
    (listing["ClosePrice"] > ListingClosePriceUpper) | 
    (listing["ClosePrice"] < ListingClosePriceLower)
)

# Listing Flag for LivingArea

ListingLivingAreaQ1 = listing["LivingArea"].quantile(0.25)
ListingLivingAreaQ3 = listing["LivingArea"].quantile(0.75)
ListingLivingAreaIQR = ListingLivingAreaQ3 - ListingLivingAreaQ1
ListingLivingAreaUpper = ListingLivingAreaQ3 + 1.5 * ListingLivingAreaIQR
ListingLivingAreaLower = ListingLivingAreaQ1 - 1.5 * ListingLivingAreaIQR

listing["LivingArea_Outlier_Flag"] = (
    (listing["LivingArea"] > ListingLivingAreaUpper) | 
    (listing["LivingArea"] < ListingLivingAreaLower)
)

# Listing Flag for DaysOnMarket

ListingDaysOnMarketQ1 = listing["DaysOnMarket"].quantile(0.25)
ListingDaysOnMarketQ3 = listing["DaysOnMarket"].quantile(0.75)
ListingDaysOnMarketIQR = ListingDaysOnMarketQ3 - ListingDaysOnMarketQ1
ListingDaysOnMarketUpper = ListingDaysOnMarketQ3 + 1.5 * ListingDaysOnMarketIQR
ListingDaysOnMarketLower = ListingDaysOnMarketQ1 - 1.5 * ListingDaysOnMarketIQR

listing["DaysOnMarket_Outlier_Flag"] = (
    (listing["DaysOnMarket"] > ListingDaysOnMarketUpper) | 
    (listing["DaysOnMarket"] < ListingDaysOnMarketLower)
)

print(sold.columns)
print(listing.columns)

soldmain = sold.copy()
listingmain = listing.copy()

soldmain.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSSold7.csv', index=False)
listingmain.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSListing7.csv', index=False)



# Written Analysis:

# Total rows in Sold: 397300
# Rows in Sold after filtering ClosePrice: 368396
# Rows in Sold after filtering LivingArea: 379984
# Rows in Sold after filtering DaysOnMarket: 368395
# Rows in Sold after filtering by all 3: 336893

# Total rows in Listing: 536346
# Rows in Listing after filtering ClosePrice: 527205
# Rows in Listing after filtering LivingArea: 510189
# Rows in Listing after filtering DaysOnMarket: 488498
# Rows in Listing after filtering by all 3: 459652
