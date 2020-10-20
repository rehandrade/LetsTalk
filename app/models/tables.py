from app import db
import peewee as p
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel(p.Model):

  class Meta:
    database = db


class User(BaseModel):
	
	username = p.CharField(unique=True)
	email = p.CharField(unique=True)
	password = p.CharField()

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True
	
	@property
	def is_anonymous(self):
		return False
	
	def get_id(self):
		return str(self.id)
	
	def senha_criptografada(self, password):
		self.password = generate_password_hash(password, method='sha256')


	def senha_descriptografada(self, password):
		return check_password_hash(self.password, password)


class Post(BaseModel):

	about = p.TextField()
	user = p.ForeignKeyField(User, backref='posts')