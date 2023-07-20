import React from "react";
import axios from "axios";
import "./Newscard.css";

const Newscard = ({ title, date, description, image, link, id }) => {
  const markAsRead = async () => {
    try {
      await axios.post("/api/mark_read/", {
        feed_id: id,
      });
    } catch (error) {
      console.error(error);
    }
  };
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
          onClick={markAsRead}
        >
          Read full article
        </a>
      </div>
    </div>
  );
};

export { Newscard };
