// src/pages/PublicationDetail.jsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import publicationsData from '../data/publicacoes.json'; // Importando os dados das publicações
import './PublicationDetail.css';

const PublicationDetail = () => {
  const { id_publicacao } = useParams();
  const [publicacao, setPublicacao] = useState(null);

  useEffect(() => {
    const pub = publicationsData.find(pub => pub.id_publicacao === parseInt(id_publicacao));
    setPublicacao(pub);
  }, [id_publicacao]);

  if (!publicacao) return <div>Publicação não encontrada</div>;

  return (
    <div className="publication-detail-container">
      <h1>{publicacao.titulo}</h1>
      <p>{publicacao.conteudo}</p>
      {publicacao.imagem_destacada && (
        <img src={publicacao.imagem_destacada} alt={publicacao.titulo} />
      )}
    </div>
  );
};

export default PublicationDetail;
