import React from "react";
import { render } from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./Home/Home";
import { Login } from "./Login/Login";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { Register } from "./Register/Register";
import { Newsfeed } from "./Newsfeed/Newsfeed";

const theme = createTheme({
  status: {
    danger: "#e53e3e",
  },
  palette: {
    primary: {
      main: "#000000",
      darker: "#053e85",
    },
    neutral: {
      main: "#64748B",
      contrastText: "#fff",
    },
    test: {
      main: "#000000",
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />}>
            <Route path="" element={<Newsfeed isRecommendation={true} />} />
            <Route
              path="category/:category"
              element={<Newsfeed isRecommendation={false} />}
            />
          </Route>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

const appDiv = document.getElementById("app");

render(<App />, appDiv);

export default App;
