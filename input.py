###############################################
# LIBRAIRES NECESSAIRES
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pySankey.sankey import sankey

from matplotlib import font_manager
###############################################
# Display precisions
title = input("Entrez le titre du diagramme.")
nombre_offre = input("Rentrez le nombre d'offre.")
nombre_offre = int(nombre_offre) + 1

##############################################
# Importation of csv file with all data needed

df = pd.read_csv('data_input.csv', sep=';')

##############################################
# Reorganizing data
# Obtaining a table with number of cell lines = number of link lines

links = df.melt(id_vars = 'Coûts').rename(columns = {'Coûts' : 'source',
                                                     'variable' : 'target',
                                                     'value': 'value'})


##############################################
# Verify that the sum of each cost is 100
lst = df.columns.to_list()
del lst[0]
for i in range(len(lst)):
    if df[lst[i]].sum() == 100:
        print(f"La somme des coûts de l'offre {lst[i]} est égale à 100.")
        
    else:
            print(f" La somme des coûts de l'offre {lst[i]} n'est pas égale à 100.")


##############################################
# Dictonnary of colors considering the number of offers
liste_offre = [a for a in range(int(nombre_offre))]

colorDict =  colorDict = {
    'Taxes environnementales':'#FF9603',
    'Matières premières minérales':'#D67E03',
    'Matières premières agricoles':'#0284D6',
    'Transport':'#005488',
    'Energie':'#8A5101',
    'Eau' : '#99d0f2',
    'Coûts stables vis-à-vis du climat':'#d4d4d4'}

for letter in liste_offre: 
    colorDict.update({ 
        f'Offre {letter}': '#666666'
    })

#############################################
# Loading Sankey Diagram

sankey(left = links['source'], right =  links['target'], leftWeight = links['value'],
      colorDict = colorDict, fontsize = 10)


#############################################
# Font management

font_path = 'C:\\Windows\\Fonts\\FontFont - Daxline Offc Light.ttf' 
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = prop.get_name()

#############################################

plt.title(label = title,
          loc = 'center',
          fontsize = 30,
          pad = 20,
         fontname = prop.get_name())


fig = plt.gcf()

fig.set_facecolor("w")

fig.savefig("output.svg", bbox_inches ='tight', dpi=150)

##############################################