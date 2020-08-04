# %%
import requests
import pandas as pd
import math
from hlidac_token import token

# %%
holding = list(pd.read_excel('./data/Seznam firem_agrofert.xlsx')['IČO'].values)

# %%
contracts = []
hdrs = {'Authorization': 'Token ' + token}

#%%
for ic in holding:
    r = requests.get('https://www.hlidacstatu.cz/api/v2/smlouvy/hledat?strana=1&razeni=1&dotaz=icoPlatce:49241494 icoPrijemce:' + str(ic), headers=hdrs).json()
    if 'Results' in r:
        contracts.extend(r['Results'])

    # strankovani
    for page in range(2, math.ceil(r['Total'] / 25) + 1):
        r = requests.get('https://www.hlidacstatu.cz/api/v2/smlouvy/hledat?strana=' + str(page) +'&razeni=1&dotaz=icoPlatce:49241494 icoPrijemce:' + str(ic), headers=hdrs).json()
        if 'Results' in r:
            contracts.extend(r['Results'])

# %%
def get_details(contract):
    return {
        'id': contract['Id'],
        'datumUzavreni': contract['datumUzavreni'],
        'url': contract['odkaz'],
        'prijemce': contract['Prijemce'][0]['nazev'],
        'ico': contract['Prijemce'][0]['ico'],
        'predmet': contract['predmet'],
        'cena_dph': contract['CalculatedPriceWithVATinCZK'],
    }

# %%
d = pd.DataFrame.from_dict(list(map(get_details, contracts)))

# %%
d.drop_duplicates(subset=['url'], inplace=True)

# %%
d.to_excel('smlouvy_holding_registr.xlsx', index=False)