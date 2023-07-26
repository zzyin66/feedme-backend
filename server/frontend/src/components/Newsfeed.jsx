import React, { useEffect, useState } from "react";
import axios from "axios";
import { Newscard } from "./Newscard";
import "./Newsfeed.css";
import { useNavigate, useParams } from "react-router-dom";
import InfiniteScroll from "react-infinite-scroll-component";

const Newsfeed = ({ isRecommendation }) => {
  const [data, setData] = useState([]);
  const { category } = useParams();
  const navigate = useNavigate();
  const [pageIndex, setPageIndex] = useState(1);

  const fetchData = async () => {
    try {
      if (isRecommendation) {
        const res = await axios.get("/api/recommendations/");
        setData(res.data);

        console.log(res);
      } else {
        const res = await axios.get("/api/feeds", {
          params: { category: category, page: pageIndex },
        });

        console.log(res.data);
        setData((prevData) => [...prevData, ...res.data.results]);
        setPageIndex(res.data.next ? pageIndex + 1 : null);
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

  useEffect(() => {
    setData([]);
    setPageIndex(1);
  }, [category, isRecommendation]);

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="newsfeed-content" id="scroll-target">
      <h1 className="newsfeed-header">
        <span className="magic-text" style={{textTransform: "capitalize"}}>
          {!isRecommendation ? category : "recommended"}
        </span>
      </h1>
      <InfiniteScroll
        dataLength={data.length}
        next={fetchData}
        hasMore={!isRecommendation ? true : false}
        loader={<h4>Loading...</h4>}
        scrollableTarget="scroll-target"
        endMessage={
          <p style={{ textAlign: "center" }}>
            <b>Yay! You have seen it all</b>
          </p>
        }
      >
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
      </InfiniteScroll>
    </div>
  );
};

export { Newsfeed };
