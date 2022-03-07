import os
import sys



class SeatAllocator(object):
	"""docstring for SeatAllocator"""
	def __init__(self, rows, columns):
		super(SeatAllocator, self).__init__()
		self.rows = rows
		self.columns = columns
		self.availableSeats = rows*columns
		self.seats = []
		for i in range(rows):
			row_s = []
			for j in range(columns):
				row_s.append(chr(i+65) + str(j+1))
			self.seats.append(row_s)

		# print(self.seats)
		


	def allocate(self, data):

		# Verfication of valid request
		if data <= 0:
			return "Invalid no of seats requested"
		elif data > self.availableSeats:
			return "cannot process request due to Insufficient seats"
		

		
		# If valid decreasing seats avaialbility
		result = ""
		while data > self.columns:
			result = result +"," + self.allocate_recur(self.columns)
			data -= self.columns

		if (data > 0):
			result = result +"," + self.allocate_recur(data)

		return result[1:]
		# print(self.seats[-1*i])
		# print(data)
		# print(self.availableSeats, "  ", data)


		

	def allocate_recur(self, data):

		i = 1

		# Veriying if available in same row
		while i < len(self.seats)+1:
			if len(self.seats[-1*i]) > data+3:
				break
			i+= 1

		self.availableSeats -= data
		# If not available making distributed allocation 
		if(i == len(self.seats)+1):
			# print("da")
			# Distributed allocation
			k = -1
			ret = ""
			while data > 0 and k*-1 < len(self.seats)+1:
				if(len(self.seats[k]) > 3):
					self.seats[k].pop()
					self.seats[k].pop()
					self.seats[k].pop()
					# while data > 0 and 
					self.availableSeats -= 3
					ret = ret + self.seats[k].pop() + ","
					data -= 1
				else:
					k -= 1

			return ret[:-1]
		else :
			# If available allocating seats in the row
			ret = ""
			self.availableSeats -= 3
			self.seats[-1*i].pop()
			self.seats[-1*i].pop()
			self.seats[-1*i].pop()
			while data > 0:
				data -= 1
				ret = ret+self.seats[-1*i].pop()+","

			return ret[:-1]
