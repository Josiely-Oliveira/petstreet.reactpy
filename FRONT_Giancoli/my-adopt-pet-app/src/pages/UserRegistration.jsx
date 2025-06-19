// src/pages/UserRegistration.jsx
import React, { useState } from 'react';
import './UserRegistration.css'; // Importando o CSS para estilização

const UserRegistration = () => {
  const [formData, setFormData] = useState({
    nome: '',
    cpf_ou_cnpj: '',
    tipo_usuario: 'pessoa_fisica', // Por padrão, pessoa física
    email: '',
    senha: '',
    telefone: '',
    endereco: '',
    cidade: '',
    estado: '',
    cep: '',
    foto_perfil: '', // Foto de perfil opcional
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleFileChange = (e) => {
    const { name, files } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: files[0],
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Cadastro de Usuário:', formData);

    // Aqui você pode integrar com uma API para salvar o usuário no banco de dados
    alert('Cadastro realizado com sucesso!');
  };

  return (
    <div className="form-container">
      <h1>Cadastro de Usuário</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Nome:</label>
          <input
            type="text"
            name="nome"
            value={formData.nome}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>CPF ou CNPJ:</label>
          <input
            type="text"
            name="cpf_ou_cnpj"
            value={formData.cpf_ou_cnpj}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Tipo de Usuário:</label>
          <select
            name="tipo_usuario"
            value={formData.tipo_usuario}
            onChange={handleChange}
            required
          >
            <option value="pessoa_fisica">Pessoa Física</option>
            <option value="instituicao">Instituição</option>
          </select>
        </div>

        <div>
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Senha:</label>
          <input
            type="password"
            name="senha"
            value={formData.senha}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Telefone:</label>
          <input
            type="text"
            name="telefone"
            value={formData.telefone}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Endereço:</label>
          <input
            type="text"
            name="endereco"
            value={formData.endereco}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Cidade:</label>
          <input
            type="text"
            name="cidade"
            value={formData.cidade}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Estado:</label>
          <input
            type="text"
            name="estado"
            value={formData.estado}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>CEP:</label>
          <input
            type="text"
            name="cep"
            value={formData.cep}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Foto de Perfil:</label>
          <input
            type="file"
            name="foto_perfil"
            onChange={handleFileChange}
          />
        </div>

        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
};

export default UserRegistration;