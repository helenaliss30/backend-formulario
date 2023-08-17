import React, { useState } from 'react';
import QRCode from "qrcode";
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

  const handleClear = () => {
    setFormData({
      nombre: '',
      apellido: '',
      edad: '',
      cedula: '',
      correo_electronico: '',
      enfermedades: [],
      alergias: [],
      medicamentos: [],
    });
    setErrorMessages({
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
    setQRCodeValue('');
  };

  const [qrCodeValue, setQRCodeValue] = useState(null); 

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const generateQRImageBase64 = value => {
    // Cambia esta URL por la que necesites
    const canvas = document.createElement("canvas");
    QRCode.toCanvas(canvas, value, error => {
      if (error) {
        console.error(error);
      } else {
        const QR_IMAGE = canvas.toDataURL("image/png");
        crearPersona(QR_IMAGE);
        setQRCodeValue(QR_IMAGE);
      }
    });
  };

  const handleArrayChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value.split(',').map((item) => item.trim()),
    }));
  };
  const crearPersona = async qrImageBase64 => {
    try {
      const dataFetch = {
        ...formData,
        qr_image: qrImageBase64
      }
      console.log(dataFetch)
      const response = await fetch(`${API}/personas`, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(dataFetch),
      });

      const data = await response.json();
      console.log(data);
      if (response.ok) {
        console.log("Response from server:", data);
      } else {
        setErrorMessages(data.message || {});
      }
    } catch (error) {
      console.error(error);
      setErrorMessages({
        general: "Ocurrio Un Error. Please try again later.",
      });
    }
  };
  const handleSubmit = e => {
    e.preventDefault();
    generateQRImageBase64(formData.cedula);
  };
  return (
    <div>
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
        <button type="button" onClick={handleClear}>Limpiar</button>
        <span className="error-message">{errorMessages.general}</span>
      </form>
      {qrCodeValue && (
        <div className="qr-code-container">
          <img src={qrCodeValue} alt="QR Code" />
        </div>
      )}
    </div>
  );
}

export default PersonaForm;