// src/components/PublicacaoCard.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './PublicacaoCard.css'; // Importando o CSS para estilização

const PublicacaoCard = ({ publicacao }) => {
  return (
    <div className="publicacao-card">
      <h3>{publicacao.titulo} 🐾</h3>

      {publicacao.imagem_destacada && (
        <img
          src={publicacao.imagem_destacada}
          alt={publicacao.titulo}
          className="publicacao-image"
        />
      )}

      <p>{publicacao.conteudo}</p>

      <Link to={`/publicacao/${publicacao.id_publicacao}`} className="publicacao-link">
        Ver mais detalhes
      </Link>
    </div>
  );
};

export default PublicacaoCard;
