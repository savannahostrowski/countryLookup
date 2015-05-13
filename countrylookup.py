import ipgetter, pygeoip

def getCountry():
	ip = ipgetter.myip()
	print(ip)
	gi = pygeoip.GeoIP('GeoIP.dat')
	country = gi.country_name_by_addr(ip)
	print(country)


getCountry()