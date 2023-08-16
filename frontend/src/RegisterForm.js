import React, { useState } from 'react';
import './RegisterForm.css';

function RegisterForm({ onRegister }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = (e) => {
    e.preventDefault();
    onRegister(email, password);
  };

  return (
    <form className="login-form" onSubmit={handleRegister}>
    <label>
      <input
        type="email"
        placeholder="Correo Electrónico"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      </label>
      <button onClick={handleRegister}>Registrarse</button>
   
    </form>
  );
}

export default RegisterForm;
