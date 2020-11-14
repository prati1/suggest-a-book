import React, { useState, useEffect } from "react";
import { Link, useHistory, withRouter } from "react-router-dom";
import books from "../resources/books.json";
import {
  Container,
  Card,
  Button,
  CardImg,
  CardTitle,
  CardDeck,
  CardSubtitle,
  CardBody,
  Row,
  Col,
} from "reactstrap";

const HomePage = () => {
  const [page, setPage] = useState(0);
  const [bookChunks, setBookChunks] = useState([]);
  const chunk = (arr, size) =>
    Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
      arr.slice(i * size, i * size + size)
    );
  const onClickNext = (e) => {
    e.preventDefault();
    let nextPage = page + 1;
    if (nextPage < bookChunks.length) {
      setPage(page + 1);
    }
  };

  const onClickPrev = (e) => {
    e.preventDefault();
    let prevPage = page - 1;
    if (prevPage > 0) {
      setPage(prevPage);
    }
  };
  useEffect(() => {
    const chunks = chunk(books, 15);
    setBookChunks(chunks);
  }, []);

  return (
    <Container className="home-page">
      <h3>Select a book from the list below that you liked</h3>
      <div>
        <CardDeck>
          <Row>
            {bookChunks &&
              bookChunks.length > 0 &&
              bookChunks[page].map((item, i) => (
                <BookContainer item={item} key={i} />
              ))}
          </Row>
        </CardDeck>
      </div>
      <Row className="prev-next-buttons">
        <Link className="previous" to="#" onClick={onClickPrev}>
          &#8249; Previous
        </Link>
        <Link className="next" to="#" onClick={onClickNext}>
          Next &#8250;
        </Link>
      </Row>
    </Container>
  );
};

const BookContainer = (props) => {
  let history = useHistory();
  let image = props.item.image_url;

  const onClick = (e) => {
    e.preventDefault();
    history.push({
      pathname: "/recommendations",
      search: `?book_id=${props.item.book_id}`,
      state: { book_id: props.item.book_id },
    });
  };

  return (
    <Col sm="3">
      <Card>
        <CardImg top width="100%" src={image} alt="Card image cap" />
        <CardBody>
          <CardTitle>{props.item.original_title}</CardTitle>
          <CardSubtitle className="mb-2 text-muted">
            {props.item.authors}
          </CardSubtitle>
          <Button onClick={onClick}>I loved this!</Button>
        </CardBody>
      </Card>
    </Col>
  );
};

export default withRouter(HomePage);
