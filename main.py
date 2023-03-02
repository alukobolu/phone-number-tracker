import phonenumbers
import opencage
from test import number

from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number,'CH')
location = geocoder.description_for_number(ch_nmber,"en")
print(location)

from phonenumbers import carrier

service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))

from opencage.geocoder import OpenCageGeocode
key = ""

geocoder =OpenCageGeocode(key)
query = str(location)
results = geocoder.gecode(query)
print(results)