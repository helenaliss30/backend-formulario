import React, { useState } from 'react';
import './formulario.css';

const API= process.env.REACT_APP_API;

function PersonaForm() {
  const [formData, setFormData] = useState({
    nombre: '',
    apellido: '',
    edad: '',
    cedula: '',
    correo_electronico: '',
    enfermedades: [],
    alergias: [],
    medicamentos: [],
  });

  const [errorMessages, setErrorMessages] = useState({
    nombre: '',
    apellido: '',
    edad: '',
    cedula: '',
    correo_electronico: '',
    enfermedades: '',
    alergias: '',
    medicamentos: '',
    general: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleArrayChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value.split(',').map((item) => item.trim()),
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`${API}/personas`, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
    
      const data = await response.json();
      console.log(data)
      if (response.ok) {
        console.log('Response from server:', data);
      } else {
        setErrorMessages(data.message || {});
      }
    } catch (error) {
      console.error(error);
      setErrorMessages({ general: 'Ocurrio Un Error. Please try again later.' });
    }
  };

  return (
    // <div>
    <form onSubmit={handleSubmit}>
      <label>
        
        <input
          type="text"
          name="nombre"
          value={formData.nombre}
          onChange={handleInputChange}
          placeholder="Nombre"
        />
        <span className="error-message">{errorMessages.nombre}</span>
      </label>

      <label>

        <input
          type="text"
          name="apellido"
          value={formData.apellido}
          onChange={handleInputChange}
          placeholder="Apellido"
        />
        <span className="error-message">{errorMessages.apellido}</span>
      </label>
      

      <label>

        <input
          type="number"
          name="edad"
          value={formData.edad}
          onChange={handleInputChange}
          placeholder="Edad"
        />
        <span className="error-message">{errorMessages.edad}</span>
      </label>
      

      <label>

        <input
          type="text"
          name="cedula"
          value={formData.cedula}
          onChange={handleInputChange}
          placeholder="Cédula"
        />
        <span className="error-message">{errorMessages.cedula}</span>
      </label>

      <label>

        <input
          type="email"
          name="correo_electronico"
          value={formData.correo_electronico}
          onChange={handleInputChange}
          placeholder="Correo Electrónico"
        />
        <span className="error-message">{errorMessages.correo_electronico}</span>
      </label>

      <label>
        Enfermedades (separadas por coma)
        <input
          type="text"
          name="enfermedades"
          value={formData.enfermedades.join(', ')}
          onChange={handleArrayChange}
          placeholder="Enfermedades"
        />
        <span className="error-message">{errorMessages.enfermedades}</span>
      </label>

      <label>
        Alergias (separadas por comas):
        <input
          type="text"
          name="alergias"
          value={formData.alergias.join(', ')}
          onChange={handleArrayChange}
          placeholder="Alergias"
        />
        <span className="error-message">{errorMessages.alergias}</span>
      </label>

      <label>
        Medicamentos (separados por comas):
        <input
          type="text"
          name="medicamentos"
          value={formData.medicamentos.join(', ')}
          onChange={handleArrayChange}
          placeholder="Medicamentos"
        />
        <span className="error-message">{errorMessages.medicamentos}</span>
      </label>
      <button type="submit">Guardar</button>
      <span className="error-message">{errorMessages.general}</span>
    </form>
    // {/* {showQR &&(
    //   <div className="qr-container">
    //     <h2>Codigo QR Generado:</h2>
    //     <QRCode value={qrContent} size={256}/>
    //   </div>
    // )}
    // </div> */}
  );
}

export default PersonaForm;