# %%
import pandas as pd
import os

# %%
d = pd.DataFrame()
for file in os.listdir('./data'):
    if 'Uzavřeno' in file:
        fle = './data/' + file
        for sheet in pd.ExcelFile(fle).sheet_names:
            d = d.append(pd.read_excel(fle, sheet_name=sheet))

# %%
d.head()

# %%
holding = list(pd.read_excel('./data/Seznam firem_agrofert.xlsx')['IČO'].values)

# %%
holding

# %%
vyplaceno = d[d['IČO klienta'].isin(holding)]

# %%
vyplaceno.head()

# %%
vyplaceno.groupby('Klient')['Výše dotace'].sum().sort_values(ascending=False).to_excel('./smlouvy_holding.xlsx')

# %%
vyplaceno.groupby('Klient')['Výše dotace'].sum()

# %%
