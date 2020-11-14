import flask
from flask import request
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1>Book recommendation</h1></p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/recommend/books', methods=['GET'])
def api_recommend_ids():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return {'errorCode': 'MissingParameterException', 'message': 'Book id not present in request.'}

	from book_recommender import recommenderCollaborativeFiltering

	recommender = recommenderCollaborativeFiltering()
	matrix = recommender.loadSparseMatrix()
	similarIds = recommender.findSimilarBooks(id, matrix, n=15)
	# bookTitle = bookTitles[bookId]

	# get book titles based on id from frontend
	return json.dumps({'bookIds': similarIds})
app.run()