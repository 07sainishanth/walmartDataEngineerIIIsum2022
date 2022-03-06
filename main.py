import os
import sys
import file_operations as fo
import algorithm as alg

data_dict = fo.read_file("./input.txt")
print(data_dict)

alg.algo(data_dict)



fo.save_file("./output.txt", data_dict)