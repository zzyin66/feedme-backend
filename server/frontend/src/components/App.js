import React from "react";
import { render } from "react-dom";
import { BrowserRouter, Routes, Route, Link, Redirect } from "react-router-dom";
import { Home } from "./Home";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}

const appDiv = document.getElementById("app");

render(<App />, appDiv);

export default App;
