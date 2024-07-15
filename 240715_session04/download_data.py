
import requests




url = 'https://universityofsussex-my.sharepoint.com/:x:/g/personal/hh65_sussex_ac_uk/EVzNpgzZewtIi_OUzqYRv_cBt3S4KIyUQrpz7yD_PPJfMA?e=pOu1Ff'

response = requests.get(url)

with open('example_data.csv', 'wb') as file:
    file.write(response.content)

print("Download complete.")