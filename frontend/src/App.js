import React, { useState } from 'react';
import './App.css'; // Ajusta la importación de CSS según tu estructura de proyecto
import PersonaForm from './PersonaForm'; // Importa el componente PersonaForm

function App (){
  return (
    <div className="App">
      <h1 style={{marginTop:'50px'}}>Formulario Persona</h1>
      <br></br>
      <br></br>
      <br></br>
      <PersonaForm/>
    </div>
  );
}
export default App;