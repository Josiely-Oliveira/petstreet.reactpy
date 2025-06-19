// src/pages/PublicacoesPage.jsx
import React, { useEffect, useState } from 'react';
import PublicacaoCard from '../components/PublicacaoCard';
import publicationsData from '../data/publicacoes.json'; // Importando os dados das publicações
import './PublicacoesPage.css'; // Importando o CSS para estilização

const PublicacoesPage = () => {
  const [publications, setPublications] = useState([]);

  useEffect(() => {
    setPublications(publicationsData);
  }, []);

  return (
    <div>
      <h1>Publicações de Adoção</h1>
      <div className="publicacao-list">
        {publications.map(publicacao => (
          <PublicacaoCard key={publicacao.id_publicacao} publicacao={publicacao} />
        ))}
      </div>
    </div>
  );
};

export default PublicacoesPage;