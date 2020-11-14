import React, { useState } from "react";
import { Navbar, NavbarToggler, NavbarBrand, Container } from "reactstrap";

const AppNavbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    console.log(isOpen);
    setIsOpen(!isOpen);
  };

  return (
    <div>
      <Navbar color="dark" dark expand="sm" className="mb-5">
        <Container>
          <NavbarBrand href="/">SuggestABook</NavbarBrand>
          <NavbarToggler onClick={toggle} />
        </Container>
      </Navbar>
    </div>
  );
};

export default AppNavbar;
