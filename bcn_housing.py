# -*- coding: utf-8 -*-
"""BCN housing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VOc3dBqY-FQAg-kS-HfIMt_2GJ1cKoWq

# Barcelona housing analysis project

The main purpose of this script is to perform an in-depth analysis of the housing market in Barcelona using search results from Idealista, a popular real estate website. The script aims to extract data from webpages specified by the user, stored in the same folder as this notebook. The extracted data is then organized and presented in visual formats, providing valuable insights beyond what is readily available online.

To use the script, the user needs to provide specific webpages to analyze. The script will extract relevant data from these webpages and generate a CSV file containing the collected information.

In order to gain a comprehensive understanding of the Barcelona housing market, the exercise should be run over a period of time. By accumulating time-trend data, we can uncover trends and patterns that are not easily accessible through individual snapshots. This long-term data enables us to gain valuable insights into the dynamics of the housing market in Barcelona.

## Script set up
1. Give permission to Colab to access GDrive
2. Specify root directory
"""

# from google.colab import drive
import os

# Mount Google Drive
# drive.mount('/content/drive')

# Set the directory path
# directory_path = '/content/drive'
directory_path = '/Users/gimmyliu/Downloads/BCN - Housing Analysis'

# List the contents of the directory
directory_contents = os.listdir(directory_path)

# Print the directory contents
for item in directory_contents:
    print(item)

# """**Note:**

# GL: the script below is using my personal MapQuest API. Limited to 15,000 map addresss to geo coordinate conversion requests per month. Plenty for now.
# """

import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import date  # Import the datetime module

api_key = "hello! get your own! :P"  # Replace with your MapQuest API key

# """## Data Import

# 1. Go to this idealista search (using the filters specified already in the URL) and download all the result pages

# https://www.idealista.com/en/venta-viviendas/barcelona-barcelona/con-metros-cuadrados-menos-de_60,pisos,terraza,ultimas-plantas,obra-nueva,buen-estado/?ordenado-por=fecha-publicacion-desc

# 2. Upload this week's saved webpages to the root folder. Use simple file names and separate each line with a comma ','
# 3. Specify the search date manually in the script below (or use the current date)



# """

# # UPDATE THIS!!!
# # Either hardcode:
# browsing_date = "2023-07-22"  # Set the browsing date as a variable
# # or
# # browsing_date = date.today().strftime("%Y-%m-%d")  # Add the date_browsed variable with today's date

# filenames = [
#     # JUL 22
#     '/content/drive/MyDrive/Colab Notebooks/BCN - Housing Analysis/matt1.html',
#     '/content/drive/MyDrive/Colab Notebooks/BCN - Housing Analysis/matt2.html',
#     '/content/drive/MyDrive/Colab Notebooks/BCN - Housing Analysis/matt3.html',
#     '/content/drive/MyDrive/Colab Notebooks/BCN - Housing Analysis/matt4.html'

#     # July 19
#     # '/content/drive/MyDrive/BCN - Housing Analysis/1.html',
#     # '/content/drive/MyDrive/BCN - Housing Analysis/2.html',
#     # '/content/drive/MyDrive/BCN - Housing Analysis/3.html'

#     # July 15
#     # '/content/drive/MyDrive/BCN - Housing Analysis/Property for sale in Barcelona, Spain flats and apartments — idealista.html'

#     # July 14
#     # '/content/drive/MyDrive/BCN - Housing Analysis/july14.html'

#     # July 11
#     # '/content/drive/MyDrive/BCN - Housing Analysis/saved_webpage.html',
#     # '/content/drive/MyDrive/BCN - Housing Analysis/Property for sale in Barcelona, Spain flats and apartments — idealista.html'
# ]

# """## Scrapping Idealista:

# See BeautifulSoup package documentation for more scraping related details.
# """

# import re
# location_data = []

