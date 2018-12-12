#!/usr/bin/python3
import whois
print('____________________________')
print('|                          |')
print('|welcome to sudarshan (who)|')
print('|__________________________|')
data = input("Enter a domain: ")
data1 = whois.whois(data)
print('[1] domain name: \n[2] domain expiration date: \n[3] html element(text): \n[4] details: ')
key = int(input('->'))

if key == 1:
   print('the name of the domain is: ',data1.name)

elif key == 2:
   print('the data of the domain is: ',data1.expiration_date)

elif key == 3:
   print('the html element is: ',data1.text)

elif key == 4:
   print('[*]softwear name: who\n[*]developer name: techie\n[*]softwear version: 1.0.0\n[*]date created: 08:12:2018')

else:
   print('not valid comend')


