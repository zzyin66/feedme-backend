import React from "react";
import "./Home.css";
import { Newsfeed } from "./Newsfeed";
import { Navbar } from "./Navbar";
import { Outlet } from "react-router-dom";

const Home = () => {

  return (
    <>
      <Navbar />
      <Outlet />
    </>
  );
};

export { Home };