# def get_coordinates(address):
#     url = f"http://www.mapquestapi.com/geocoding/v1/address?key={api_key}&location={address}"
#     response = requests.get(url)
#     data = response.json()
#     if data["info"]["statuscode"] == 0 and data["results"]:
#         lat = data["results"][0]["locations"][0]["latLng"]["lat"]
#         lng = data["results"][0]["locations"][0]["latLng"]["lng"]
#         return lat, lng
#     else:
#         return None, None

# for filename in filenames:
#     with open(filename, "r") as file:
#         html_content = file.read()
#     soup = BeautifulSoup(html_content, "html.parser")

#     properties = soup.find_all("article", class_="item")
#     for prop in properties:
#         name = prop.find("a", class_="item-link")["title"].strip()
#         url = prop.find("a", class_="item-link")["href"]  # Extract URL of the listing

#         # Extract Price
#         price_element = prop.find("span", class_="item-price")  # Extract Price
#         price = price_element.contents[0].strip().replace(",", "") if price_element else ""

#         # Extract Bedrooms
#         bedrooms = prop.find("span", class_="item-detail").text.strip().split(" ")[0]

#         # Extract Square Meters
#         sq_meters_element = prop.find_all("span", class_="item-detail")[1]
#         sq_meters = sq_meters_element.text.strip().split(" ")[0].replace(",", "")

#         # Extract floor number
#         floor_element = prop.find_all("span", class_="item-detail")[2] if len(prop.find_all("span", class_="item-detail")) >= 3 else None
#         floor_text = floor_element.text.strip() if floor_element else ""
#         floor_match = re.search(r'(\d+)(?:\w+)? floor', floor_text)
#         floor = floor_match.group(1) if floor_match else "-1"


#         # Extract StreetName
#         street_name = name.split("in ", 1)[1] if "in " in name else ""

#         if int(bedrooms) <= 4:
#             price_per_sq_m = float(price) / float(sq_meters)

#             # Geocode the street name
#             latitude, longitude = get_coordinates(street_name)

#             location_data.append({
#                 "Name": name,
#                 "Price": price,
#                 "Bedrooms": bedrooms,
#                 "Square Meters": sq_meters,
#                 "StreetName": street_name,
#                 "Price_per_sq_m": price_per_sq_m,
#                 "Latitude": latitude,
#                 "Longitude": longitude,
#                 "URL": url,
#                 "date_browsed": browsing_date,  # Assign the value of browsing_date to date_browsed field
#                 "Floor": floor  # Add the extracted floor number
#             })

# # print(location_data)

# # Convert location_data to a pandas DataFrame
# df = pd.DataFrame(location_data)
# # print(df)

# """## Save the scrapping work into a CSV file

# After this, the uploaded html files from the week can be deleted as the information is already stored in the csv file.

# **Note:**
# Uncomment the line "# files.download(file_name)" to actually download the csv onto your computer. You would need to re-upload the csv file back onto GDrie.
# """

# import pandas as pd
# from google.colab import files

# # Convert location_data to a pandas DataFrame
# df = pd.DataFrame(location_data)

# # Define the file name
# file_name = f"location_data_{browsing_date}.csv"

# # Save the DataFrame as a CSV file
# df.to_csv(file_name, index=False)

# print("CSV file created successfully.")

# location_data = []

# # Generate a download link for the CSV file

# # files.download(file_name)

# """## Load the CSVs into dataframes and post-process:


# 1.   Upload the csv file that was downloaded in the previous step back onto GDrive. In the future, the script could consider saving the CSV directly in GDrive.
# 2.   The script compares csv from this week vs. previous week. The differences between the CSV files are analyzed. This helps to establish which listings are delisted, which listings are still on the website, how long did each listing stay on the website (earliest and last date recorded).

# """

import pandas as pd
from datetime import datetime

# Set the display options to show all rows and columns
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)

