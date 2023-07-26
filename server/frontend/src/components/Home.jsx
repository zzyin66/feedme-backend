import React, { useEffect } from "react";
import "./Home.css";
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
