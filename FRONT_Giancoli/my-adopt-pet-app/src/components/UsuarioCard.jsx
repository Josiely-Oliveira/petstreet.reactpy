// src/components/UsuarioCard.jsx
import React from 'react';
import './UsuarioCard.css'; // Importando o CSS para estilização

const UsuarioCard = ({ usuario }) => {
  return (
    <div className="usuario-card">
      <h3>{usuario.nome}</h3>
      <p>{usuario.email}</p>
      <p>{usuario.cidade} - {usuario.estado}</p>
      <p>{usuario.telefone}</p>
      <img src={usuario.foto_perfil} alt={usuario.nome} />
    </div>
  );
};

export default UsuarioCard;