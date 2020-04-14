import os
from pathlib import Path
import sklearn.datasets as skd

OUTPUT_PATH = Path('out')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)
TEST_PATH = Path('test')
TEST_PATH.mkdir(exist_ok=True, parents=True)

# TODO: Check if we want to use NLTK
def clean_text(s):
	r = s.replace('\n', ' ').lower().replace(',',' ').replace('  ', ' ')
	if r == '':
		r = ' '
	return r


a = skd.fetch_20newsgroups(data_home='.', remove=('headers'), random_state=0)
test = skd.fetch_20newsgroups(subset='test', data_home='.', remove=('headers'), random_state=0)

for x in zip(a.data, a.target, a.filenames):
	b = Path(x[2])
	t = clean_text(x[0])
	p = OUTPUT_PATH / b.name
	print(f"Writing to {p}")
	if len(t) == 0:
		print('Original text is', x[0])
		raise Exception('Empty string')
	with open(p, 'w') as f:
		f.write(t)

for x in zip(test.data, test.target, test.filenames):
	b = Path(x[2])
	t = clean_text(x[0])
	p = TEST_PATH / b.name
	print(f"Writing to {p}")
	if len(t) == 0:
		print('Original text is', x[0])
		raise Exception('Empty string')
	with open(p, 'w') as f:
		f.write(t)

