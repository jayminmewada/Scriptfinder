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

for i in range(0,sheetRead.ncols):
    urls=sheetRead.col_values(i)

print('Getting Data Please Wait.....')

# Workbook is created(Write)
wb = Workbook()
sheetWrite = wb.add_sheet('Sheet 1')

# Specifying style of Head in excel
style = xlwt.easyxf('font: bold 1') 
  
# Specifying Header in excel
sheetWrite.write(0, 0, 'URL', style)
sheetWrite.write(0, 1, 'scriptStatus', style)

i=1

for URL in urls:
    # Returns a CloudScraper instance
    scraper = cloudscraper.create_scraper()
    # Exception Handing
    try:
        info = scraper.get(URL).text # => "<!DOCTYPE html><html><head>..."
    
    except Exception as e:
        # Appending error
        f = open("Error.txt", "a")
        f.write("There is an Error")
        f.close()

    # Parsing HTML
    soup = BeautifulSoup(info, "html.parser")

    # Finding Ads of context ads is live or not 
    scriptFinder = soup.find_all(text = re.compile('//pubs.contextads.live/(.*?)/(.*?)/generic.js'))
    
    sheetWrite.write(i, 0, URL)
    
    if not scriptFinder:

        sheetWrite.write(i,1,'Absent')
    
    else:

        sheetWrite.write(i,1,'Present')

    i+=1

    #Save output in excel
    wb.save('ContextAdsReport.xls')
  
print('Complete!!!')
