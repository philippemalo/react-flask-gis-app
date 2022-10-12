import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { Home } from './Home';
import { Login } from './Login';
import Map from './Map'
import { Navbar } from './Navbar';
import { AppContainer } from './styles/AppContainer.css';

export const App = () => {
  // const [currentTime, setCurrentTime] = useState(0);

  // useEffect(() => {
  //   fetch('/api/time').then(res => res.json()).then(data => {
  //     setCurrentTime(data.time);
  //   });
  // }, []);


  return (
    <AppContainer className="App">
      <BrowserRouter>
        <Navbar />
        <Switch>
          <Route exact path="/">
              <Home/>
          </Route>
          <Route path="/map">
            <Map/>
          </Route>
          <Route path="/login">
            <Login/>
          </Route>
        </Switch>
      </BrowserRouter>
    </AppContainer>
  )
}


export default App;
