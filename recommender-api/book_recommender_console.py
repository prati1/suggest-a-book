from collaborative_filtering_recommender import collaborativeFilteringModel
from book_recommender import recommenderCollaborativeFiltering

collaborativeFiltering = collaborativeFilteringModel()
bookTitles = collaborativeFiltering.getBookTitles()

# A bookId used to suggest similar books
bookId = 12

recommender = recommenderCollaborativeFiltering()
matrix = recommender.loadSparseMatrix()
similarIds = recommender.findSimilarBooks(bookId, matrix, n=15)
bookTitle = bookTitles[bookId]

# get book titles based on id from frontend
print("People who read ", bookTitle, " also liked:")
for i in similarIds:
	print(bookTitles[i])