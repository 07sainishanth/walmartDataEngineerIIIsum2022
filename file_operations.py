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

	# print(data_dict)
	return data_dict

