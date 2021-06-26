import sqlite3
import random
import datetime

class verb:
        def __init__(self,*data):
                self.id               = data[0] if len(data)>=1 else ""
                self.ru_verb          = data[1] if len(data)>=2 else ""
                self.ru_complete_verb = data[2] if len(data)>=3 else ""
                self.en_complete_verb = data[3] if len(data)>=4 else ""
                self.point            = data[4] if len(data)>=5 else ""
                self.last_date        = data[5] if len(data)>=6 else ""
                if not data:
                        self.get()

        def get(self):
                con = sqlite3.connect("verbs.db")
                cur = con.cursor()
                sql = """
                        select * from verbs where 
                        (((point/100)*100)+100)>point and 
                        cast(julianday('now')-julianday(last_time) as INTEGER)>=6 
                        limit 5
                      """
                try:
                        data = cur.execute(sql).fetchall()
                        con.commit()
                        index = random.randint(0,len(data)-1)
                        data = data[index]
                        self.id               = data[0]
                        self.ru_verb          = data[1]
                        self.ru_complete_verb = data[2]
                        self.en_complete_verb = data[3]
                        self.point            = data[4]
                        self.last_date        = data[5]
                except :pass
                finally:     
                        cur.close()
                        con.close()

                return self
        def update(self):
                sql =  f"""update verbs set ru_verb='{self.ru_verb}',
                                       ru_verb_complete='{self.ru_complete_verb}',
                                       en_verb_complete='{self.en_complete_verb}',
                                       point='{self.point}',
                                       last_time='{str(datetime.datetime.now())[:10]}' 
                                       where id='{self.id}'
                        """
                con = sqlite3.connect("verbs.db")
                cur = con.cursor()
                try:
                        data = cur.execute(sql)
                        con.commit()
                finally:        
                        cur.close()
                        con.close()