import pandas as pd
excel_file_path ='weather_data.xlsx'
df = pd.read_excel(excel_file_path)
grouped = df.groupby('Pincode')
for pincode,group in grouped:
    txt_file = f'{pincode}.txt'
    with open(txt_file,'w') as file:
     file.write(group.to_string(index=False))
