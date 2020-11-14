import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix, load_npz, save_npz
from sklearn.neighbors import NearestNeighbors
import pickle

class collaborativeFilteringModel():
    def __init__(self):
        self.bookRatings = pd.read_csv("dataset/ratings.csv")
        self.bookList = pd.read_csv("dataset/books.csv")

    def dataCleaning(self):
        # find any missing column
        column = ['user_id', 'book_id', 'rating']
        for columns in column:
            missing = self.bookRatings[columns].isnull().value_counts()

        # drops missing columns if any
        self.bookRatings = self.bookRatings.dropna(how='any')
        return self.bookRatings
    
    def calculateSparsity(self, matrix):
        sparsity = matrix.count_nonzero()/(matrix.shape[0]*matrix.shape[1])
        return sparsity
    
    def getDataInsights(self):
        noOfRatings = len(self.bookRatings)
        noOfBooks = self.bookRatings['book_id'].nunique()
        noOfUsers = self.bookRatings['user_id'].nunique()
        return noOfRatings, noOfBooks, noOfUsers

    def saveSparseMatrix(self, matrix):      
        save_npz('data/user_item_matrix.npz', matrix)

    def loadSparseMatrix(self):
        return load_npz('data/user_item_matrix.npz')

    def saveIndexDict(self, mappings):
        mappingFile = open("data/mappings.pkl", "wb")
        pickle.dump(mappings, mappingFile)
        mappingFile.close()

    def loadIndexDict(self):
        mappingFile = open("data/mappings.pkl", "rb")
        mapping = pickle.load(mappingFile)
        mappingFile.close()
        return mapping
    
    def getBookTitles(self):
        return dict(zip(self.bookList['book_id'], self.bookList['original_title']))

    # Using collaborative filtering to recommend a user a book 
    # Assuming that similar users like similar things

    # Transforming data into user-item matrix
    # No information about user or item is required 
    def generateSparseMatrix(self, df):
        """ Generates a sparse matrix from a pandas dataframe.

        Args:
            df: pandas dataframe
        
        Returns:
            matrix: a sparse matrix
            userMap: dict. maps user id to user indices
            userMapInv: dict. maps user indices to user id
            bookMap: dict. maps book id to book indices
            bookMapInv: dict. maps book indices to book id
        """
        noOfUsers = df['user_id'].nunique()
        noOfBooks = df['book_id'].nunique()

        userMap = dict(zip(np.unique(df["user_id"]), list(range(noOfUsers))))
        bookMap = dict(zip(np.unique(df["book_id"]), list(range(noOfBooks))))
        
        userMapInv = dict(zip(list(range(noOfUsers)), np.unique(df["user_id"])))
        bookMapInv = dict(zip(list(range(noOfBooks)), np.unique(df["book_id"])))
        
        userIndex = [userMap[i] for i in df['user_id']]
        bookIndex = [bookMap[i] for i in df['book_id']]

        matrix = csr_matrix((df["rating"], (bookIndex, userIndex)), shape=(noOfBooks, noOfUsers))
        
        return matrix, userMap, bookMap, userMapInv, bookMapInv

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
            neighbourIds.append(bMapInv[bookIndex])
        neighbourIds.pop(0)
        return neighbourIds