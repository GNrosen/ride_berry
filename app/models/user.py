""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model

class user(Model):
	def __init__(self):
		super(user, self).__init__()


	def register(self, registration_info):
		regis_errors = []
		if not registration_info['first_name']:
			regis_errors.append('First Name cannot be blank')
		elif len(registration_info['first_name']) < 2:
			regis_errors.append('First Name must be at least 2 characters long')
		if not registration_info['last_name']:
			regis_errors.append('Last Name cannot be blank')
		elif len(registration_info['last_name']) < 2:
			regis_errors.append('Last Name must be at least 2 characters long')


		if not registration_info['phone_number']:
			regis_errors.append('Phone number cannot be blank')
		elif len(registration_info['phone_number']) != 11:
			regis_errors.append('Please enter a valid phone number with area code and no special characters')
		elif any(char.isalpha() for char in registration_info['phone_number']):
			regis_errors.append('Must be a valid phone number with area code')




		if not registration_info['password']:
			regis_errors.append('Password cannot be blank')
		elif len(registration_info['password'])< 8:
			regis_errors.append('Password must be at least 8 characters long')
		elif registration_info['password'] != registration_info['confirmpassword']:
			regis_errors.append('Password and confirmation must match.')

		if regis_errors:
			return{'status': False, 'regis_errors': regis_errors}

		else:

			password = registration_info['password']
			hashed_pw = self.bcrypt.generate_password_hash(password)
			query = "INSERT INTO users (first_name, last_name, phone_number, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :phone_number, :email, :password, NOW(), NOW())"
			data = {'first_name': registration_info['first_name'], 'last_name': registration_info['last_name'], 'phone_number':registration_info['phone_number'], 'email': registration_info['email'], 'password': hashed_pw}

			self.db.query_db(query, data)

			get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
			users = self.db.query_db(get_user_query)

			return{'status': True, 'user':users[0]}
	
	def login(self, login_info):
		login_errors = []
		if not login_info['emailcheck']:
			login_errors.append('username field cannot be blank')
		if not login_info['passwordcheck']:
			login_errors.append('password field cannot be blank')
		if login_errors:
			return {"status": False, "login_errors": login_errors}
		
		else:
			password = login_info['passwordcheck']
			query = "SELECT * FROM users WHERE email = :email LIMIT 1"
			data = {'email': login_info['emailcheck']}
			user = self.db.query_db(query, data)
			print user

			if user and self.bcrypt.check_password_hash(user[0]['password'], password):
			
				id = user[0]['id']
				first_name = user[0]['first_name']
				last_name = user[0]['last_name']
				
				return{'status': True, 'first_name': first_name, 'last_name': last_name, 'id': id}
				
			else:
				login_errors.append('Try logging in again')
				return {'status': False, 'login_errors': login_errors}
	def get_user(self,id):
		query="SELECT phone_number, venmo, fav_food FROM users WHERE id=:id"
		data={
		'id':id
		}
		return self.db.query_db(query,data)

	def update(self, update_info, id):
		query="UPDATE ride_berry.users SET venmo=:venmo, fav_food= :fav_food WHERE id=:id"
		data = {
			'id': id,
			'venmo': update_info['venmo'],
			'fav_food': update_info['fav_food']
			}

		return self.db.query_db(query, data)




