import pandas
from pandas import read_csv
import numpy

comment = """

# Create Date 2020-12-23 WCB 
# Requirement - Load stock data CSV into Pandas data frame and clean up strange formatting

# https://www.geeksforgeeks.org/change-data-type-for-one-or-more-columns-in-pandas-dataframe/
# https://datascienceplus.com/cleaning-modifying-a-dataframe-python/
# https://datatofish.com/replace-character-pandas-dataframe/

"""

df = read_csv("hcac.csv")
print(df.count())
print("The column headers :")
print(list(df.columns.values))

# selection = df.loc['0']
# print(selection)

print(df.isnull().all())
print(df.isnull().sum())
#print(df['0'].unique())

print(df.head(1))


comment = """
colors = {'first_set':  ['aa_bb','cc_dd','ee_ff','gg_hh'],
          'second_set': ['','','','']
         }

df = pandas.DataFrame(colors, columns= ['first_set','second_set'])

"""

string = r'\\r\''

df = df.replace('b','', regex=True)
df = df.replace(string, regex=True)

print(df['0'].unique())
print (df)

