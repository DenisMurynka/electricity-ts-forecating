#add date column to 'row data' folder
import os
import pandas as pd
import xlrd
path = '/home/denis-root/Documents/data engineering projects/'
files = os.listdir(path)

for index,file in enumerate(files):

    if file =='1month.xlsx':
        workbook = xlrd.open_workbook('1month.xlsx', ignore_workbook_corruption=True)
        df = pd.read_excel(workbook,engine='xlrd')

        #df = pd.read_excel(path+'/'+file,engine='xlrd') #Read Excel file as a DataFrame
        df['newcol'] = df['datetimest']
        #df.drop(df.columns[0], axis=1)
        #To save it back as Excel
        df.to_excel('kek.xlsx',engine='xlsxwriter') #Write DateFrame back as Excel file

