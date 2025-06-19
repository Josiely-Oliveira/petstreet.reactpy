import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import animalsData from '../data/animais.json';
import usersData from '../data/usuarios.json';
import './AnimalDetail.css';

const AnimalDetail = () => {
  const { id_animal } = useParams();
  const [animal, setAnimal] = useState(null);
  const [owner, setOwner] = useState(null);

  useEffect(() => {
    const animalDetails = animalsData.find(animal => animal.id_animal === parseInt(id_animal));

    if (animalDetails) {
      setAnimal(animalDetails);

      const ownerDetails = usersData.find(user => user.id_usuario === animalDetails.id_usuario_dono);
      setOwner(ownerDetails);
    }
  }, [id_animal]);

  if (!animal) return <div>Animal não encontrado</div>;

  return (
    <div className="animal-detail-container">
      <h1>{animal.nome}</h1>
      <div className="animal-detail-info">
        <p><strong>Espécie:</strong> {animal.especie}</p>
        <p><strong>Raça:</strong> {animal.raca}</p>
        <p><strong>Sexo:</strong> {animal.sexo}</p>
        <p><strong>Idade Aproximada:</strong> {animal.idade_aproximada}</p>
        <p><strong>Descrição:</strong> {animal.descricao}</p>
        <p><strong>Localização:</strong> {animal.cidade} - {animal.estado}</p>
      </div>

      {owner ? (
        <div className="owner-section">
          <h2>Dono do Animal</h2>
          <p><strong>Nome:</strong> {owner.nome}</p>
          <p><strong>Email:</strong> {owner.email}</p>
          <p><strong>Telefone:</strong> {owner.telefone}</p>
        </div>
      ) : (
        <p>Dono não encontrado.</p>
      )}
    </div>
  );
};

export default AnimalDetail;
