import React, { useEffect, useState } from "react";
import axios from "axios";
import { Newscard } from "./Newscard";
import "./Newsfeed.css";
import { useParams } from "react-router-dom";

const Newsfeed = ({ isRecommendation }) => {
  const [data, setData] = useState([]);
  const { category } = useParams();

  useEffect(() => {
    const getNewsfeed = async () => {
      try {
        if (isRecommendation) {
          const res = await axios.get("/api/recommendations/");

          setData(res.data);
        } else {
          const res = await axios.get("/api/feeds", {
            params: { category: category },
          });
          console.log(res);
          setData(res.data);
        }
      } catch (error) {
        if (error.response) {
          if (error.response.data.detail === "Unauthenticated") {
            navigate("/login");
          }
          console.error(error);
        }
      }
    };

    getNewsfeed();
  }, []);

  return (
    <div className="newsfeed-content">
      <h1 className="newsfeed-header">
        <span className="magic-text">
          {!isRecommendation ? category : "recommended"}
        </span>
      </h1>
      {data?.map((newsfeed) => (
        <Newscard
          key={newsfeed.id}
          title={newsfeed.title}
          date={newsfeed.date}
          description={newsfeed.description}
          image={newsfeed.image}
          link={newsfeed.url}
          id={newsfeed.id}
        />
      ))}
    </div>
  );
};

export { Newsfeed };
