import React, { useState } from 'react';
import './App.css'; // Ajusta la importación de CSS según tu estructura de proyecto
import PersonaForm from './PersonaForm'; // Importa el componente PersonaForm
import LoginComponent from './LoginComponent';
import RegisterForm from './RegisterForm';

const API= process.env.REACT_APP_API;

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false); // Cambiado a false, ya que el usuario aún no ha iniciado sesión
  const [loginError, setLoginError] = useState("");
  const [showLogin, setShowLogin] = useState(true);
  
  const handleLogin = async (email, password) => {
    try {
      const response = await fetch(`${API}/login`, {
        method: "POST",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email: email, password: password }),
      });

      const data = await response.json();
      if (response.ok) {
        setIsLoggedIn(true);
      } else {
        setLoginError(data.message || "Error de inicio de sesión");
      }
    } catch (error) {
      console.error(error);
      setLoginError("Ocurrió un error. Por favor, inténtalo de nuevo más tarde.");
    }
  };
  const handleToggleForm = () => {
    setShowLogin(!showLogin);
  };

  const handleRegister = async (email, password) => {
    
    try {
      const response = await fetch(`${API}/registro`, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: email, password: password }),
      });
    
      const data = await response.json();
      if (response.ok) {
        setIsLoggedIn(true);
      } else {
        setLoginError(data.message || "Error de registrarse");
      }
    } catch (error) {
      console.error(error);
      setLoginError("Ocurrió un error. Por favor, inténtalo de nuevo más tarde.");
    }
    console.log('Registrarse con:', email, password);
  };
  return (
    <div className="App">
      <br></br>
      {isLoggedIn ? (
        <>
         <h1 style={{ marginTop: '15px' }}>Formulario de Persona</h1>
          <PersonaForm />
        </>
      ) : (
        <>
          <br></br>
          <br></br>
         <h1>{showLogin ? 'Iniciar Sesión' : 'Registrarse'}</h1>
          {showLogin ? (
            <LoginComponent onLogin={handleLogin} />
          ) : (
            <RegisterForm onRegister={handleRegister} />
          )}
          {showLogin ? (
            <>
              <span className="error-message">{loginError}</span>
              <br />
              <button onClick={handleToggleForm}>
                Cambiar a Registro
              </button>
            </>
          ) : (
            <button onClick={handleToggleForm}>
              Cambiar a Iniciar Sesión
            </button>
          )}
        </>
      )}
    </div>
  );

}

export default App;
