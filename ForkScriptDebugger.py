import re
from bs4 import BeautifulSoup
import cloudscraper
from xlwt import Workbook
import xlwt
import xlrd

#Worbook is created (Read)
workbook = xlrd.open_workbook("Urls.xls")

#Get the first sheet in the workbook by index
sheetRead = workbook.sheet_by_index(0)

#Get URLS
for i in range(0,sheetRead.ncols):
    urls=sheetRead.col_values(i)

print('Getting Data Please Wait.....')

# Workbook is created(Write)
wb = Workbook()
sheetWrite = wb.add_sheet('Sheet 1')

# Specifying style of Head
style = xlwt.easyxf('font: bold 1') 
  
# Specifying Header
sheetWrite.write(0, 0, 'URL', style)
sheetWrite.write(0, 1, 'scriptStatus', style)

i=1

for URL in urls:
    #
    scraper = cloudscraper.create_scraper(delay=10, browser={'custom': 'ScraperBot/1.0',})
    
    info = scraper.get(URL).text
    
    soup = BeautifulSoup(info, "html.parser")
    
    #Script Present or Not
    
    test = soup.find_all(text = re.compile('//pubs.contextads.live/(.*?)/(.*?)/generic.js'))
    
    sheetWrite.write(i, 0, URL)
    
    if not test:
        
        sheetWrite.write(i,1,'Absent')
        
    else:
        sheetWrite.write(i,1,'Present')

    i+=1
    #Save output in excel
    wb.save('ContextAds.xls')
  
print('Complete!!!')
