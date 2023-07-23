import React from "react";
import "./Navbar.css";

const Navitem = ({ link, title }) => {
  return (
    <span>
      <a className="navitem-main" href={link}>
        <span className="magic-text">{title}</span>
      </a>
    </span>
  );
};

export { Navitem };
