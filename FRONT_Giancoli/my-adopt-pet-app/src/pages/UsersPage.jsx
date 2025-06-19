// src/pages/UsersPage.jsx
import React from 'react';
import UsuarioCard from '../components/UsuarioCard';
import usersData from '../data/usuarios.json'; // Importando os dados dos usuários
import './UsersPage.css'; // Importando o CSS para estilização

const UsersPage = () => {
  return (
    <div>
      <h1>Instituições e Usuários</h1>
      <div className="usuario-list">
        {usersData.map(usuario => (
          <UsuarioCard key={usuario.id_usuario} usuario={usuario} />
        ))}
      </div>
    </div>
  );
};

export default UsersPage;