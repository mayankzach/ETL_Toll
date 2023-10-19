from datetime import date
import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
class ETL:
    def __init__(self,plaza_id, sql_file_path, sql_table_name):
        self.plaza_id=plaza_id
        self.sql_file_path=sql_file_path
        self.sql_table_name=sql_table_name
        self.url="https://tis.nhai.gov.in/TollInformation.aspx?TollPlazaID="+str(plaza_id)
        self.soup=''
        self.df_info=pd.DataFrame()

    def extract(self):
        r=requests.get(self.url)
        self.soup=BeautifulSoup(r.text,'html.parser')
        if(self.soup.find(class_='PA15')):
            return True
        else:
            return False
    def transform(self):
        plaza_name=self.soup.find(class_='PA15').find_all('p')[0].find('lable')
        table=self.soup.find_all('table',class_='tollinfotbl')[0]
        x=str(table)
        df_info=pd.read_html(x)[0].dropna(axis=0,how='all')
        cols=list(df_info.columns)
        cols.insert(0,'Date Scraped')
        cols.insert(1,'Plaza Name')
        cols.insert(2,'Plaza Id')
        df_info['Date Scraped']=date.today()
        df_info['Plaza Id']=self.plaza_id
        df_info['Plaza Name']=plaza_name.text
        self.df_info=df_info[cols]
    def load(self):
        conn=sqlite3.connect(self.sql_file_path)
        self.df_info.to_sql(self.sql_table_name,conn,if_exists='append',index=False)
    def run_etl(self):
        if(self.extract()):
            self.transform()
            self.load()
            print(f'Done with ETL of plaza_id: {self.plaza_id}')
        else:
            print(f'Skipped plaza_id:{self.plaza_id}')