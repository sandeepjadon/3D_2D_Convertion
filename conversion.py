import argparse
import csv

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, required=True, help='input file')
	parser.add_argument('--output', type=str, required=True, help='output file')

	args = parser.parse_args()
	infile = args.input
	outfile = args.output

	file = open(outfile, "w")

	with open(infile, "r") as f:
			reader = csv.reader(f, delimiter=',')
			for i, line in enumerate(reader):
				if(i%2==0):
					x = line[0]
					y = line[2]
					z = line[4]
					u = (float(x)*1045.640667/float(z)) + 989.3053162
					v = (float(y)*-1073.818121/float(z)) + 555.9211734
					file.write(x+","+y+","+z+","+str(u)+","+str(v))
					file.write("\n")
	print('output File created')