# List the CSV files you want to merge
filenames = [
    directory_path+'/location_data_2023-07-11.csv',  # dummy data: keep it here or the current csv merge function will throw an error.

    # BASELINE FOR PRICE/SQ_M (EXTRACTED 2023-07-19: all the apartment in Barcelona with Top floor && terase && <60 sqm)
    directory_path+'/location_data_2023-07-19.csv',  # 2023-07-19: all the apartment in Barcelona with (top floor && terase && <60 sqm)
    directory_path+'/location_data_2023-07-22.csv'  # 2023-07-22: w matt in milan, demo
    # REMEMBER TO ADD A COMMA AFTER INSERTING A NEW ROW!

    # '/content/drive/MyDrive/BCN - Housing Analysis/location_data_2023-07-11.csv',  # dummy data
    # '/content/drive/MyDrive/BCN - Housing Analysis/location_data_2023-07-14.csv', # random data for debugging
    # '/content/drive/MyDrive/BCN - Housing Analysis/location_data_2023-07-15.csv', # random data for debugging
    ]

# Initialize an empty list to store the DataFrames
dataframes = []

# Read each CSV file into a DataFrame and append it to the list
for file in filenames:
    df = pd.read_csv(file)
    dataframes.append(df)

# Concatenate the DataFrames vertically
merged_df = pd.concat(dataframes, ignore_index=True)

# Group the DataFrame by the "URL" column and find the maximum date_browsed for each group
latest_date = merged_df["date_browsed"].max()

# Group the DataFrame by the "URL" column and check if each row's date_browsed is equal to the latest date
merged_df["Delisted"] = merged_df["date_browsed"] < latest_date

# Group the DataFrame by the "URL" column and set "Delisted" as True for all rows in a group if none of the rows have "Delisted" as False
merged_df["Delisted"] = merged_df.groupby("URL")["Delisted"].transform("all")

# Group the DataFrame by the "URL" column and find the minimum and maximum date_browsed for each group
grouped_dates = merged_df.groupby("URL")["date_browsed"].agg(["min", "max"])

# Merge the grouped_dates DataFrame back into the original DataFrame based on "URL"
merged_df = pd.merge(merged_df, grouped_dates, on="URL", suffixes=("", "_max"))

# Rename the "min" and "max" columns to "date_browsed_min" and "date_browsed_max"
merged_df.rename(columns={"min": "date_browsed_min", "max": "date_browsed_max"}, inplace=True)

# Convert "date_browsed_min" and "date_browsed_max" columns to datetime objects
merged_df["date_browsed_min"] = pd.to_datetime(merged_df["date_browsed_min"])
merged_df["date_browsed_max"] = pd.to_datetime(merged_df["date_browsed_max"])

# Calculate the difference in days for "Num_days_listed"
merged_df["Num_days_listed"] = (merged_df["date_browsed_max"] - merged_df["date_browsed_min"]).dt.days

# For rows where "Delisted" is False, calculate the difference between "date_browsed_min" and today's date
today = pd.Timestamp(datetime.now().date())
merged_df.loc[~merged_df["Delisted"], "Num_days_listed"] = (today - merged_df.loc[~merged_df["Delisted"], "date_browsed_min"]).dt.days

# Sort the DataFrame by "date_browsed" in ascending order
merged_df.sort_values(by="date_browsed", ascending=True, inplace=True)

# Drop duplicates based on the "URL" column, keeping the row with the latest date_browsed_max
merged_df.drop_duplicates(subset="URL", keep="first", inplace=True)

# Convert the merged DataFrame back to a list of dictionaries
location_data = merged_df.to_dict('records')

# Count the number of True and False values in the "Delisted" column
delisted_counts = merged_df["Delisted"].value_counts()
print("Number of Delisted True:", delisted_counts[True])
print("Number of Delisted False:", delisted_counts[False])
print(merged_df.shape)

# Print the updated DataFrame with the specified columns
print(merged_df.loc[:, ["URL", "date_browsed", "Floor", "Delisted", "date_browsed_min", "date_browsed_max", "Num_days_listed"]])

# Reset the display options to their default values (optional)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
pd.reset_option('display.width')

# """## Visualization of data:

# ### Basic heat map (Price/Sq m)

# The basic heat map uses a black and white background to highlight the building shapes and street layout, providing a quick representation of the surrounding space.

