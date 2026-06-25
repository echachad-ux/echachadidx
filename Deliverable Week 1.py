import pandas as pd

# add CSV files

# use sold_filled for: 202405,202406,202407,202501

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

soldlist = [sold202401, sold202402, sold202403, sold202404, sold202405, sold202406, sold202407, sold202408, sold202409, sold202410, sold202411, sold202412, sold202501, sold202502, sold202503, sold202504, sold202505, sold202506, sold202507, sold202508, sold202509, sold202510, sold202511, sold202512, sold202601, sold202602, sold202603, sold202604]

# Count rows before concatenation
print("Sold dataset total rows before concatenation:")
for solddataset in soldlist:
    print(len(solddataset))

# Concatenate sold datasets
combinesold = pd.concat(soldlist)
print("Sold dataset total rows after concatenation")
print(len(combinesold))

# Drop duplicates
cleanedsoldlist = combinesold.drop_duplicates()
print("Sold dataset total rows after dropped duplicates")
print(len(cleanedsoldlist))


# Filter to residential
filteredsold = cleanedsoldlist[cleanedsoldlist["PropertyType"] == "Residential"]
print("Sold dataset total rows after filtering")
print(len(filteredsold))

# Create a copy
mainsold = filteredsold.copy()

# Export as Sold CSV
mainsold.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/CRMLSSold.csv', index=False)

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

listinglist = [listing202401, listing202402, listing202403, listing202404, listing202405, listing202406, listing202407, listing202408, listing202409, listing202410, listing202411, listing202412, listing202501, listing202502, listing202503, listing202504, listing202505, listing202506, listing202507, listing202508, listing202509, listing202510, listing202511, listing202512, listing202601, listing202602]

# Count rows before concatenation
print("Listing dataset total rows before concatenation")
for listingdataset in listinglist:
    print(len(listingdataset))

# Concatenate datasets
combinelisting = pd.concat(listinglist)
print("Listing dataset total rows after concatenation")
print(len(combinelisting))

# Drop duplicates
cleanedlistinglist = combinelisting.drop_duplicates()
print("Listing dataset total rows after dropped duplicates")
print(len(cleanedlistinglist))

# Filter to residential
filteredlisting = cleanedlistinglist[cleanedlistinglist["PropertyType"] == "Residential"]
print("Listing dataset total rows after filtering")
print(len(filteredlisting))

# Create a copy
mainlisting = filteredlisting.copy()

# Export as Sold CSV
mainlisting.to_csv('/Users/eshaanchachad/Desktop/IDXExchange/CRMLSListing.csv', index=False)