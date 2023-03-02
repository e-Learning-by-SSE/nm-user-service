from db import db
from models.entities import User
from typing import List


class UserRepo:
    
 def create(self,user):
    db.session.add(user)
    db.session.commit()
    
 def fetchById(self,_id)-> 'User':
     return db.session.query(User).filter_by(id=_id).first()
 
 def fetchAll(self) -> List['User']:
     return db.session.query(User).all()
 
 def delete(self,_id) -> None:
     item= db.session.query(User).filter_by(id=_id).first()
     db.session.delete(User)
     db.session.commit()
     
 def update(self,user_data):
    db.session.merge(user_data)
    db.session.commit()