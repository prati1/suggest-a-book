from collaborative_filtering_recommender import collaborativeFilteringModel

collaborativeFiltering = collaborativeFilteringModel()
ratings = collaborativeFiltering.dataCleaning()

noOfRatings, noOfBooks, noOfUsers = collaborativeFiltering.getDataInsights()
print("Number of ratings: ", noOfRatings)
print("Number of unique books: ", noOfBooks)
print("Number of unique users: ", noOfUsers)
print("Average number of ratings per user: ", round(noOfRatings/noOfUsers, 2))
print("Average number of ratings per book: ", round(noOfRatings / noOfBooks, 2))

matrix, userMap, bookMap, userMapInv, bookMapInv = collaborativeFiltering.generateSparseMatrix(ratings)
userAndBookMaps = {"userMap": userMap, "bookMap":bookMap, "userMapInv": userMapInv, "bookMapInv": bookMapInv}

collaborativeFiltering.saveSparseMatrix(matrix)
collaborativeFiltering.saveIndexDict(userAndBookMaps)

sparsity = collaborativeFiltering.calculateSparsity(matrix)
print("Matrix sparsity: ", round(sparsity*100,2))
