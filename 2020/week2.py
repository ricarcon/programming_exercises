import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print('Beginning file download with requests')
user = "rcontre1"
password = "Hawaii506901!"
url = 'https://tidbits.intel.com/tidbits/web/app.php/admin/pordownload/ADS'
r = requests.get(url, auth=(user, password), verify=False)

with open(r"C:\Users\rcontre1\Desktop\ads.xls", 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
