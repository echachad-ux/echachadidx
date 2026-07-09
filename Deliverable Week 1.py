import pandas as pd




# Sold

# Import all CSVs
# Create a list with all CSVs

sold202401 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202401.csv", encoding="ISO-8859-1")
sold202402 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202402.csv", encoding="ISO-8859-1")
sold202403 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202403.csv", encoding="ISO-8859-1")
sold202404 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202404.csv", encoding="ISO-8859-1")
sold202405 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202405_filled.csv", encoding="ISO-8859-1")
sold202406 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202406_filled.csv", encoding="ISO-8859-1")
sold202407 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202407_filled.csv", encoding="ISO-8859-1")
sold202408 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202408.csv", encoding="ISO-8859-1")
sold202409 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202409.csv", encoding="ISO-8859-1")
sold202410 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202410.csv", encoding="ISO-8859-1")
sold202411 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202411.csv", encoding="ISO-8859-1")
sold202412 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202412.csv", encoding="ISO-8859-1")

sold202501 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202501_filled.csv", encoding="ISO-8859-1")
sold202502 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202502.csv", encoding="ISO-8859-1")
sold202503 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202503.csv", encoding="ISO-8859-1")
sold202504 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202504.csv", encoding="ISO-8859-1")
sold202505 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202505.csv", encoding="ISO-8859-1")
sold202506 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202506.csv", encoding="ISO-8859-1")
sold202507 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202507.csv", encoding="ISO-8859-1")
sold202508 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202508.csv", encoding="ISO-8859-1")
sold202509 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202509.csv", encoding="ISO-8859-1")
sold202510 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202510.csv", encoding="ISO-8859-1")
sold202511 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202511.csv", encoding="ISO-8859-1")
sold202512 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202512.csv", encoding="ISO-8859-1")

sold202601 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202601.csv", encoding="ISO-8859-1")
sold202602 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202602.csv", encoding="ISO-8859-1")
sold202603 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202603.csv", encoding="ISO-8859-1")
sold202604 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202604.csv", encoding="ISO-8859-1")
sold202605 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold202605.csv", encoding="ISO-8859-1")

soldlist = [sold202401, sold202402, sold202403, sold202404, sold202405, sold202406, sold202407, sold202408, sold202409, sold202410, sold202411, sold202412, sold202501, sold202502, sold202503, sold202504, sold202505, sold202506, sold202507, sold202508, sold202509, sold202510, sold202511, sold202512, sold202601, sold202602, sold202603, sold202604]

# Concatenate sold datasets

sold_concat = pd.concat(soldlist)

# Drop duplicates and extra columns

sold_drop_duplicates = sold_concat.drop_duplicates()

columns_to_drop = ["latfilled", "lonfilled"]
sold_cleaned = sold_drop_duplicates.drop(columns=columns_to_drop)

# Filter to residential

sold_filtered = sold_cleaned[sold_cleaned["PropertyType"] == "Residential"]

# Create CSV

sold = sold_filtered.copy()
sold.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSSold.csv', index=False)

# Sold row counts for each month
# 17976
# 19925
# 23276
# 24640
# 26487
# 24328
# 26240
# 24558
# 21267
# 23274
# 20279
# 20241
# 18738
# 18702
# 21445
# 23262
# 23154
# 22883
# 23646
# 22972
# 22443
# 23233
# 19088
# 20538
# 16487
# 19010
# 23372
# 24261

# Sold row counts after concatenation
# 615725

# Sold row counts after dropping duplicates
# 615585

# Sold row counts after filtering to residential
# 414015








# Listing

# Import all CSVs
# Create a list with all CSVs

listing202401 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202401.csv", encoding="ISO-8859-1")
listing202402 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202402.csv", encoding="ISO-8859-1")
listing202403 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202403.csv", encoding="ISO-8859-1")
listing202404 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202404.csv", encoding="ISO-8859-1")
listing202405 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202405.csv", encoding="ISO-8859-1")
listing202406 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202406.csv", encoding="ISO-8859-1")
listing202407 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202407.csv", encoding="ISO-8859-1")
listing202408 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202408.csv", encoding="ISO-8859-1")
listing202409 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202409.csv", encoding="ISO-8859-1")
listing202410 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202410.csv", encoding="ISO-8859-1")
listing202411 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202411.csv", encoding="ISO-8859-1")
listing202412 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202412.csv", encoding="ISO-8859-1")

listing202501 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202501.csv", encoding="ISO-8859-1")
listing202502 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202502.csv", encoding="ISO-8859-1")
listing202503 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202503.csv", encoding="ISO-8859-1")
listing202504 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202504.csv", encoding="ISO-8859-1")
listing202505 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202505.csv", encoding="ISO-8859-1")
listing202506 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202506.csv", encoding="ISO-8859-1")
listing202507 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202507.csv", encoding="ISO-8859-1")
listing202508 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202508.csv", encoding="ISO-8859-1")
listing202509 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202509.csv", encoding="ISO-8859-1")
listing202510 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202510.csv", encoding="ISO-8859-1")
listing202511 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202511.csv", encoding="ISO-8859-1")
listing202512 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202512.csv", encoding="ISO-8859-1")

listing202601 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202601.csv", encoding="ISO-8859-1")
listing202602 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202602.csv", encoding="ISO-8859-1")
listing202603 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202603.csv", encoding="ISO-8859-1")
listing202604 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202604.csv", encoding="ISO-8859-1")
listing202605 = pd.read_csv("/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing202605.csv", encoding="ISO-8859-1")

listinglist = [listing202401, listing202402, listing202403, listing202404, listing202405, listing202406, listing202407, listing202408, listing202409, listing202410, listing202411, listing202412, listing202501, listing202502, listing202503, listing202504, listing202505, listing202506, listing202507, listing202508, listing202509, listing202510, listing202511, listing202512, listing202601, listing202602, listing202603, listing202604]

# Concatenate sold datasets

listing_concat = pd.concat(listinglist)

# Drop duplicates and extra columns

listing_cleaned = listing_concat.drop_duplicates()

# Filter to residential

listing_filtered = listing_cleaned[listing_cleaned["PropertyType"] == "Residential"]

# Create CSV

listing = listing_filtered.copy()
listing.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/csvs/CRMLSListing.csv', index=False)

# Sold row counts for each month
# 27454
# 27447
# 32282
# 36503
# 38796
# 35893
# 36340
# 35305
# 34625
# 34730
# 25128
# 19417
# 37469
# 33983
# 38492
# 40187
# 40271
# 26399
# 27345
# 25210
# 26923
# 27586
# 20677
# 18773
# 35302
# 32884
# 39153
# 39020

# Sold row counts after concatenation
# 893594

# Sold row counts after cleaning
# 893594

# Sold row counts after filtering to residential
# 567549
