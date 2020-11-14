from collaborative_filtering_recommender import collaborativeFilteringModel

collaborativeFiltering = collaborativeFilteringModel()

bookTitles = collaborativeFiltering.getBookTitles()

bookId = 23

matrix = collaborativeFiltering.loadSparseMatrix()
similarIds = collaborativeFiltering.findSimilarBooks(bookId, matrix, n=15)
bookTitle = bookTitles[bookId]

# get book titles based on id from frontend
print("People who read ", bookTitle, " also liked:")
for i in similarIds:
	print(bookTitles[i])