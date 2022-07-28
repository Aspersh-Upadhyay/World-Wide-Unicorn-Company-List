import requests
from bs4 import BeautifulSoup
import pandas as pd 

# import useful library which will help us to scrape the data from website
import requests # to make request 
from bs4 import BeautifulSoup # useful to scrape data from website
import pandas as pd # make DataFrame

url = 'https://www.cbinsights.com/research-unicorn-companies'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)

col_name  = [title.text for title in soup.find_all('th')]
# here we added columns in our comp_dataframe
comp_data = pd.DataFrame(columns = col_name)

# Here we are adding our data into each columns
for j in soup.find_all('tr')[1:]: # find table row 
 row_data = j.find_all('td') # find table data 
 row = [i.text for i in row_data] # get the text  
 length = len(comp_data) # checking length of our comp_data
 comp_data.loc[length] = row # here we are adding the each columns data


# checking data integrity using pandas
comp_data.info()

# sorting values in ascending order by Company Name
comp_data.sort_values(by=['Company'],ascending=True).reset_index(drop=True)

# finally we are going to make our DataFrame
comp_data.to_csv('World_Wide-Unicorn-Company-List.csv',index=False)
print(comp_data.head())