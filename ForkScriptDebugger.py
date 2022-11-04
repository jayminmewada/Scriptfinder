import re
from bs4 import BeautifulSoup
import cloudscraper
from xlwt import Workbook
import xlwt

#URL of Website to check whether script available or not
url=['https://curlytales.com','https://in.mashable.com/','https://www.jansatta.com/','https://www.loksatta.com/','https://me.mashable.com/','https://www.financialexpress.com/','https://indianexpress.com/article/business/banking-and-finance/e-rupee-launch-landmark-moment-in-the-history-of-currency-rbi-governor-shaktikanta-das-speech-at-fibac-2022-8244176/','https://www.layalina.com/أفكار-لأزياء-الهالوين-جربيها-من-مجموعات-عروض-الأزياء-425660.html','https://in.mashable.com/science/40923/just-in-time-for-halloween-the-suns-spooky-smile-in-this-new-nasa-image-is-unmissable','https://style.tribunnews.com/2022/10/10/nafsu-sudah-di-ubun-ubun-pasangan-muda-nekat-memadu-kasih-di-restoran-aksi-tak-senonoh-terekam','https://hai.grid.id/read/072294909/kisah-25-tahun-superman-is-dead-dari-ditipu-distro-hingga-dituduh-rasis-terhadap-jawa','https://www.idntimes.com/','http://popbela.com','http://popmama.com']
print('Getting Data Please Wait.....')


# Workbook is created
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

# Specifying style of column
style = xlwt.easyxf('font: bold 1') 
  
# Specifying column
sheet1.write(0, 0, 'URL', style)
sheet1.write(0, 1, 'scriptStatus', style)

#for each Loop
#excel column
i=1 
for URL in url:
    #scripting all the URl one by one
    scraper = cloudscraper.create_scraper(delay=10, browser={'custom': 'ScraperBot/1.0',})
    info = scraper.get(URL).text
    soup = BeautifulSoup(info, "html.parser")
    #Checking if script is Present or Not
    test = soup.find_all(text = re.compile('//pubs.contextads.live/(.*?)/(.*?)/generic.js'))
     
    if not test:
        #Script Absent
        sheet1.write(i, 0, URL)
        sheet1.write(i,1,'Absent')
        
    else:
        #Script Present
        sheet1.write(i, 0, URL)
        sheet1.write(i,1,'Present')

    i+=1
    #Saving the Output in excel File
    wb.save('ContextAdsScriptReport.xls')     
  
print('Complete!!!')





