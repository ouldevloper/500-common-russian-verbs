import sqlite3
import random
def get():
        con = sqlite3.connect("verbs.db")
        cur = con.cursor()
        sql = "select id,en_verb_complete from verbs"
        try:
                data = cur.execute(sql).fetchall()
                con.commit()
                for item in data:
                        id = item[0]
                        verb = ",".join([x.replace("to ","").strip(" ") for x in item[1].split(',')  if x.strip(" ").startswith("to ")])
                        print(verb,end="")
                        sql = f"update verbs set en_verb_complete='{verb}' where id ='{id}'"
                        data = cur.execute(sql)
                        con.commit()
        except sqlite3.Error:
                print("Error")   
        cur.close()
        con.close()

get()