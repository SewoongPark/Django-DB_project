import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

conn = pymysql.connect(host='127.0.0.1', user = 'root', password='qwer1234', db = 'project',charset = 'utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

chams_info = pd.read_csv(r"C:\Users\efkje\OneDrive\바탕 화면\project\data\champion_skill_img_text.csv", index_col=False)
chams_info = chams_info.where((pd.notnull(chams_info)), 'N/A')
print(chams_info.head())

for index, row in chams_info.iterrows():
    tu = (row.cham_img, row.passive_img, row.q_img, row.w_img, row.e_img, row.r_img, row.passive, row.Q, row.W, row.E, row.R, row.champion_id)
    curs.execute("""  INSERT IGNORE INTO project.board_champion_skill_img_text
    (cham_img, passive_img, q_img, w_img, e_img, r_img, passive, Q, W, E, R, champion_id) VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tu)

conn.commit()
conn.close()