// src/pages/Home.jsx
import React, { useEffect, useState } from 'react';
import AnimalCard from '../components/AnimalCard';
import PublicacaoCard from '../components/PublicacaoCard';
import UsuarioCard from '../components/UsuarioCard';
import animais from '../data/animais.json';
import publicationsData from '../data/publicacoes.json';
import usersData from '../data/usuarios.json';
import './Home.css'; // Importando o CSS para estilização

const Home = () => {
  const [animals, setAnimals] = useState([]);
  const [publications, setPublications] = useState([]);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    setAnimals(animais);
    setPublications(publicationsData);
    setUsers(usersData);
  }, []);

  return (
    <div>
      <h1>Adoção de Animais</h1>

      <h2>Animais Disponíveis</h2>
      <div className="animal-list">
        {animals.filter(animal => animal.id_status === 1).map(animal => (
          <AnimalCard key={animal.id_animal} animal={animal} />
        ))}
      </div>

      <h2>Publicações de Adoção</h2>
      <div className="publicacao-list">
        {publications.map(publicacao => (
          <PublicacaoCard key={publicacao.id_publicacao} publicacao={publicacao} />
        ))}
      </div>

      <h2>Instituições e Usuários</h2>
      <div className="usuario-list">
        {users.map(usuario => (
          <UsuarioCard key={usuario.id_usuario} usuario={usuario} />
        ))}
      </div>
    </div>
  );
};

export default Home;