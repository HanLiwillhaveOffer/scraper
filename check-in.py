import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.footlocker.com/_-_/N-1z141xe"
headers = {
    'cookie': "TRACK_USER_P=63902192617093819090995854; mbdc=B466CE64.962B.5D78.0328.1CFC128BEFE2; cnx_sid=742794660782107463; cnx_start=1506436702909; cnx_rid=1506436703426186608; BVBRANDID=768dddf2-0033-41cf-a304-e70f052a0bd1; TID=5555%2D17261709412117090938884%2D0; SECURE_USER_PROFILE=7QtYIQqsj1dvbGPeN3ERBBeV57sxklqsal0BUR8YZQuyuftHtf02yE7v95qVWxAssEhs40y%2F%2FZBHUHaVbsbqY6CC2B1BV08vvNI9kJYgclM%3D; cnx_views=16; cnx_pg=1506437113803; SSLC=web122; DOTOMI_SESSION=1; INLINECARTSUMMARY=0%2C0; CHOSEN_BANNER=1; CHOSEN_BANNER_ID=25%25%20Off%20%2499%20%2B%20FS; USER_PROFILE=Cy4RyF0p%2B4F6dBSh8wSJgoiio1BSFONW5VPL3B0jCuHPYa1%2BuVUcC%2BvPQEzQR%2Fe5fQLRVYQjYP4UTiPzJ4%2FPwP0GigMla00yd%2FfK8HeKClgHarIIQxH%2BfuzF4p7BDMSz2T8X5mC6NAFTboyg4eE6n43CgLkWMBFvbmOQwdMWM0iZfvoAQ14joFY59IhtGumhSDsHQNC%2FWI13hIUCpdZuaoWkaTjwz4%2FcqqEYBMcfewSJakzZXnXx8eByhnIxoZsM7MXinsEMxLO5aKgO7DihemIXuIT1lw3hmUZJrcu5bLpkdSpYQTeJRtJmvgkTUSV7J2O6cSE5ntaUOrr%2BJbM5WA%3D%3D; BROWSER_SESSION=Cy4RyF0p%2B4FceUrVwCvwqFIkk%2F3G1%2F5k5hWa4S68U%2BaeiXi74X12otyNmXFH19vOxEkBltYfo6laV6Jff6JPclebgm9bEDrqmS2bD4o%2B2Zk5cYcvZ7AYNeH4upOkn3do%2Bw%2F5WNYvBdai7pX5%2BwL%2FevGDPK%2BmV7L5E1DvPYqa3LVKtrVRd9aCJNJ4ycdZbdBoamGPDVoEYHFUYo%2BL9HUMW2HxE5wahRBq5gDuTxgVpWjGjpmUwgcP7tp1VQgcjmDDAF4D7imypkQRvQeHJAryZ01IZjkDQ%2BPF%2Bw%2F5WNYvBdY52LX%2FxIbm%2BokhCYGG6v3ekzOW9L3yn3wo%2BiXuRPzXHR%2FJtARBmaG03H97N%2BX88%2Bq1vmDW%2BvdaxtOw9xq6cTT74zO6iE4VRkL8sbKa3CiJ5zkp48ctHHzUX9peBztAOQXhgACxz4Na06PXqpBMJoSLcHY77JpJ%2BC3zCNQO9xBU8k%2FwZeu%2FzGkZcHY77JpJ%2BC3Te0eMkOXTBQ%3D%3D; AKA_A2=1; cmTPSet=Y; mdr_browser=desktop; ak_bmsc=8E83F4F1B3E2C94F5BD231F1C4F18C55172DB62EFA0E000040121E5A496D485A~plO4uLoSPteWOV8nqNsV1pXswntZAWdqoen2wTJuccbRvKGGZEPbwyfz6Vlke/dedfYmxCudOEF1DQzncVszE0tRS2q4I5v4A4zZFXkT5qve7naeZrqpIrIWsZxmC1mOasFlQUW1yUECegeromJ1H5ek/7HqboRaXBdV902A8M0EYKdsKQQNR+Y0TMVkOYcByGnPj+QRJC7gYae/U0qtKIFm2hp3D9/ENgL3vLp8cFVVAmBCGfrrxnVDbbUf9kJ7XP; dtm_token=AQELI46wns71tAEBAQEAAQEJrgE; SSLB=0; bm_sz=8263BDC2DBBF886A0456FBBD87A718E2~QAAQLrYtFymIcQNgAQAAhlx3Bdimk6JUzCOgZbcS6WMPpfPo0St6+RlR5YzTpGURxURG2e5P/ayFSTtPh+cpTUy/jORGVaE4due/ZWl8thANFC0xGx39qXAU/WCFHhJNeuho93lb0dLQDZ2NnmMqW6/yqAHKhscdQvlgNlUQ484RFDdpQCmLPkeju3EUYyYg/yez; _abck=1F7BD30BB26D95B1F49203CC961DECFE172DB62EFA0E000044121E5AE92D4D32~0~utjCSLi95CTUgMccu2/HmLBz36pVRYze2HlCQX8TIhE=~-1~-1; RECENTSKULIST=14574705%3A150074%3AMain; LOCALEID=en%5FUS; mbox=check#true#1511920285|session#f4489f35d6e145069c1d2b07b952deb8#1511922085|PC#f4489f35d6e145069c1d2b07b952deb8.20_17#1513129825; _ga=GA1.2.1539365442.1506436701; _gid=GA1.2.1955319058.1511920194; visits=2; _mibhv=anon-1506436702203-5988748964_2389; xyz_cr_100238_et_111==undefined&cr=100238&et=111&ap=undefined; mbcc=334116DD-6601-54E2-98B6-2599994A030A; lastRskxRun=Tue Nov 28 2017 19:50:25 GMT-0600 (Central Standard Time); rskxRunCookie=0; rCookie=9vxibdg3u9essnlxvcmhjt; bm_sv=11514786404128E637441AFF65519C73~WC5kXGjGdgX+nQ/qIys6y2h3w3JCoc2fBmZJtqqsUEA8jV+kezPeyyFayGkvlSFsGSaDDen4kH/t7Prl7wQi5pLtwr+9EuNQmaff9jCrRQy6EcJ85MkfWNPS8VaCyO+xHLolE9T7kjptlyWkltmIHisoOeXp2fd4A13yWJS/YJk=; RT=\"sl=6&ss=1511920191978&tt=12151&obo=0&sh=1511920225487%3D6%3A0%3A12151%2C1511920221761%3D5%3A0%3A10789%2C1511920215903%3D4%3A0%3A9333%2C1511920214401%3D3%3A0%3A7882%2C1511920198575%3D2%3A0%3A5578&dm=footlocker.com&si=622e55db-2260-4a36-a09f-663cc60bdc44&bcn=%2F%2F36f1f340.akstat.io%2F&r=https%3A%2F%2Fwww.footlocker.com%2F_-_%2FN-1z141xe&ul=1511922149631\"; lastVisitURL=https://www.footlocker.com/_-_/N-1z141xe",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'x-hd-token': "rent-your-own-vps",
    'cache-control': "no-cache",
    'authority': "www.footlocker.com",
    'referer': "https://www.footlocker.com/",
    'postman-token': "662b75e6-a993-c5d8-f153-59df618e4bc7"
    }
response = requests.request("GET", url, headers=headers)
bs = BeautifulSoup(response.text,"lxml")
product_title = []
product_images = []
product_price = []
for tag in bs.find_all(class_="product_title"):
   product_title.append(tag.get_text())
   product_images.append(tag.parent.img.attrs['data-blzsrc'])
for tag in bs.find_all("div",{"class":"product_price"}):
   product_price.append(tag.get_text())
for index in range (len(product_price)):
    print("product title is:"+product_title[index])
    print("product image url is:"+product_images[index])
    print("product price is:"+product_price[index])


#print(bs.prettify())
