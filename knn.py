import pandas as pd 
import math
from operator import itemgetter

def load_dataset(filename):
	datalist = []
	with open(filename,'r') as csvfile:
		reader = pd.read_csv(csvfile,skiprows=3)
		datalist = reader.values.tolist()
		for entry in datalist:
			entry.pop(0)	
		return datalist

def euclidean_distance(arr1,arr2):
	distance = 0
	for i in range(len(arr1)):
		distance += pow((arr1[i] - arr2[i]),2)
	return math.sqrt(distance)

def get_neighbors(trainingsSet,testSet,k):
	distances = []
	for m in range(len(trainingsSet)):
		dis = euclidean_distance(testSet,trainingsSet[m])
		distances.append((trainingSet[m],dis))
	distances.sort(key=itemgetter(1))
	neighbors = []
	for i in range(k):
		neighbors.append(distances[i][0])
	return neighbors

def get_votes(neighbors):
	votes = {}
	for i in xrange(len(neighbors)):
		vote = neighbors[i][-1]
		if vote in votes:
			votes[vote] += 1
		else:
			votes[vote] = 1
	votes = sorted(votes.items(), key = itemgetter(1) ,reverse = True)
	return votes[0][0]

 def main():
	filename = "weather_data.csv"
 	trainingsSet = load_dataset(filename)
 	testSet = []
 	testSet.append(raw_input("Enter the RH: "))
 	testSet.append(raw_input("Enter the Temperatur: "))
 	actual = raw_input("Exact class label: ")
	k = raw_input("Enter k: ")
	for x in xrange(len(testSet)):
 		neighbors  = get_neighbors(trainingsSet,testSet,k)
 		class_label = get_votes(neighbors)
 		print("Predicted: {}, actual: {}").format(class_label,actual)
 		print "\n"

if __name__ == "__main__":
	main()