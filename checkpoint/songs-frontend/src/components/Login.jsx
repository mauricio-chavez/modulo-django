import { useState } from 'react';
import axios from 'axios';

function Login({ authHandler }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [usernameErrors, setUsernameErrors] = useState([]);
  const [passwordErrors, setPasswordErrors] = useState([]);

  async function getToken(e) {
    e.preventDefault();
    try {
      const { data } = await axios.post('http://localhost:8000/auth/token/', {
        username,
        password,
      });
      localStorage.setItem('auth-token', data.access);
      authHandler(true);
    } catch (e) {
      if (e.response) {
        const { data } = e.response;
        if (e.response.status === 400) {
          if (data.username) setUsernameErrors(data.username);
          if (data.password) setPasswordErrors(data.password);
        } else if (e.response.status === 401) {
          alert(data.detail);
        }
      } else {
        alert(e.message);
      }
    }
  }

  return (
    <section className='section'>
      <div className='container px-5'>
        <form onSubmit={getToken}>
          <div className='field'>
            <label className='label'>Usuario:</label>
            <div className='control'>
              <input
                className='input'
                type='text'
                value={username}
                onInput={e => setUsername(e.target.value)}
              />
            </div>
            {usernameErrors.map(error => (
              <p key={error} className='help is-danger'>
                {error}
              </p>
            ))}
          </div>
          <div className='field'>
            <label className='label'>Contraseña:</label>
            <div className='control'>
              <input
                className='input'
                type='password'
                value={password}
                onInput={e => setPassword(e.target.value)}
              />
            </div>
            {passwordErrors.map(error => (
              <p key={error} className='help is-danger'>
                {error}
              </p>
            ))}
          </div>
          <div className='field is-grouped'>
            <div className='control'>
              <button className='button is-link'>Enviar</button>
            </div>
            <div className='control'>
              <button className='button is-link is-light' type='reset'>
                Vaciar
              </button>
            </div>
          </div>
        </form>
      </div>
    </section>
  );
}

export default Login;
