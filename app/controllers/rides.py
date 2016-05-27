"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *
from twilio.rest import TwilioRestClient

class rides(Controller):
	def __init__(self, action):
		super(rides, self).__init__(action)
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
   
	def creategroup(self):

		return self.load_view('rides/creategroup.html')

	def riders(self):

		return redirect()

	def grouppage(self):
		allrides=self.models['ride'].allrides()
		# ride_id = allrides[0]['id']
		# one_ride = self.models['ride'].displayride()


		
		
		# open_seats = allrides[0]['open_seats']
		passenger_list = self.models['ride'].passenger_list()

		# length = len(passenger_list)
		# seats_left = open_seats - length 


		return self.load_view('rides/grouppage.html', allrides=allrides, passenger_list = passenger_list)

	def createride(self):

		return self.load_view('rides/createrequestride.html')


	def addrides(self, id):
		one_user = self.models['user'].get_user(id)

		
		
		rides_info={
			'id':id,
			'ride_name':request.form['ride_name'],
			'place':request.form['place'],
			'depart_time':request.form['depart_time'],
			'open_seats':request.form['open_seats'],
			'add_notes':request.form['add_notes']
		}
		account_sid = "AC3047e8e0939df384b9cd10305b411bf9" # Your Account SID from www.twilio.com/console
		auth_token  = "a8bc2dfa0f4ed94815dd646bd466caab"  # Your Auth Token from www.twilio.com/console

		client = TwilioRestClient(account_sid, auth_token)

		message = client.messages.create(body="Your ride has been created! You are heading to " + rides_info['place'] + " at " + rides_info['depart_time'],
			to=one_user[0]['phone_number'],    # Replace with your phone number
			from_="+16504828349") # Replace with your Twilio number
		self.models['ride'].addrides(rides_info)
		return redirect('/grouppage')

	def joinrides(self,id):
		# allrides=self.models['ride'].allrides()
		one_ride=self.models['ride'].displayride(id)

		join_info = {
			'user_id':session['id'],
			'passenger_name':request.form['passenger_name'],
			'phone_number': request.form['phone_number'],
			'ride_id': one_ride[0]['id']
		}

		account_sid = "AC3047e8e0939df384b9cd10305b411bf9" # Your Account SID from www.twilio.com/console
		auth_token  = "a8bc2dfa0f4ed94815dd646bd466caab"  # Your Auth Token from www.twilio.com/console

		client = TwilioRestClient(account_sid, auth_token)

		message = client.messages.create(body="You have joined " + one_ride[0]['ride_name'] + "! You are heading to " + one_ride[0]['place'] + " at " + one_ride[0]['depart_time'],
			to=join_info['phone_number'],    # Replace with your phone number
			from_="+16504828349") # Replace with your Twilio number

		self.models['ride'].joinrides(join_info)
		return redirect('/grouppage')

	def passenger_list(self):

		allrides=self.models['ride'].allrides()
		# ride_test = allrides[0]['id']
		# self.models['ride'].passenger_list(ride_test)
		return redirect('/grouppage')


