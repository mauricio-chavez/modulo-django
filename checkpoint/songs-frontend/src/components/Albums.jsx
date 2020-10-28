import { useEffect, useState } from 'react';
import axios from 'axios';

import NewAlbum from './NewAlbum';

function Albums() {
  const [albums, setAlbums] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('auth-token');
    axios
      .get('http://localhost:8000/album/', {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then(response => {
        setAlbums(response.data);
      });
  }, [setAlbums]);

  return (
    <>
      <section className='section'>
        <div className='container'>
          <NewAlbum />
        </div>
      </section>
      <section className='section'>
        <div className='container'>
          <h1 className='title'>Albums</h1>
          <div className='columns is-multiline'>
            {albums.map(album => (
              <div key={album.id} className='column is-one-quarter'>
                <div className='card'>
                  <div className='card-image'>
                    <figure className='image is-square'>
                      <img src={album.cover} alt={`Portada de ${album.name}`} />
                    </figure>
                  </div>
                  <div className='card-content'>
                    <h2 className='title is-5'>{album.name}</h2>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}

export default Albums;
