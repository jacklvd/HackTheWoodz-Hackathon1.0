import React, { useState } from 'react';
import { ReactNotifications } from 'react-notifications-component';
import './App.css';
import Login from "./Pages/Login";
import Prac from './Pages/Prac';
import CreateAccount from './Pages/CreateAccount';
import { Routes, Route, useNavigate } from 'react-router-dom';
import Loader from "./Components/Loader";

function App() {

  const navigate = useNavigate();
  const [overlays, setOverlays] = useState({loading: false, background: false});

  return (
    <>
      <ReactNotifications />
      {/* <Routes>
        <Route path="/" element={<Login navigate={navigate} setOverlays={setOverlays} />}></Route>
        <Route path="/create-account" element={<CreateAccount />} />
      </Routes> */}
      <Prac />
      {/* { overlays.loading && <Loader /> }
      { overlays.background && <div id="dark-overlay"></div> } */}
    </>
  );
}

export default App;
