import axios from 'axios';

export async function getToken() {
  const token = localStorage.getItem('accessToken');
  if (token) {
    try {
      await axios.post('http://localhost:8000/api/token/verify/', { token });
      return token;
    } catch {
      const refresh = localStorage.getItem('refreshToken');
      try {
        const { data } = await axios.post(
          'http://localhost:8000/api/token/refresh/',
          {
            refresh,
          }
        );
        localStorage.setItem('accessToken', data.access);
        return data.access;
      } catch {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        return null;
      }
    }
  }
}
