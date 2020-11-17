import phonenumbers
from phonenumbers import geocoder, carrier

sim=str(input("Enter your ph no[ex= +849253648985]:\n"))
pn = phonenumbers.parse(sim)

cr = carrier.name_for_number(pn, 'en')
rg = geocoder.description_for_number(pn, 'en')

print(f"| Region | Supplier |\n|-------------------|\n| {rg} | {cr} |")


