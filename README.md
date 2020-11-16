# suggest-A-book

A book recommendation system using item-item collaborative filtering. It is a simple implemenation of collaborative filtering approach for recommendation systems. The system recommends books to the user based on their recent read by using k-Nearest neighbors approach on user-item sparse matrix.

## Dataset

The dataset used is goodreads-10k dataset that contains 6 million ratings for ten thousand most popular books (https://github.com/zygmuntz/goodbooks-10k).

## Prerequisites

### Backend (Recommendation system)

- python >= 3.6

### Frontend

- node.js >= 10.12.0

## Installation steps

### Optional: Create virtual environment for python

```
pip install --user virtualenv
virtualenv env
source env/bin/activate
```

### Clone the repository and install required packages

```
git clone https://github.com/prati1/suggest-a-book.git
cd suggest-a-book/frontend
npm install
cd ../recommender-api
pip install -r requirements.txt
```

### Generate user-item sparse matrix

Go to `recommender-api` folder

```
python sparse_matrix_generator.py
```

### Run recommender api

```
python recommender_api.py
```

### Run recommender frontend

Go to `frontend` folder

```
npm start
```
