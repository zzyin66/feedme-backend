import React, { useState } from "react";
import axios from "axios";
import "./Navbar.css";
import { useNavigate } from "react-router-dom";
import { Navitem } from "./Navitem";

const Navbar = () => {
  const navigate = useNavigate();
  const [showNav, setShowNav] = useState(true);

  const onLogout = async () => {
    try {
      await axios.post("/api/logout/");

      navigate("/login");
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div className="side-navbar" style={{
      transform: showNav ? "translateX(0%)" : "translateX(-100%)",
    }}>
      <div className="navbar-toggle" onClick={() => setShowNav(!showNav)}>
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M16 5H4V7H16V5Z" fill="currentColor" />
          <path d="M16 9H4V11H16V9Z" fill="currentColor" />
          <path d="M4 13H12V15H4V13Z" fill="currentColor" />
          <path d="M20 16L14 13V19L20 16Z" fill="currentColor" />
        </svg>
      </div>
      <div className="item-container">
        <h3 className="navbar-header">
          <span className="magic-text">Menu</span>
        </h3>
        <Navitem title="Home" link="/" />
        <Navitem title="Science" link="/category/science" />
        <Navitem title="Sports" link="/category/sports" />
        <Navitem title="Health" link="/category/health" />
        <Navitem title="Entertainment" link="/category/entertainment" />
        <Navitem title="Technology" link="/category/technology" />
        <Navitem title="Business" link="/category/business" />
        <Navitem title="Nation" link="/category/nation" />
        <Navitem title="World" link="/category/world" />
        <div onClick={onLogout} className="footer">
          <span className="magic-text">Logout</span>
        </div>
      </div>
    </div>
  );
};

export { Navbar };
