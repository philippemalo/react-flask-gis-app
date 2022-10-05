import React, { useState, useEffect } from 'react';
import { BrowserRouter, Link, Switch, Route } from 'react-router-dom';
import Map from './Map'
import { Navbar } from './Navbar';
import { AppContainer } from './styles/AppContainer.css';

export const App = () => {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);


  return (
    <AppContainer className="App">
      <BrowserRouter>
        <Navbar />
        <Switch>
          <Route exact path="/">
              <p>The current time is: {currentTime}.</p>
          </Route>
          <Route path="/page2">
            <Map/>
          </Route>
        </Switch>
      </BrowserRouter>
    </AppContainer>
  )
}


export default App;
