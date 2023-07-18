import React, { useMemo, useState, useEffect } from "react";
import "./Home.css";
import { Newscard } from "./Newscard";
import axios from "axios";

const Home = () => {
  const [data, setData] = useState([]);

  useMemo(() => {
    const getNewsfeed = async () => {
      try {
        const res = await axios.get("/api/recommendations/");

        console.log(res);
        setData(res.data);
      } catch (error) {
        console.error(error);
      }
    };

    getNewsfeed();
  }, []);

  return (
    <>
      <div className="side-navbar">
        <div className="blur-effect">
          <h3>Menu</h3>
          <a href="#">Link 1</a>
          <a href="#">Link 2</a>
        </div>
      </div>

      <div className="homepage-content">
        <h1 className="homepage-header">
          <span className="magic-text">Feedme</span>
        </h1>
        {data?.map((newsfeed) => (
          <Newscard
            key={newsfeed.id}
            title={newsfeed.title}
            date={newsfeed.date}
            description={newsfeed.description}
            image={newsfeed.image}
            link={newsfeed.url}
          />
        ))}
      </div>
    </>
  );
};

export { Home };
