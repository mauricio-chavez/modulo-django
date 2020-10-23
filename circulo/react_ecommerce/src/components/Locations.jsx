import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

import { getToken } from '../utils/auth';

export default function Locations() {
  const [locations, setLocations] = useState([]);
  const history = useHistory();

  useEffect(() => {
    getToken().then(token => {
      if (!token) {
        history.push('/');
      } else {
        axios
          .get('http://localhost:8000/api/location/')
          .then(response => {
            setLocations(response.data);
          })
          .catch(() => {
            history.push('/');
          });
      }
    });
  }, [history]);

  function sendLocation() {
    const success = location => {
      getToken().then(token => {
        if (!token) {
          history.push('/');
        } else {
          axios
            .post(
              'http://localhost:8000/api/location/',
              {
                json: {
                  latitude: location.coords.latitude,
                  longitude: location.coords.longitude,
                },
              },
              {
                headers: { Authorization: `Bearer ${token}` },
              }
            )
            .then(() => {
              axios
                .get('http://localhost:8000/api/location/')
                .then(response => {
                  setLocations(response.data);
                });
            })
            .catch(() => {
              history.push('/');
            });
        }
      });
    };

    navigator.geolocation.getCurrentPosition(success, e => {
      console.log('e');
    });
  }

  function logOut() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    history.push('/');
  }

  return (
    <div>
      <h1>Locations</h1>
      <div>
        <button onClick={sendLocation}>Crear nueva localización</button>
        <button onClick={logOut}>Cerrar sesión</button>
      </div>
      <ul>
        {locations.map(location => (
          <li key={location.url}>{JSON.stringify(location.json)}</li>
        ))}
      </ul>
    </div>
  );
}
