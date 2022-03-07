import os
import sys
import file_operations as fo
import algorithm as alg

output_file = "./output_1.txt"

def main():
	if len(sys.argv) < 1:
		print("In sufficient arguments")

	data_dict = fo.read_file(sys.argv[1])
	# print(data_dict)
	mta = alg.SeatAllocator(10,20)
	data_result = {}
	for key in data_dict.keys():
		data_result[key] = mta.allocate(data_dict[key])
		# print(key + " " + data_result[key])

	fo.save_file(output_file, data_result)
	print(os.path.abspath(output_file))


if __name__=="__main__":
    main()