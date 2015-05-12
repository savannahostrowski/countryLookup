import ipgetter
import geoip2

ip = ipgetter.myip()
country = geoip2.country(ip)
print(country)
 
