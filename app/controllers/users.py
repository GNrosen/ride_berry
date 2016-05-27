"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *


class users(Controller):
	def __init__(self, action):
		super(users, self).__init__(action)
		"""
			This is an example of loading a model.
			Every controller has access to the load_model method.
		"""
		self.load_model('user')
		self.load_model('ride')
		self.db = self._app.db

		"""
		
		This is an example of a controller method that will load a view for the client 

		"""
   
	def index(self):


		return self.load_view('users/welcome.html')

	def logout(self):

		session.clear()

		return redirect('/')

	def profile(self, id):

		# all_groups = self.models['ride'].getgroups()
		# print all_groups
		one_user = self.models['user'].get_user(id)
		return self.load_view('users/profile.html', one_user = one_user)


	def update_display(self):

		return self.load_view('users/updateinfo.html')

	def register(self):
		registration_info = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'phone_number': request.form['phone_number'],
			'email': request.form['email'],
			'password': request.form['password'],
			'confirmpassword': request.form['confirmpassword']
			}

		create_user = self.models['user'].register(registration_info)
		
		if create_user ['status'] == True:
			if 'id' not in session:
				session['id'] = create_user['user']['id'] 
			if 'first_name' not in session:
				session['first_name'] = create_user['user']['first_name']
			if 'last_name' not in session:
				session['last_name'] = create_user['user']['last_name']


			url = 'profile/'+ str(session['id'])
			return redirect(url)

		else:
			for message in create_user['regis_errors']:
				flash(message, 'regis_errors')
			return redirect('/#register')

	def login(self):

		login_info = {
			'emailcheck': request.form['emailcheck'], 
			'passwordcheck': request.form['passwordcheck']
		}

		login_user = self.models['user'].login(login_info)
		if login_user['status'] == True:
			session['first_name'] = login_user['first_name']
			session['last_name'] = login_user['last_name']
			session['id'] = login_user['id']
			url = 'profile/'+ str(session['id'])

			return redirect(url)
		else:
			if login_user['status'] == False:
				for message in login_user['login_errors']:
					flash(message, 'login_errors')
				return redirect('/')

	def update(self, id):
		
		update_info ={
			'venmo': request.form['venmo'],
			'fav_food': request.form['fav_food']
			}

		self.models['user'].update(update_info, id)
		url = 'profile/'+ str(session['id'])
		return redirect(url)





