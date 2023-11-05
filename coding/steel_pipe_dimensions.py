# filename: steel_pipe_dimensions.py
import requests
from bs4 import BeautifulSoup

# URL of the website containing the steel pipe dimensions
url = "https://example.com/steel_pipe_dimensions"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the dimensions
table = soup.find("table")

# Iterate over the rows of the table
for row in table.find_all("tr"):
    # Extract the columns of each row
    columns = row.find_all("td")
    
    # Check if the row contains the dimensions
    if len(columns) >= 4:
        nps_number = columns[0].text
        inner_diameter = columns[1].text
        outer_diameter = columns[2].text
        wall_thickness = columns[3].text
        
        # Print the dimensions
        print(f"NPS Number: {nps_number}")
        print(f"Inner Diameter: {inner_diameter}")
        print(f"Outer Diameter: {outer_diameter}")
        print(f"Wall Thickness: {wall_thickness}")
        print("--------------------")
