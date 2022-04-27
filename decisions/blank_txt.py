# running this script will blank all .txt files in the same directory.
from glob import glob
for filename in glob('*.txt'):
	with open(filename, 'w') as f:
		pass