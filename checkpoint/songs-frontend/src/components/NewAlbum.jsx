import { useState } from 'react';

function NewAlbum() {
  const [name, setName] = useState('');
  const [cover, setCover] = useState('');

  async function createAlbum(e) {
    e.preventDefault();
    const token = localStorage.getItem('auth-token');

    const formData = new FormData();
    formData.append('name', name);
    formData.append('cover', cover);

    const response = await fetch('http://localhost:8000/album/', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    });

    const data = await response.json();
    // eslint-disable-next-line no-restricted-globals
    location.reload();
    alert(`Se ha creado el album ${data.name}`);
  }

  return (
    <form onSubmit={createAlbum}>
      <div className='field'>
        <label className='label'>Nombre:</label>
        <div className='control'>
          <input
            className='input'
            type='text'
            value={name}
            onInput={e => setName(e.target.value)}
          />
        </div>
      </div>
      <div className='file has-name'>
        <label className='file-label'>
          <input
            className='file-input'
            type='file'
            accept='image/*'
            onInput={e => {
              setCover(e.target.files[0]);
            }}
          />
          <span className='file-cta'>
            <span className='file-icon'>
              <i className='fas fa-upload'></i>
            </span>
            <span className='file-label'>Sube tu portada…</span>
          </span>
          {cover ? <span className='file-name'>{cover.name}</span> : null}
        </label>
      </div>
      <div className='field is-grouped mt-3'>
        <div className='control'>
          <button className='button is-link'>Crear</button>
        </div>
        <div className='control'>
          <button className='button is-link is-light' type='reset'>
            Vaciar
          </button>
        </div>
      </div>
    </form>
  );
}

export default NewAlbum;
