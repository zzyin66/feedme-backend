import React, { useEffect } from "react";
import "./Home.css";
import { Navbar } from "./Navbar";
import { Outlet } from "react-router-dom";
import axios from "axios";

const Home = () => {
  return (
    <>
      <Navbar />
      <Outlet />
    </>
  );
};

export { Home };
