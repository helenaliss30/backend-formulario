import React, { useState } from 'react';
import './LoginComponent.css'; // Importa el archivo de estilos CSS

function LoginComponent({ onLogin }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onLogin(email, password);
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
      <label>
        
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          placeholder="Email"
        />
      </label>
      <label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          placeholder="Contraseña"
        />
      </label>
      <button type="submit">Iniciar Sesión</button>
    </form>
  
  );
}

export default LoginComponent;
