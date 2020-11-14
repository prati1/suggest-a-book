import React, { useState, useEffect } from "react";
import { useLocation, withRouter } from "react-router-dom";
import books from "../resources/books.json";
import {
  Container,
  Card,
  CardImg,
  CardTitle,
  CardDeck,
  CardSubtitle,
  CardBody,
  Row,
  Col,
} from "reactstrap";
import axios from "axios";

const BookRecommendations = () => {
  const [recommendedBooks, setRecommendedBooks] = useState([]);
  const [bookTitle, setBookTitle] = useState("");
  const location = useLocation();

  useEffect(() => {
    if (location.search) {
      const search = location.search;
      const params = new URLSearchParams(search);
      const id = params.get("book_id");
      const recommendation = {
        method: "GET",
        url: `http://localhost:5000/api/recommend/books?id=${id}`,
      };

      axios(recommendation)
        .then((res) => {
          const bookIds = res.data.bookIds;
          const recommendations = books.filter((book) => {
            if (book.book_id == id) {
              setBookTitle(book.original_title);
            }
            return bookIds.includes(book.book_id);
          });
          setRecommendedBooks(recommendations);
        })
        .catch((err) => {
          console.log(`err`, err);
        });
    }
  }, [location]);

  return (
    <Container className="home-page">
      <h3>Recommendations based on the movie {bookTitle} that you liked:</h3>
      <div>
        <CardDeck>
          <Row>
            {recommendedBooks &&
              recommendedBooks.length > 0 &&
              recommendedBooks.map((item, i) => (
                <BookContainer item={item} key={i} />
              ))}
          </Row>
        </CardDeck>
      </div>
    </Container>
  );
};

const BookContainer = (props) => {
  let image = props.item.image_url;

  return (
    <Col sm="3">
      <Card>
        <CardImg top width="100%" src={image} alt="Card image cap" />
        <CardBody>
          <CardTitle>{props.item.original_title}</CardTitle>
          <CardSubtitle className="mb-2 text-muted">
            {props.item.authors}
          </CardSubtitle>
        </CardBody>
      </Card>
    </Col>
  );
};

export default withRouter(BookRecommendations);
