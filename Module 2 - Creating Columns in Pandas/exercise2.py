import pandas as pd
from IPython.core.display import display
from scipy.stats import zscore

# Begin assignment
df = pd.read_csv("http://data.heatonresearch.com/data/t81-558/datasets/reg-33-data.csv", na_values=['NA', '?'])

df.drop('id', 1, inplace=True)

# Your code goes here!

# Add a column named ratio that is max divided by number. Leave max and number in the dataframe
df['ratio'] = df['max'] / df['number']

# Replace the cat2 column with dummy variables. e.g. 'cat2_CA-0', 'cat2_CA-1'
dummiesC = pd.get_dummies(df['cat2'], prefix='cat2')

df = pd.concat([df, dummiesC], axis=1)

# drop remain column cat2 after insert the dummies
df.drop('cat2', axis=1, inplace=True)

# Replace the item column with dummy variables, e.g. 'item_IT-0', 'item_IT-1'
dummiesI = pd.get_dummies(df['item'], prefix='item')

# drop remain column item after insert the dummies
df.drop('item', axis=1, inplace=True)

# fill na items from lenght column with median
medianL = df['length'].median()
df['length'] = df['length'].fillna(medianL)

# fill na items from height column with median
medianH = df['height'].median()
df['height'] = df['height'].fillna(medianH)

# compute zscore to column height
df['height'] = zscore(df['height'])

df.drop(['convention', 'usage', 'weight', 'country', 'region', 'code', 'power', 'target'], 1, inplace=True)

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 0)

df = pd.concat([df, dummiesI], axis=1)

display(df)
