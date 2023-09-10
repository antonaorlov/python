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

                 
                 