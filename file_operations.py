import os
import sys


def read_file(file_path):
	f = open(file_path, "r")
	data = f.read()
	data_lines = data.split("\n")
	data_dict = {}
	for line in data_lines:
		temp = line.split(" ")
		data_dict[temp[0]] = temp[1]

	f.close()
	# print(data_dict)
	return data_dict



def save_file(file_path, data):
	result = []
	for key in data.keys():
		dat = key + " "
		for seat in data[key]:
			dat = dat + seat + ","

		dat = dat[:-1]
		result.append(dat)

	f = open(file_path, "w")
	f.write('\n'.join(result))
	f.close