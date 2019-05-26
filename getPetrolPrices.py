import requests
from bs4 import BeautifulSoup

address = requests.get('https://taripebi.ge/%E1%83%91%E1%83%94%E1%83%9C%E1%83%96%E1%83%98%E1%83%9C%\
E1%83%98%E1%83%A1-%E1%83%A4%E1%83%90%E1%83%A1%E1%83%94%E1%83%91%E1%83%98')
addressContent = address.content
soup = BeautifulSoup(addressContent, 'html.parser')

stations = {}
stationsNames = {"/გასამართი/1": "Gulf", "/გასამართი/2": "Frego",
                 "/გასამართი/9": "Portal", "/გასამართი/6": "Wissol",
                 "/გასამართი/5": "Socar", "/გასამართი/11": "Optima",
                 "/გასამართი/3": "Lukoil"}

for i in soup.findAll("td"):
    if "გასამართი" in str(i):
        test = str(i)[39:51]
        stations[stationsNames[test]] = []
    if "float" in str(i.div):
        if "---" in str(i.div):
            stations[stationsNames[test]].append("---")
        else:
            test1 = str(i.div)[37:41]
            test2 = str(i.div)[43:47]
            if "*" not in test1:
                stations[stationsNames[test]].append(test1)
            else:
                stations[stationsNames[test]].append(test2)

for i in stations:
    print(i, "რეგულარი: "
          + stations[i][0] + ' '
          + "ევრო რეგულარი: "
          + stations[i][1] + ' '
          + "პრემიუმი: "
          + stations[i][2] + ' '
          + "სუპერი: "
          + stations[i][3] + ' '
          + "დიზელი: "
          + stations[i][4] + ' '
          + "ევრო დიზელი: "
          + stations[i][5] + ' '
          + "ბიოდიზელი: "
          + stations[i][6] + ' ')

print("წყარო: www.taripebi.ge")






