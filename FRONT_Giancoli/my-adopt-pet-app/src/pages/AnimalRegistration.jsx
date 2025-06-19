import React, { useState } from 'react';
import './AnimalRegistration.css'; // Importando o CSS para estilização

const AnimalRegistration = () => {
  const [formData, setFormData] = useState({
    nome: '',
    especie: '',
    raca: '',
    sexo: '',
    idade_aproximada: '',
    descricao: '',
    status: '1', // Status disponível por padrão
    cidade: '',
    estado: '',
    imagem: '', // Imagem do animal
    tipo_registro: '', // Tipo de registro de saúde (vacina, castração, etc.)
    descricao_registro: '', // Descrição do registro de saúde
    veterinario_nome: '', // Nome do veterinário
    documento_anexo: '', // Documento anexo (PDF)
    vacinado: '', // Se o animal foi vacinado
    castrado: '', // Se o animal foi castrado
    vermifugado: '', // Se o animal foi vermifugado
    estado_saude: '', // Estado de saúde (Ótimo, Bom, etc.)
    observacoes: '', // Observações sobre a saúde
    data_registro: '', // Data do registro
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
    console.log('Cadastro de Animal:', formData);

    // Aqui você pode integrar com uma API para salvar o animal no banco de dados
    alert('Animal cadastrado com sucesso!');
  };

  return (
    <div className="form-container">
      <h2>Cadastro de Animal</h2>
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
          <label>Espécie:</label>
          <input
            type="text"
            name="especie"
            value={formData.especie}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Raça:</label>
          <input
            type="text"
            name="raca"
            value={formData.raca}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Sexo:</label>
          <select
            name="sexo"
            value={formData.sexo}
            onChange={handleChange}
            required
          >
            <option value="macho">Macho</option>
            <option value="femea">Fêmea</option>
          </select>
        </div>

        <div>
          <label>Idade Aproximada:</label>
          <input
            type="text"
            name="idade_aproximada"
            value={formData.idade_aproximada}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Descrição:</label>
          <textarea
            name="descricao"
            value={formData.descricao}
            onChange={handleChange}
            required
          ></textarea>
        </div>

        <div>
          <label>Status:</label>
          <select
            name="status"
            value={formData.status}
            onChange={handleChange}
            required
          >
            <option value="1">Disponível</option>
            <option value="2">Adotado</option>
            <option value="3">Em tratamento</option>
          </select>
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

        {/* Campo de Imagem */}
        <div>
          <label>Imagem (Foto do Animal):</label>
          <input
            type="file"
            name="imagem"
            accept="image/*"
            onChange={handleFileChange}
          />
        </div>

        {/* Dados de Saúde do Animal */}
        <div>
          <label>Tipo de Registro de Saúde:</label>
          <select
            name="tipo_registro"
            value={formData.tipo_registro}
            onChange={handleChange}
            required
          >
            <option value="">Selecione</option>
            <option value="vacina">Vacina</option>
            <option value="castracao">Castração</option>
            <option value="vermifugacao">Vermifugação</option>
            <option value="avaliacao">Avaliação</option>
            <option value="tratamento">Tratamento</option>
          </select>
        </div>

        <div>
          <label>Descrição do Registro de Saúde:</label>
          <input
            type="text"
            name="descricao_registro"
            value={formData.descricao_registro}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Nome do Veterinário:</label>
          <input
            type="text"
            name="veterinario_nome"
            value={formData.veterinario_nome}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Documento Anexo (PDF):</label>
          <input
            type="file"
            name="documento_anexo"
            accept="application/pdf"
            onChange={handleFileChange}
          />
        </div>

        <div>
          <label>Vacinado:</label>
          <select
            name="vacinado"
            value={formData.vacinado}
            onChange={handleChange}
            required
          >
            <option value="">Selecione</option>
            <option value="TRUE">Sim</option>
            <option value="FALSE">Não</option>
          </select>
        </div>

        <div>
          <label>Castrado:</label>
          <select
            name="castrado"
            value={formData.castrado}
            onChange={handleChange}
            required
          >
            <option value="">Selecione</option>
            <option value="TRUE">Sim</option>
            <option value="FALSE">Não</option>
          </select>
        </div>

        <div>
          <label>Vermifugado:</label>
          <select
            name="vermifugado"
            value={formData.vermifugado}
            onChange={handleChange}
            required
          >
            <option value="">Selecione</option>
            <option value="TRUE">Sim</option>
            <option value="FALSE">Não</option>
          </select>
        </div>

        <div>
          <label>Estado de Saúde:</label>
          <select
            name="estado_saude"
            value={formData.estado_saude}
            onChange={handleChange}
            required
          >
            <option value="Ótimo">Ótimo</option>
            <option value="Bom">Bom</option>
            <option value="Regular">Regular</option>
            <option value="Ruim">Ruim</option>
          </select>
        </div>

        <div>
          <label>Observações de Saúde:</label>
          <textarea
            name="observacoes"
            value={formData.observacoes}
            onChange={handleChange}
            required
          ></textarea>
        </div>

        <div>
          <label>Data do Registro:</label>
          <input
            type="date"
            name="data_registro"
            value={formData.data_registro}
            onChange={handleChange}
            required
          />
        </div>

        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
};

export default AnimalRegistration;