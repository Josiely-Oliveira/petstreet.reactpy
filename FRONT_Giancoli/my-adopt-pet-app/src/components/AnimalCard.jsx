// src/components/AnimalCard.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './AnimalCard.css'; // Importando o CSS para estilização
import '../data/animais.json'; // Importando os dados dos animais

const AnimalCard = ({ animal }) => {
  return (
    <div className="animal-card">
      <h3>{animal.nome}</h3>
      <img src={animal.imagem_animal} alt={animal.nome} />
      <p>{animal.especie} - {animal.raca}</p>
      <p>{animal.sexo} | {animal.idade_aproximada}</p>
      <p>{animal.descricao}</p>
      <p><strong>{animal.cidade} - {animal.estado}</strong></p>
      <Link to={`/animal/${animal.id_animal}`}>Ver detalhes</Link>

    </div>
  );
};

export default AnimalCard;