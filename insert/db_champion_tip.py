import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

conn = pymysql.connect(host='127.0.0.1', user = 'root', password='admin1234', db = 'mydjango_project',charset = 'utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

chams_info = pd.read_csv(r"/Users/vvoo/mydjango_project_SW/lol_data/champion_tip.csv", index_col=False)
chams_info = chams_info.where((pd.notnull(chams_info)), 'N/A')
print(chams_info.head())

for index, row in chams_info.iterrows():
    tu = (row.image_url, row.enemy_tips, row.ally_tips, row.champion_id)
    curs.execute("""  INSERT IGNORE INTO mydjango_project.boards_champion_tip
    (image_url, enemy_tips, ally_tips, champion_id) VALUES
    (%s, %s, %s, %s)""", tu)

conn.commit()
conn.close()