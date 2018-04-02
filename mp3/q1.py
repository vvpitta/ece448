import math

Matrix=[] # likelyhood matrix
Freq=[]
laplace=1 #laplace
V=3
_lines=28

#
#returns array of frequencies of the numbers
#
def frequencies(values):
	ret_val= [0]*10
	for value in values:
		ret_val[int(value)]+=1

	return ret_val


#
#reads the files with the images of text
#returns  a list will all the images as given to us
def read_images(filename):
	#ret val
	global _lines
	images=[]
	file = open(filename, "r")
	ctr = 0
	curr_image=[]


	for line in file:
		# 28 lines per digit
		if ctr == _lines :
			ctr = 0
			images.append(curr_image)
			curr_image=[]

		ctr+=1

		curr_image.append(list(line))

	images.append(curr_image)
	return images
#
# returns values that are stored in file
#
def read_vals(filename):
	values=[]
	with open(filename, 'r') as file:
		for line in file:
			values.append(list(line)[0])

	return values


#genearing licklyhood matrix
def genMatrix( images , values , freq ):
	#will be 3 D
	matrix=[]
	global V
	global laplace

	for number in range(10):
		count = freq[number]

		row=[]
		for i in range(0,28):
			col=[0.0]*28
			for j in range(0,28):
				ctr = 0.0

				for k in range(5000):
					if int(values[k]) == number and images[k][i][j] =='+':
						ctr+=0.33
					elif int(values[k]) == number and images[k][i][j] =='#':
						ctr+=1
				#adjut laplace value
				col[j]=max(( (float(ctr+laplace))/ float(count+V*laplace)),0.000000001)# to stop math error while taking log
			row.append(col)

		matrix.append(row)

	return matrix

def getMax(poss):
	return poss.index(max(poss))


def train():
	global Freq
	global Matrix
	print ('--------------TRAINING---------------')

	images =  read_images('trainingimages')
	values = read_vals('traininglabels')

	Freq = frequencies(values)
	print(len(images), len(values))
	Matrix = genMatrix(images, values, Freq)

def test():
	global Freq
	global Matrix

	print ('--------------TESTING---------------')

	mat_len= len(Matrix)
	print(mat_len)
	testImages = read_images('testimages')
	testVals = read_vals("testlabels")





	test_results = []
	i=0
	poss=[]



	for curr_image in testImages:
		poss=[0.0]*mat_len

		for digit in range(mat_len):
			im_=0
			temp=0

			result=0.0


			for i in range(28):
				for j in range(28):
					if curr_image[i][j]== "+":
						result += 0.33* math.log(Matrix[digit][i][j])
					elif curr_image[i][j]== '#':
						result += math.log(Matrix[digit][i][j])
					else:
						result += math.log(1-Matrix[digit][i][j])

			poss[digit]=(result)
		test_results.append(getMax(poss))


	print(len(test_results))

	ctr=0
	d=open("results_max.txt", 'w+')
	fr=[0]*10
	suc=[0]*10

	idx_min=[0]*10
	idx_values=[-99999999.0 for i in range(10)]
	for idx in range(len(test_results)):
		x=int(test_results[idx])
		if int(test_results[idx]) == int(testVals[idx]):
			result=8.0
			for i in range(28):
				for j in range(28):
					if testImages[idx][i][j]== "+":
						result += 0.33*math.log(Matrix[digit][i][j])
					elif testImages[idx][i][j]== '#':
						result += math.log(Matrix[digit][i][j])
					else:
						result += math.log(1-Matrix[digit][i][j])
			if idx_values[x] < result:
				#print("here")
				idx_min[x]=idx
				idx_values[x]=result

	d.write("Image for 0\n")
	for m in range(10):
		for i in range(28):
			for j in range(28):
				d.write(testImages[idx_min[m]][i][j])
			d.write("\n")
		d.write(str(idx_min[m]))
		d.write("-----------------\n")
	d.close()









'''
	d.write("Total Successes:\t"+str(ctr))
	d.write("\nPercent:\t"+str(float(ctr)/10))
	d.write("\n")
	for idx in range(10):
		d.write(str(idx)+ " Accuracy: "+ str(float(suc[idx])/fr[idx]))
		d.write("\n")'''

	#get_conf(test_results , testVals)



def get_conf(results, actual):
	conf=[[0 for x in range(10)] for y in range(10)]
	for i in range(len(results)):
		#if int(results[i]) != int(actual[i]):
		conf[int(results[i])][int(actual[i])] +=1
	print(conf)

	for i in range(10):
		print(conf[i])

	return conf






def main():
	train()
	test()

if __name__== '__main_':
	main()
