import pandas as pd

df = pd.read_excel('Donnees.xlsx')


dfret = df.loc[(df['Vitamine A (µg)']<=900) & (df['Vitamine A (µg)']>700) & (df['Vitamine B1 (mg)'] <= 5) & (df['Vitamine B1 (mg)'] > 2) & (df['Vitamine B2 (mg)'] <= 6) & (df['Vitamine B2 (mg)'] > 3) & (df['Vitamine B12 (µg)'] <= 6) & (df['Vitamine B12 (µg)'] >2) & (df['Vitamine B6 (mg)'] <= 8) & (df['Vitamine B6 (mg)'] > 3) & (df['Vitamine C (mg)'] <= 240) & (df['Vitamine C (mg)'] > 120 ) & (df['Vitamine D3 (µg)'] <= 6) & (df['Vitamine D3 (µg)'] > 3) & (df['Vitamine E (mg)'] <= 15) & (df['Vitamine E (mg)'] > 7) &  (df['Vitamine K (µg)'] <= 34) & (df['Vitamine K (µg)'] > 23) & (df['Vitamine H (mg)'] <= 1) & (df['Vitamine H (mg)'] > 0) &(df['Acide folique (mg)'] <= 1) & (df['Acide folique (mg)'] > 0) & (df['Nicotinamide  (mg)'] <= 14)& (df['Nicotinamide  (mg)'] > 11) & (df['Acide pantothénique (mg)'] == 5) & (df['Fer (mg)'] == 9) & (df['Fluor (mg)'] == 3.5) & (df['Iode (µg)'] == 150) & (df['Calcium (mg)'] <= 1200) & (df['Calcium (mg)'] > 1000) & (df['Cuivre (mg)'] <= 3) & (df['Cuivre (mg)'] > 1.5) & (df['Magnésium (mg)'] <= 420) & (df['Magnésium (mg)'] > 320) & (df['Manganèse (mg)'] <= 5) & (df['Manganèse (mg)'] > 2) & (df['Phosphore (mg)'] == 700) & (df['Sélénium (µg)'] == 55) & (df['Zinc (mg)'] <= 11) & (df['Zinc (mg)'] > 8),:]

dataenctoex = pd.ExcelWriter("SolRetenues.xlsx",engine = 'xlsxwriter')
dfret.to_excel(dataenctoex,sheet_name = 'Feuil1' )
dataenctoex.save()