import pandas as pd;
import requests;
import json;
from PP import ValorDoral;
import xlsxwriter;
i=0
Frame = {"Titulo":[],"Precio(USD$)":[],"Precio(ARS$)":[],"Link":[]}
while i <5*50:
    url = f"https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&offset={i}"
    response = requests.get(url)
    if response.ok:
        datos = response.json()
        results = datos["results"]
        for R in results:
            location = R["location"]
            Divisa = R["currency_id"]
            Link = R["permalink"]
            city = location["city"]
            name = city["name"]
            if name == "Rosario":
                title = R["title"]
                price = R["price"]
                if Divisa == "USD":
                    J = ValorDoral(int(price))
                    for F in Frame:
                        Fis = Frame[F]
                        if F == "Titulo":
                            Fis.append(title)
                        elif F == "Precio(USD$)":
                            Fis.append(price)
                        elif F == "Precio(ARS$)":
                            Fis.append(J)
                        elif F == "Link":
                            Fis.append(Link)
                else:
                    J = ValorDoral(int(price))
                    for F in Frame:
                        Fis = Frame[F]
                        if F == "Titulo":
                            Fis.append(title)
                        elif F == "Precio(USD$)":
                            Fis.append(0)
                        elif F == "Precio(ARS$)":
                            Fis.append(price)
                        elif F == "Link":
                            Fis.append(Link)
    i+=50

df = pd.DataFrame(Frame)
archivo_excel = 'ejemplo.xlsx'
writer = pd.ExcelWriter(archivo_excel, engine='xlsxwriter')
df.to_excel(writer, index=False, sheet_name='Hoja1')
workbook  = writer.book
worksheet = writer.sheets['Hoja1']
worksheet.set_column('A:A', 54)
worksheet.set_column('B:B', 12)
worksheet.set_column('C:C', 12)
worksheet.set_column('D:D', 120)
writer.close()