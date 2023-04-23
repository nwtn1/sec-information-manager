from datetime import datetime
from sql_alchemy import db

class DatabaseModel(db.Model):
  __tablename__ = "historic"

  id = db.Column(db.Integer, primary_key=True)
  target = db.Column(db.String())
  token = db.Column(db.String())
  savedAt = db.Column(db.DateTime, nullable=False, default=datetime.now)

  def __init__(self, target: str, token: str):
    self.target = target
    self.token = token
  
  def as_json(self):
    return {
      "id": self.id,
      "target": self.target,
      "token": self.token,
      "savedAt": str(self.savedAt)
    }
  
  @classmethod
  def find_all(self):    
    return self.query.all()
  
  def save(self):
    db.session.add(self)
    db.session.commit()


