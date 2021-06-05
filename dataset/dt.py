from bs4 import BeautifulSoup
import requests
import urllib
import os

head = "https://www.gettyimages.in/photos/taj-mahal?page="
filter = "&phrase=taj%20mahal&sort=mostpopular"
page = 1
monument = "tajmahal"
os.mkdir(monument)
img_number = 1
for page in range(1, 20):
    url = head + str(page) + filter
    response = requests.Session().get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find_all('img')
    i = 0
    for img in images:
        if i>=200:
            break
        try:
            img_src = img["src"]
            print(img_src)
            if monument[:3] in img_src:
                
                img_data = requests.get(img_src).content
                with open(monument+"//"+monument[:3]+str(img_number)+'.jpg', 'wb+') as f:
                    f.write(img_data)
                i+=1
                img_number+=1
        except:
            pass



            

    
