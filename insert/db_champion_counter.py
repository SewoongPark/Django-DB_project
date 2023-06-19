import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

conn = pymysql.connect(host='127.0.0.1', user = 'root', password='admin1234', db = 'mydjango_project',charset = 'utf8') #본인 db password 입력, database 이름 입력 
curs = conn.cursor(pymysql.cursors.DictCursor)

chams_info = pd.read_csv(r"/Users/vvoo/mydjango_project_SW/lol_data/champion_counter.csv", index_col=False) #csv 파일 저장된 경로 
chams_info = chams_info.where((pd.notnull(chams_info)), 'N/A')
print(chams_info.head())

for index, row in chams_info.iterrows():
    tu = (row.counter_name, row.win, row.champion_id)   #db에 넣고자 하는 csv파일의 컬럼 입력 ex) rew.champion_id / 순서 상관 x
    curs.execute("""  INSERT IGNORE INTO mydjango_project.boards_champion_counter      
    (counter_name, win, champion_id) VALUES
    (%s, %s, %s)""", tu)   # INSERT IGNORE INTO project.board_champion_counter  //  (본인database 이름).(database내 table 이름)   
    # ( ) VALUES -> csv를 넣을 database table의 컬럼 입력. 순서는 table 컬럼 순서 맞춰서
    # id 컬럼은 models.py에서 따로지정해주지 않은 autofield primary_key 입력해주지 않아도 됨.

conn.commit()
conn.close()