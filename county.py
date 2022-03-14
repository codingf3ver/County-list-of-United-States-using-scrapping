# web scrapping county names using state
from bs4 import BeautifulSoup
import request

def get_county_list():
  master_county_list = []

  county_dict = dict()

#   You can add any states name
  urls = ['https://en.wikipedia.org/wiki/List_of_counties_in_New_Jersey','https://en.wikipedia.org/wiki/List_of_counties_in_New_York'\
          ,'https://en.wikipedia.org/wiki/List_of_parishes_in_Louisiana','https://en.wikipedia.org/wiki/List_of_counties_in_Texas'\
          ,'https://simple.wikipedia.org/wiki/List_of_counties_in_Florida']

  for url in urls:
    states_county_list = []
    url=requests.get(url).text
    soup=BeautifulSoup(url,'lxml')
    wiki = soup.find('table', class_="wikitable sortable")

    for i in wiki.tbody.find_all('th'):
      if "County" in i.text:
        text = i.text
        text = text.split('County')
        states_county_list.append(text[0].strip())
      if "Parish" in i.text:
        text = i.text
        text = text.split('Parish')
        states_county_list.append(text[0].strip())

    
    if len(states_county_list)<3:  
      for i in wiki.tbody.find_all('td'):
          if "County" in i.text:
            text = i.text
            text = text.split('County')
            states_county_list.append(text[0].strip())
    
    master_county_list.append(states_county_list[2:])

# Adding county into dictionary
  for country,county in zip(urls,master_county_list):
    country = country.split('_')[-2:]
    if 'New' in country:
      c = " ".join(country)
      county_dict[c] = county
    else:
      c = country[-1]
      county_dict[c] = county

  return county_dict

county_list = get_county_list()

      
