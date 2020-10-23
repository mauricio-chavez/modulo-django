import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Login from './components/Login';
import Locations from './components/Locations';

function App() {
  return (
    <Router>
      <Switch>
        <Route path='/locations'>
          <Locations />
        </Route>
        <Route path='/'>
          <Login />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
