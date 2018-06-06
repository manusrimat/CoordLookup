
import re
import urllib
import json
from requests import get

def get_ip():
	url = "http://checkip.dyndns.org"
	data = urllib.urlopen(url).read()
	ip_address = data[-27:-16]
	return ip_address

def get_data(ip_address):
	query = 'https://ipapi.co/'+str(ip_address) +'/json/'
	loc = get(query);
	return loc

def print_val(ip,field):
	return get('https://ipapi.co/'+str(ip)+'/'+field+'/').text

def print_info(ip):
	print "\nBased in " + print_val(ip,"city") + "," + print_val(ip,"region")
	print "\nYour latitude is: " + print_val(ip, "latitude")
	print "Your longitude is: " + print_val(ip, "longitude")

def main():
	print "\nGetting coordinate information for your location..."
	ip_address = get_ip()
	query = get_data(ip_address)
	print_info(ip_address)
   


if __name__ == "__main__":
	main()
