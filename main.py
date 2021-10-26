import requests
import json

# Github gist API URl
api_url = "https://api.github.com/gists"

URLs = 0

for page_number in range(1, 100):

  # Make request to gist API
  raw_data = requests.get(
    api_url,
    params={"per_page": 100, "page": page_number}).text

  # Parse data returned by gist API
  data = json.loads(raw_data)

  # Iterate over data to get all URLs
  for gist in data:
    print(next(iter(gist["files"].values()))["raw_url"])
    URLs += 1

print(URLs)  