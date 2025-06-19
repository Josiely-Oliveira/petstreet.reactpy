// src/components/NavBar.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css';

const NavBar = () => {
  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/animais">Animais</Link>
        </li>
        <li>
          <Link to="/publicacoes">Publicações</Link>
        </li>
        <li>
          <Link to="/usuarios">Usuários</Link>
        </li>
        <li>
          <Link to="/cadastro-usuario">Cadastrar Usuário</Link>
        </li>
        <li>
          <Link to="/cadastro-animal">Cadastrar Animal</Link>
        </li>
        <li>
          <Link to="/login">Login</Link>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;
