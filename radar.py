import requests
import xml.etree.ElementTree as ET

URL = "https://ted.europa.eu/api/v3/notices/search?limit=5"

print("Pobieram przetargi z TED...")

try:
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    print("Połączenie z TED działa!")
    print(response.text[:500])

except Exception as e:
    print("Błąd:", e)