# *   Circle Size: The size of each circle on the map corresponds to the square meter area of the respective apartment.
# *    Color Gradient: The color of the heat map indicates the price per square meter for each location.
# """

import folium
import xyzservices.providers as xyz
from branca.colormap import LinearColormap

# Center the map around Barcelona
map_barcelona = folium.Map(location=[41.3851, 2.1734], zoom_start=12)

# Add the Stadia Maps Stamen Toner provider details via xyzservices
tile_provider = xyz.Stadia.StamenTonerLite

# Update the URL to include the API key placeholder
tile_provider["url"] = tile_provider["url"] + "?api_key={api_key}"

# Create the folium TileLayer, specifying the API key
folium.TileLayer(
    tiles=tile_provider.build_url(api_key='hello! get your own! :P'),
    attr=tile_provider.attribution,
    name=tile_provider.name,
    max_zoom=tile_provider.max_zoom,
    detect_retina=True
).add_to(map_barcelona)

folium.LayerControl().add_to(map_barcelona)

# Save the map to an HTML file
map_barcelona.save('barcelona_map.html')


# Create a dictionary to store the overlapping locations
overlapping_locations = {}

# Calculate the maximum and minimum square meters for scaling the circle markers
max_sq_meters = max([loc['Price_per_sq_m'] for loc in location_data])
min_sq_meters = min([loc['Price_per_sq_m'] for loc in location_data])

# Iterate through the location data
for location in location_data:
    lat = location['Latitude']
    lon = location['Longitude']

    # Check if the location's latitude and longitude are already present in the dictionary
    if (lat, lon) in overlapping_locations:
        # If present, concatenate the information with a line break
        overlapping_locations[(lat, lon)] += f"<br>---<br>{location['Name']}<br>Price: {location['Price']}<br>Price per sqm: {location['Price_per_sq_m']}<br>Address: {location['StreetName']}<br>Floor: {location['Floor']}<br>Date Browsed: {location['date_browsed']}<br><a href='{location['URL']}' target='_blank'>Link</a>"
    else:
        # If not present, add the location to the dictionary
        overlapping_locations[(lat, lon)] = f"<b>Name:</b> {location['Name']}<br><b>Price:</b> {location['Price']}<br><b>Price per sqm:</b> {location['Price_per_sq_m']}<br><b>Address:</b> {location['StreetName']}<br><b>Floor:</b> {location['Floor']}<br><b>Date Browsed:</b> {location['date_browsed']}<br><a href='{location['URL']}' target='_blank'>Link</a>"

    # Calculate the scaled radius based on square meters
    radius = 5 + 10 * ((location['Price_per_sq_m'] - min_sq_meters) / (max_sq_meters - min_sq_meters))

    # Create a colormap
    colormap = LinearColormap(
        colors=['green', 'yellow', 'red'],
        vmin=min_sq_meters,
        vmax=max_sq_meters
    )

    # Create a circle marker for each location with weight as the price per square meter
    folium.CircleMarker(
        location=[lat, lon],
        radius=radius,
        weight=0,
        fill=True,
        fill_color=colormap(location['Price_per_sq_m']),
        fill_opacity=0.6,
        popup=overlapping_locations[(lat, lon)]
    ).add_to(map_barcelona)

# Add the colormap to the map
colormap.add_to(map_barcelona)

# Display the map
map_barcelona.save('barcelona_map.html')

# """Or if we prefer to have the colored version of the city map:"""

# import folium
# from branca.colormap import LinearColormap

# # Create a map centered around Barcelona with a specified size
# map_barcelona = folium.Map(location=[41.3851, 2.1734], zoom_start=12, scrollWheelZoom=False, rotation=45)

# # Create a dictionary to store the overlapping locations
# overlapping_locations = {}

# # Calculate the maximum and minimum square meters for scaling the circle markers
# max_sq_meters = max([loc['Price_per_sq_m'] for loc in location_data])
# min_sq_meters = min([loc['Price_per_sq_m'] for loc in location_data])

