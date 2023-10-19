from fetch_ids import fetch_id
import ETL_class
from datetime import date
from time import time
import concurrent.futures
from functools import partial

def start(plaza_id,db_file_path,db_table_name):
    plaza_etl=ETL_class.ETL(plaza_id,db_file_path,db_table_name)
    plaza_etl.run_etl()
if __name__=="__main__":
    i=time()
    db_file="nhai_inf.sqlite"
    db_table="nhai_toll_info"
    ids=fetch_id()
    partial_func=partial(start,db_file_path=db_file,db_table_name=db_table)
    with concurrent.futures.ThreadPoolExecutor(4) as executor:
        executor.map(partial_func,ids)
    print("Total time: ",time()-i)