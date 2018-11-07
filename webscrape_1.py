#https://towardsdatascience.com/data-science-skills-web-scraping-using-python-d1a85ef607ed
#Referred link above with tweaks over unicode conversion issues
from bs4 import BeautifulSoup
import urllib
import requests
import csv

# specify the url
urlpage =  'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'
#print(urlpage)
# query the website and return the html to the variable 'page'
page = requests.get(urlpage, timeout=5)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page.content, "html.parser")


# find results within table
table = soup.find('table', attrs={'class': 'tableSorter'})
results = table.find_all('tr')
#print('Number of results', len(results))

# create and write headers to a list 
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])

# loop over results
for result in results:
    # find all columns per result
    #print(result)
    
    data = result.find_all('td')
    # check that columns have data 
    if len(data) == 0: 
        continue
# write columns to variables
    rank = data[0].getText().encode('utf-8')
    print(rank)
    company = data[1].getText().encode('utf-8')
    location = data[2].getText().encode('utf-8')
    yearend = data[3].getText().encode('utf-8')
    salesrise = data[4].getText().encode('utf-8')
    sales = data[5].getText().encode('utf-8')
    staff = data[6].getText().encode('utf-8')
    comments = data[7].getText().encode('utf-8')

    
    # extract description from the name
    companyname = data[1].find('span', attrs={'class':'company-name'}).getText().encode('utf-8')  
    description = company.replace(companyname, '')
    
    #emove unwanted characters
    sales = sales.strip('*').strip('†').replace(',','')
    #print("**")
    
    '''    
            # write each result to rows'''
    rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])

    
## Create csv and write rows to output file
with open('techtrack100.csv','w') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)


print("done")       