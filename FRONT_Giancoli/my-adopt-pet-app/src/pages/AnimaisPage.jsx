// src/pages/AnimaisPage.jsx
import React, { useEffect, useState } from 'react';
import AnimalCard from '../components/AnimalCard';
import animalsData from '../data/animais.json';
import './AnimaisPage.css'; // Importando o CSS para estilização

const AnimaisPage = () => {
  const [animals, setAnimals] = useState([]);

  useEffect(() => {
    setAnimals(animalsData);
  }, []);

  return (
    <div>
      <h1>Animais Disponíveis</h1>
      <div className="animal-list">
        {animals.filter(animal => animal.id_status === 1).map(animal => (
          <AnimalCard key={animal.id_animal} animal={animal} />
        ))}
      </div>
    </div>
  );
};

export default AnimaisPage;