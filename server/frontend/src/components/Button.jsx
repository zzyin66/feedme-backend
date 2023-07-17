import React from "react";
import Button from "@mui/material/Button";
import { createTheme, ThemeProvider } from "@mui/material/styles";

const theme = createTheme({
  status: {
    danger: "#e53e3e",
  },
  palette: {
    primary: {
      main: "#0971f1",
      darker: "#053e85",
    },
    neutral: {
      main: "#64748B",
      contrastText: "#fff",
    },
  },
});

const GlobalButton = ({ onButtonClick }) => {
  return (
    <ThemeProvider theme={theme}>
      <Button color="neutral" variant="contained">
        Hello
      </Button>
    </ThemeProvider>
  );
};

export { GlobalButton };
