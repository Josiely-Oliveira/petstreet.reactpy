// src/pages/Login.jsx
import React, { useState } from 'react';
import usersData from '../data/usuarios.json'; // Importando os dados dos usuários
import { useNavigate } from 'react-router-dom';
import './Login.css'; // Importando o CSS estiloso

const Login = () => {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();

    const user = usersData.find(u => u.email === email && u.senha === senha);

    if (user) {
      console.log('Login bem-sucedido!', user);
      localStorage.setItem('usuarioLogado', JSON.stringify(user));
      navigate('/');
    } else {
      setError('Email ou senha incorretos.');
    }
  };

  return (
    <div className="login-container">
      <h2>Login de Usuário</h2>

      {error && <p className="error-message">{error}</p>}

      <form onSubmit={handleLogin}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <div>
          <label>Senha:</label>
          <input
            type="password"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
            required
          />
        </div>

        <button type="submit">Entrar</button>
      </form>
    </div>
  );
};

export default Login;
