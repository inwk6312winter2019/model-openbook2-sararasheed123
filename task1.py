import CSV
def easy():

	With open(‘Street_Centrelines.csv’, ‘rb’) as f:
	reader = csv.reader(f)
	for row in reader:
	data=('STR_NAME'),('FULL_NAME'),('FROM_STR,TO_STR')
	csv_out=csv.writer(out)
	for row in data:
        csv_out.writerow(row)
easy()
