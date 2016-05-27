""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model
from time import strftime

class ride(Model):
	def __init__(self):
		super(ride, self).__init__()


	def addrides(self, rides_info):
		query="INSERT INTO rides (ride_name, place, depart_time, open_seats, add_notes, user_id) VALUES(:ride_name, :place, :depart_time, :open_seats, :add_notes, :user_id)"
		data={
			'user_id': rides_info['id'],
			'ride_name':rides_info['ride_name'],
			'place':rides_info['place'],
			'depart_time':rides_info['depart_time'],
			'open_seats':rides_info['open_seats'],
			'add_notes':rides_info['add_notes']
		}
		return self.db.query_db(query,data)
	

	def allrides(self):
		query="SELECT id, ride_name, place, depart_time, open_seats, add_notes FROM rides"
		return self.db.query_db(query)

	def displayride(self, ride_id):
		query="SELECT id, ride_name, place, depart_time, open_seats, add_notes FROM rides WHERE id = :ride_id"
		data={
			'ride_id': ride_id,
		}
		return self.db.query_db(query,data)

	# # def test(self,id):
	# # 	query="SELECT rides.id, rides.open_seats, passengers.id, passengers.ride_id FROM rides LEFT JOIN passengers WHERE rides.id=passengers.ride_id"
	# # 	data={
	# # 	'id':id
	# # 	}

	# 	return self.db.query_db(query,data)
	def joinrides(self, join_info):
		query = "INSERT into passengers (passenger_name, phone_number, ride_id, user_id) VALUES(:passenger_name, :phone_number, :ride_id, :user_id)"
		data = {
			'user_id': join_info['user_id'],
			'passenger_name': join_info['passenger_name'],
			'phone_number': join_info['phone_number'], 
			'ride_id': join_info['ride_id']
		}
		return self.db.query_db(query, data)

	def passenger_list(self):
		query = "SELECT * FROM passengers"
		# data={
		# 	'ride_id': ride_id,
		# }
		return self.db.query_db(query)
