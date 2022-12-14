# import useful library which will help us to scrape the data from website
import requests # to make request 
from bs4 import BeautifulSoup # useful to scrape data from website
import pandas as pd # make DataFrame

url = 'https://www.cbinsights.com/research-unicorn-companies'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)

col_name  = [title.text for title in soup.find_all('th')]
# here we added columns in our startup_dataframe
startup_data = pd.DataFrame(columns = col_name)

# Here we are adding our data into each columns
for j in soup.find_all('tr')[1:]: # find table row 
    row = [i.text for i in j.find_all('td')] # get the all table data
    startup_data.loc[len(startup_data)] = row # add table to each column 


# checking data integrity using pandas
startup_data.info()

# sorting values in ascending order by Company Name
startup_data.sort_values(by=['Company'],ascending=True).reset_index(drop=True)

# finally we are going to make our DataFrame
startup_data.to_csv('World_Wide-Unicorn-Company-List.csv',index=False)