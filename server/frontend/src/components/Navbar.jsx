import React from "react";
import "./Navbar.css";

const Navbar = () => {
  return (
    <div className="side-navbar">
      <div className="blur-effect">
        <h3>Menu</h3>
        <a href="/">Home</a>
        <a href="/category/sports">Sports</a>
        <a href="/category/science">Science</a>
        <a href="/category/health">Health</a>
        <a href="/category/entertainment">Entertainment</a>
        <a href="/category/technology">Technology</a>
        <a href="/category/business">Business</a>
        <a href="/category/nation">Nation</a>
        <a href="/category/world">World</a>
      </div>
    </div>
  );
};

export { Navbar };
