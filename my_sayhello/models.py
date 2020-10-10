from datetime import datetime
from my_sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    #存储每一条留言的发表时间
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    