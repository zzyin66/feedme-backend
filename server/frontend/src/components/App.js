import React from 'react';
import { render } from 'react-dom';

function App() {
  return (
    <div className="App">
      Hello
    </div>
  );
}

const appDiv = document.getElementById("app");

render(<App />, appDiv);

export default App;