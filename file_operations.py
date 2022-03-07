import os
import sys


def read_file(file_path):
	# Reads through a each line of file and creates a dictionary 
	# containing reservation number as keys and number of seats requested as value
	f = open(file_path, "r")
	data = f.read()
	data_lines = data.split("\n")
	data_dict = {}
	for line in data_lines:
		temp = line.split(" ")
		try:
			data_dict[temp[0]] = int(temp[1])
		except Exception as e:
			data_dict[temp[0]] = 0
		

	f.close()
	# print(data_dict)
	return data_dict



def save_file(file_path, data):
	# {"Roo1": "E1,E2,E3", --}
	result = []
	# Saves the given data into file :
	# Parses each key value pair into single line string
	for key in data.keys():
		# dat = key + " "
		# for seat in data[key]:
		# 	dat = dat + seat + ","

		# dat = dat[:-1]
		result.append(key + "	" + data[key])

	f = open(file_path, "w")
	f.write('\n'.join(result))
	f.close()