import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

conn = pymysql.connect(host='127.0.0.1', user = 'root', password='qwer1234', db = 'project',charset = 'utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

chams_info = pd.read_csv(r"C:\Users\efkje\OneDrive\바탕 화면\project\data\champion_line_position_cc.csv", index_col=False)
chams_info = chams_info.where((pd.notnull(chams_info)), 'N/A')
print(chams_info.head())

for index, row in chams_info.iterrows():
    tu = (row.champion, row.line, row.position, row.CC)
    curs.execute("""  INSERT IGNORE INTO project.board_champions
    (champion, line, position, CC) VALUES
    (%s, %s, %s, %s)""", tu)

conn.commit()
conn.close()