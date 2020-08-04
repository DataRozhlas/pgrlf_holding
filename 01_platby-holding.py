# %%
import pandas as pd

# %%
fle = './data/vyplaty na smlouvach_2017_2018_2019.xlsx'

# %%
d = pd.DataFrame()
for sheet in pd.ExcelFile(fle).sheet_names:
    d = d.append(pd.read_excel(fle, sheet_name=sheet))

# %%
d.head()

# %%
holding = list(pd.read_excel('./data/Seznam firem_agrofert.xlsx')['IČO'].values)

# %%
holding

# %%
vyplaceno = d[d['IČO'].isin(holding)]

# %%
vyplaceno.groupby('Klient').sum().sort_values(by='částka', ascending=False).to_excel('./vyplaceno_holding.xlsx')

# %%