# # Iterate through the location data
# for location in location_data:
#     lat = location['Latitude']
#     lon = location['Longitude']

#     # Check if the location's latitude and longitude are already present in the dictionary
#     if (lat, lon) in overlapping_locations:
#         # If present, concatenate the information with a line break
#         overlapping_locations[(lat, lon)] += f"<br>---<br>{location['Name']}<br>Price: {location['Price']}<br>Price per sqm: {location['Price_per_sq_m']}<br>Address: {location['StreetName']}<br>Floor: {location['Floor']}<br>Date Browsed: {location['date_browsed']}<br><a href='{location['URL']}' target='_blank'>Link</a>"
#     else:
#         # If not present, add the location to the dictionary
#         overlapping_locations[(lat, lon)] = f"<b>Name:</b> {location['Name']}<br><b>Price:</b> {location['Price']}<br><b>Price per sqm:</b> {location['Price_per_sq_m']}<br><b>Address:</b> {location['StreetName']}<br><b>Floor:</b> {location['Floor']}<br><b>Date Browsed:</b> {location['date_browsed']}<br><a href='{location['URL']}' target='_blank'>Link</a>"

#     # Calculate the scaled radius based on square meters
#     radius = 5 + 10 * ((location['Price_per_sq_m'] - min_sq_meters) / (max_sq_meters - min_sq_meters))

#     # Create a colormap
#     colormap = LinearColormap(
#         colors=['green', 'yellow', 'red'],
#         vmin=min_sq_meters,
#         vmax=max_sq_meters
#     )

#     # Create a circle marker for each location with weight as the price per square meter
#     folium.CircleMarker(
#         location=[lat, lon],
#         radius=radius,
#         weight=0,
#         fill=True,
#         fill_color=colormap(location['Price_per_sq_m']),
#         fill_opacity=0.6,
#         popup=overlapping_locations[(lat, lon)]
#     ).add_to(map_barcelona)

# # Add the colormap to the map
# colormap.add_to(map_barcelona)

# # Display the map
# map_barcelona

# """## Groupped by browsing date

# The dataframe is grouped by the earliest date a listing appeared. The intent is to help separate listing based on date, so we can visit the search result each week individually.
# """

# # Create a map centered around Barcelona
# map_barcelona_grouped_by_date = folium.Map(location=[41.3851, 2.1734], zoom_start=12, scrollWheelZoom=False)


# # Group location data by date_browsed
# grouped_data = merged_df.groupby('date_browsed')

# # Iterate through the grouped data
# for date_browsed, group in grouped_data:
#     # Create a new feature group for each date
#     feature_group = folium.FeatureGroup(name=date_browsed)

#     # Iterate through the locations in the group
#     for _, location in group.iterrows():
#         lat = location['Latitude']
#         lon = location['Longitude']
#         name = location['Name']
#         price = location['Price']
#         price_per_sqm = location['Price_per_sq_m']
#         address = location['StreetName']
#         url = location['URL']  # Extract the URL
#         floor = location['Floor']  # Extract the floor number

#         # Create a circle marker for each location
#         folium.CircleMarker(
#             location=[lat, lon],
#             radius=15,
#             weight=0,
#             fill=True,
#             fill_color=colormap(price_per_sqm),
#             fill_opacity=0.6,
#             popup=f"<b>Name:</b> {name}<br><b>Price:</b> {price}<br><b>Price per sqm:</b> {price_per_sqm}<br><b>Address:</b> {address}<br><b>Date Browsed:</b> {date_browsed}<br><b>Floor:</b> {floor}<br><a href='{url}' target='_blank'>Link</a>"
#         ).add_to(feature_group)

#     # Add the feature group to the map
#     feature_group.add_to(map_barcelona_grouped_by_date)

# # Add the colormap to the map
# colormap.add_to(map_barcelona_grouped_by_date)

# # Add layer control to toggle between dates
# folium.LayerControl().add_to(map_barcelona_grouped_by_date)

# # Display the map
# map_barcelona_grouped_by_date