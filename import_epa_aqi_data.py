## Import EPA AQI Data
# Quick script to download/unzip annual AQI summary data csv files for each year between 1980 to 2018 from https://aqs.epa.gov/aqsweb/airdata/download_files.html.

import requests, zipfile, io

# Remove item from scope or change year range to include/exclude files
params = {'scope':['cbsa', 'county'],
          'year':range(1980, 2018)}

for scope in params['scope']:
    for yr in params['year']:
        url = 'https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_{a}_{b}.zip'.format(a=scope, b=yr)
        r = requests.get(url)

        filename = url.split('/')[-1][:-4]

        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("raw_data")

print('Done.')