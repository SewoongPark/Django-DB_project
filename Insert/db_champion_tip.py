import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
import csv
sns.set()


conn = pymysql.connect(host='127.0.0.1', user = 'root', password='qwer1234', db = 'project',charset = 'utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

chams_info = pd.read_csv(r"C:\Users\efkje\OneDrive\바탕 화면\project\data\champion_tip.csv", index_col=False)
chams_info = chams_info.where((pd.notnull(chams_info)), 'N/A')
print(chams_info.head())

for index, row in chams_info.iterrows():
    tu = (row.image_url, row.enemy_tips, row.ally_tips, row.champion_id)
    curs.execute("""  INSERT IGNORE INTO project.board_champion_tip
    (image_url, enemy_tips, ally_tips, champion_id) VALUES
    (%s, %s, %s, %s)""", tu)

conn.commit()
conn.close()
