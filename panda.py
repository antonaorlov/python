import pandas as pd
#reads csv file
df = pd.read_csv('file.csv')
#top 3 rows printed
print(df.head(3))
#print the last 3 rows
print(df.tail(3))
#reading headers
print(df.columns)
#read column, prints all names
print(df['Name'])
#prints top 5 names
print(df['Name'][0:5])
##multiple columns
df[['Name', 'Type 1', 'HP']]
#read 1-4 row
print(df.iloc[1:4])
#specific row, second colum first row
print(df.iloc[2,1])
for index, row in df.iterrows():
    print(index, row['Name'])
#specific one
df.loc[df['Type 1'] == "Fire"]
df.describe() #lookup data
df.sort_values('Name', ascending=False) #sorted by Names
df.sort_values(['Type 1', 'HP'], ascending=[1,0]) #sorted by type 1 and HP, Type 1 ascending, HP descending



#write data

#write a new column Total with sum of all stats
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] #adds new column
df.head(5)
df = df.drop(columns=['Total']) #drops column
df['Total'] = df.iloc[:, 4:10].sum(axis=1) #: all rows, 4:10 columns 4-9, axis=1 adds horizontally

cols = list(df.columns.values) #list of columns
df=df[cols[0:4]+ [cols[-1]]+cols[4:12]] #rearrange columns

#saving file
df.to_csv('modified.csv', index=False, sep='\t') #index=False removes index column in csv file, seperate by tab



#Filtering Data
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')] #only grass type columns with poison as second type
print(new_df)
new_df.to_csv('filtered.csv') #saves filtered data to csv file
new_df = new_df.reset_index(drop=True, inplace=True) #resets index drop=True removes old index, inplace=True changes new_df to new index
df.loc[df['Name'].str.contains('Mega')] #contains mega in name
df.loc[~df['Name'].str.contains('Mega')] #does not contain mega in name

import re
df.loc[df['Type 1'].str.contains('Fire|Grass', flags=re.I, regex=True)] #flags=re.I ignores case sensitive, regex=True allows to use regex
#^pi[a-z]* starts with pi, [a-z]* any letter after pi, * any letter after pi
df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer' #changes fire to flamer
#changes generation and legendary to test 1 and test 2 if total is greater than 500
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2'] 

df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False) #groups by type 1 and sorts by defense
df.groupby(['Type 1']).sum() #sums up all stats by type 1
df['count'] = 1 #adds count column
df.groupby(['Type 1']).count()['count'] #counts all types
df.groupby(['Type 1', 'Type 2']).count()['count'] #counts all types and type 2

for df in pd.read_csv('modified.csv', chunksize=5): #reads 5 rows at a time
    print("Chunk DF") #prints chunk df evry 5 rows
    print(df)

new_df = pd.DataFrame(columns=df.columns) #creates new dataframe
for df in pd.read_csv('modified.csv', chunksize=5): #reads 5 rows at a time
    results = df.groupby(['Type 1']).count() #counts all types
    new_df = pd.concat([new_df, results]) #adds results to new_df











##PANDASSSSSSSSSSSS





A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.
Return the result table in any order.

import pandas as pd
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
  
   df_new=world[(world['area']>=3000000) | (world['population']>=25000000)]
   result=df_new[['name', 'population', 'area']]
   return result


Write a solution to find the ids of products that are both low fat and recyclable.
Return the result table in any order.
The result format is in the following example.

import pandas as pd
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df_id=products[(products['low_fats']=='Y') & (products['recyclable'] == 'Y')]
    df_new=df_id[['product_id']]
    return df_new    


  
Write a solution to find all customers who never order anything.
Return the result table in any order.
The result format is in the following example.
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    #customers whose id is not in orders customerID
    df= customers[~customers['id'].isin(orders['customerId'])]
    #build dataframe of names rename Cusotmers
    df=df[['name']].rename(columns={'name':'Customers'})
    return df



Write a solution to find all the authors that viewed at least one of their own articles.
Return the result table sorted by id in ascending order.
The result format is in the following example.

import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ans= views[(views['author_id'] == views['viewer_id'])]
    ans1 = ans[['author_id']].rename(columns ={'author_id':'id'})
    ans1 = ans1.drop_duplicates()
    ans1 = ans1.sort_values(by=['id'],ascending=True)
    return ans1


Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
Return the result table in any order.
The result format is in the following example.
  
import pandas as pd
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df=tweets[tweets['content'].apply(len)>15][['tweet_id']]
    return df



Write a solution to calculate the bonus of each employee. 
The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'.
The bonus of an employee is 0 otherwise.
Return the result table ordered by employee_id.
The result format is in the followin example.

import pandas as pd
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees[(~employees['name'].str.startswith('M')) & (employees['employee_id'] % 2 == 1)]['salary']
    employees['bonus'] = employees.bonus.fillna(value=0)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')




Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
Return the result table ordered by user_id.
The result format is in the following example.

import pandas as pd
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name']=users['name'].str.capitalize()
    return users.sort_values('user_id')
    



Write a solution to find the users who have valid emails.
A valid e-mail has a prefix name and a domain where:
The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
The domain is '@leetcode.com'.
Return the result table in any order.
The result format is in the following example.

import pandas as pd
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

  pattern = r"^[A-Za-z][-._A-Za-z0-9]*@leetcode\.com$"
  filterr = users['mail'].str.match(pattern)
  df = users[filterr]
  return df



Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.
Return the result table in any order.
The result format is in the following example.


import pandas as pd
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
     result = patients[patients['conditions'].str.contains(r'\bDIAB1')]
     return result


Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
For Pandas users, please note that you are supposed to modify Person in place.
After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
The result format is in the following example.

import pandas as pd
# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', ascending=True, inplace=True)
    person.drop_duplicates(subset="email", keep="first", inplace=True)




Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
Return the result table in any order.
The result format is in the following example.
  
import pandas as pd
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
     # set product_id as the index, preparing for stacking stores
    products.set_index('product_id', inplace=True)
    # stack stores
    products = products.stack(dropna=True).reset_index()
    # rename columns
    products.columns = ['product_id','store','price']
    return pd.DataFrame(products)



Write a solution to calculate the total time in minutes spent by each employee on each day at the office.
Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.
Return the result table in any order.
The result format is in the following example.
  

import pandas as pd
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    #calculate time spent
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    #group by employee id event day and sum itemspent
    result = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()
    result.rename(columns={'event_day': 'day', 'time_spent': 'total_time'}, inplace=True)
    return result
    


Write a solution to find the first login date for each player.
Return the result table in any order.
The result format is in the following example.

 import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    #sort DataFrame by player_id event_date
    activity=activity.sort_values(by=['player_id', 'event_date'])
    #group by player_id select min event_date for each player
    result=activity.groupby('player_id')['event_date'].min().reset_index()
    result.rename(columns={'event_date': 'first_login'}, inplace=True)

    return result
  

Write a solution to calculate the number of unique subjects each teacher teaches in the university.
Return the result table in any order.
The result format is shown in the following example.

import pandas as pd
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Group by teacher_id and count the number of unique subject_ids
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    result.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return result

































    

                 
                 
