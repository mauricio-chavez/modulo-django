import { useState } from 'react';

import Header from './components/Header';
import Login from './components/Login';
import Albums from './components/Albums';

function App() {
  const token = localStorage.getItem('auth-token')
  const [authenticated, setAuthenticated] = useState(!!token);

  return (
    <div className='App'>
      <Header />
      {authenticated ? <Albums /> : <Login authHandler={setAuthenticated} />}
    </div>
  );
}

export default App;
