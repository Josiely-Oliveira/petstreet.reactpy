// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import AnimaisPage from './pages/AnimaisPage';
import PublicacoesPage from './pages/PublicacoesPage';
import AnimalDetail from './pages/AnimalDetail';
import PublicationDetail from './pages/PublicationDetail';
import UsersPage from './pages/UsersPage';
import UserRegistration from './pages/UserRegistration'; // Nova Rota
import AnimalRegistration from './pages/AnimalRegistration'; // Nova Rota
import NavBar from './components/NavBar';
import Login from './pages/Login';

const App = () => {
  return (
    <Router>
      <div className="App">
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/animais" element={<AnimaisPage />} />
          <Route path="/publicacoes" element={<PublicacoesPage />} />
          <Route path="/animal/:id_animal" element={<AnimalDetail />} />
          <Route path="/publicacao/:id_publicacao" element={<PublicationDetail />} />
          <Route path="/usuarios" element={<UsersPage />} />
          <Route path="/cadastro-usuario" element={<UserRegistration />} /> {/* Rota para cadastro de usuário */}
          <Route path="/cadastro-animal" element={<AnimalRegistration />} /> {/* Rota para cadastro de animal */}
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;