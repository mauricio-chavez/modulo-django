import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

import { getToken } from '../utils/auth';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  useEffect(() => {
    getToken().then(token => {
      if (token) history.push('/locations');
    });
  }, [history]);

  async function submitForm(e) {
    e.preventDefault();
    try {
      const { data } = await axios.post('http://localhost:8000/api/token/', {
        username,
        password,
      });
      const { access, refresh } = data;
      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', refresh);
      localStorage.setItem('authToken', access);
      history.push('/locations');
    } catch (e) {
      alert(e.response.data.detail);
    }
  }

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={submitForm}>
        <p>
          <label htmlFor='username-id'>Username:</label>
          <input
            type='text'
            id='username-id'
            value={username}
            onInput={e => {
              setUsername(e.target.value);
            }}
          />
        </p>
        <p>
          <label htmlFor='password-id'>Password:</label>
          <input
            type='password'
            id='password-id'
            value={password}
            onInput={e => {
              setPassword(e.target.value);
            }}
          />
        </p>
        <button>Submit!</button>
      </form>
    </div>
  );
}
