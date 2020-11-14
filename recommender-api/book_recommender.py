import numpy as np
import pandas as pd
from scipy.sparse import load_npz
from sklearn.neighbors import NearestNeighbors
import pickle
class recommenderCollaborativeFiltering():
	def loadSparseMatrix(self):
		return load_npz('data/user_item_matrix.npz')

	def loadIndexDict(self):
		mappingFile = open("data/mappings.pkl", "rb")
		mapping = pickle.load(mappingFile)
		mappingFile.close()
		return mapping

	def findSimilarBooks(self, bookId, matrix, n=10, metric='cosine', show_distance=False):
		"""
		Finds k-nearest neighbours for a given movie id.
				
		Args:
			bookId: id of the movie of interest
			matrix: user-item utility matrix
			n: number of similar movies to retrieve
			metric: distance metric for kNN calculations
				
        Returns:
            list of k similar movie ID's
        """
		neighbourIds = []

		mapping = self.loadIndexDict()
		bMap = mapping["bookMap"]
		bMapInv = mapping["bookMapInv"]

		bookIndex = bMap[bookId]
		bookVector = matrix[bookIndex]
		n+=1
		kNN = NearestNeighbors(n_neighbors=n, algorithm="brute", metric=metric)
		kNN.fit(matrix)
		if isinstance(bookVector, (np.ndarray)):
			bookVector = bookVector.reshape(1,-1)
		neighbour = kNN.kneighbors(bookVector, return_distance=show_distance)
		for i in range(0,n):
			bookIndex = neighbour.item(i)
			
			# convert nparray to list to pass it to frontend
			bookId = (bMapInv[bookIndex]).tolist()
			neighbourIds.append(bookId)
		neighbourIds.pop(0)
		return neighbourIds