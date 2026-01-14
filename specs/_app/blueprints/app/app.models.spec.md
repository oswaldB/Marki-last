# Modèles : App (ST-001)
**Fichier cible** : `app/blueprints/app/models.py`

---

## **Modèles SQLAlchemy**

### 1. User
```python
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations
    notifications = db.relationship('Notification', backref='user', lazy=True)
    relances = db.relationship('Relance', backref='user', lazy=True)
```

### 2. Notification
```python
class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

---

## **Schémas Pydantic**

### 1. UserSchema
```python
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    is_admin: bool = False

    class Config:
        from_attributes = True
```

### 2. NotificationSchema
```python
class NotificationSchema(BaseModel):
    message: str
    is_read: bool = False

    class Config:
        from_attributes = True
