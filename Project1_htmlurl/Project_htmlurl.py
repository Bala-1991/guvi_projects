

import requests

# GitHub API URL for issues in the pandas repository
json_url = "https://api.github.com/repos/pandas-dev/pandas/issues"

# Fetch the data from the URL
req = requests.get(json_url)

# Check if the request was successful
if req.status_code == 200:
    data = req.json()  # Parse the JSON response
else:
    print(f"Failed to fetch data. Status code: {req.status_code}")

# Function to recursively find and print all 'html_url' in the JSON data
def find_html_urls(data):
    if isinstance(data, dict):
        # If it's a dictionary, iterate through its keys and values
        for key, value in data.items():
            if key == 'html_url':
                print(value)  # Print the value if the key is 'html_url'
            else:
                find_html_urls(value)  # Recursively check the value
    elif isinstance(data, list):
        # If it's a list, iterate through its elements
        for item in data:
            find_html_urls(item)  # Recursively check each element

# Call the function to print all 'html_url'
find_html_urls(data)
