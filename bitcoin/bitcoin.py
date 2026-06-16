import sys
import requests
import json

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=91305470eb92d58a3001d4d4249fcc4080cbcf1ef1d90d3184233c9ea04281c2")

o =response.json()
price = float(o["data"]["priceUsd"])

if (len(sys.argv) < 2):
    print("Missing command-line argument")
else:
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

total = price * bitcoins
print(f"${total:,.4f}")
