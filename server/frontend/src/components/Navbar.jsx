import React from "react";
import axios from "axios";
import "./Navbar.css";
import { useNavigate } from "react-router-dom";
import { Navitem } from "./Navitem";

const Navbar = () => {
  const navigate = useNavigate();
  const onLogout = async () => {
    try {
      await axios.post("/api/logout/");

      navigate("/login");
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div className="side-navbar">
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
