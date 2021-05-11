import pandas as pd

df = pd.read_excel('Donnees.xlsx')


dfenc = df.loc[(df['Vitamine A (µg)']==770) & (df['Vitamine B1 (mg)'] <= 3) & (df['Vitamine B2 (mg)'] == 4.2) & (df['Vitamine B12 (µg)'] <= 5) & (df['Vitamine B6 (mg)'] <= 5) & (df['Vitamine B12 (µg)'] == 4.5) & (df['Vitamine C (mg)'] == 170) & (df['Vitamine D3 (µg)'] == 4) & (df['Vitamine E (mg)'] <= 12) & (df['Vitamine E (mg)'] > 9) & (df['Vitamine K (µg)'] == 25) & (df['Vitamine H (mg)'] == 0.45) & (df['Acide folique (mg)'] == 0.6) & (df['Nicotinamide  (mg)'] == 0) & (df['Acide pantothénique (mg)'] <= 10) & (df['Acide pantothénique (mg)'] >5) & (df['Fer (mg)'] == 10) & (df['Fluor (mg)'] == 3.5) & (df['Iode (µg)'] <= 150) & (df['Iode (µg)'] > 100) & (df['Calcium (mg)'] <= 1300) & (df['Calcium (mg)'] > 1000) & (df['Cuivre (mg)'] <= 3) & (df['Cuivre (mg)'] > 1.5) & (df['Magnésium (mg)'] == 400) & (df['Manganèse (mg)'] <= 5) & (df['Manganèse (mg)'] > 4) & (df['Phosphore (mg)'] == 700) & (df['Sélénium (µg)'] <= 70) & (df['Sélénium (µg)'] >60) & (df['Zinc (mg)'] == 11),:]

dataenctoex = pd.ExcelWriter("SolPrFemmeEnc.xlsx",engine = 'xlsxwriter')
dfenc.to_excel(dataenctoex,sheet_name = 'Feuil1' )
dataenctoex.save()