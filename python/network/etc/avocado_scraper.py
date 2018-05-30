import requests
import re

# Example of how to query and parse web pages

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36' }

x = requests.get(
    'http://indexfresh.com/growers/avocado-sizing/',
    headers=headers)

m = re.search('<td style="text-align: center;" width="154">28</td>',x.text)
f = re.search('>..<',m.group(0))
print "Scaped size of avocado: "+f.group(0)+" please clap"
