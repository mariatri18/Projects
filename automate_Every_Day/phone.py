import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

Phonenumber=input("Enter you phone number: ")

number=phonenumbers.parse(Phonenumber)

print(geocoder.description_for_number(number,'en'))
print(carrier.name_for_number(number,'en'))
+