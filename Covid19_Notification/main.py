from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMy(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\ashwary.soni\Desktop\Udemy_DS\Python_June_2020_VS_Code\Practice_basic\virus_image_axA_icon.ico",
        timeout = 15
    )

def getData(url):
   r = requests.get(url)
   return r.text

if __name__ == "__main__":
      
        #notifyMy("Covid19-Update", "Wash your hand frequently...")
        myHtmlData = getData('https://www.mohfw.gov.in/')
   
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify())

        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
          #[0] becoz we need 1st table i.e 0th index
          myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]  
        #sliced   
        itemList = myDataStr.split("\n\n")
       # print(itemList)
   
        states = ['Madhya Pradesh','Delhi','Andhra Pradesh']
        for item in itemList[0:22]:
           dataList = item.split('\n')
           if dataList[1] in states:
             print(dataList)
             nTitle = 'Cases of Covid-19'
             nText = f" State {dataList[1]}: Active-Cases* : {dataList[2]}\nCured* : {dataList[3]}\nDeaths** : {dataList[4]}\nTotal Confirmed : {dataList[5]}"
             notifyMy(nTitle,nText)
             time.sleep(2)
             