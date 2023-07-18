import React from "react";
import "./Newscard.css";

const Newscard = ({ title, date, description, image, link }) => {
  return (
    <div className="main">
      <div className="screen">
        <div
          style={{ backgroundImage: `url("${image}")` }}
          className="image"
        ></div>
        {/* <div className="overlay"></div> */}
      </div>

      <div className="content">
        <span className="date">{date}</span>
        <div className="title_container">
          <span className="title">{title}</span>
          <p className="description">{description}</p>
        </div>
        <a
          className="link"
          target="_blank"
          rel="noopener noreferrer"
          href={link}
        >
          Read full article
        </a>
      </div>
    </div>
  );
};

export { Newscard };
