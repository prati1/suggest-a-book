import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import { Route, BrowserRouter as Router } from "react-router-dom";
import Navbar from "./components/Navbar";
import HomePage from "./components/HomePage";
import BookRecommendations from "./components/BookRecommendations";

const App = () => {
  return (
    <div>
      <Navbar />
      <Router>
        <div>
          <Route exact path="/" component={HomePage} />
          <Route path="/recommendations" component={BookRecommendations} />
        </div>
      </Router>
    </div>
  );
};

export default App;
