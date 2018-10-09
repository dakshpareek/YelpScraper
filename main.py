import requests
import lxml,json
from bs4 import BeautifulSoup


def hashes(start):
  url="https://www.yelp.com/search?find_loc=Melbourne,+Melbourne+Victoria,+Australia&start={}&cflt=restaurants".format(start)
  #print(url)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "lxml")
  blocks=soup.findAll('li',{'class':'regular-search-result'})
  #print(len(blocks))
  if len(blocks) ==0 :
    return False
  else:
    for i,block in enumerate(blocks):
      try:
        name=block.find('a',{'class':'biz-name js-analytics-click'}).text
      except:
        name=''
      try:
        number=block.find('span',{'class':'biz-phone'}).text.strip()
      except:
        number=''
      try:
        address=block.find('address').text.strip()
      except:
        address=''
      data.append([name,number,address])
    return True

ret=True
i=0
data=[]
while ret:
  print(i)
  ret=hashes(i)
  i+=30
dt={'data':data}
with open('hotels_data_sample.json', 'w') as outfile:
  json.dump(dt,outfile,indent=4)