import React from 'react';
import { ReactNotifications } from 'react-notifications-component'
import './App.css';
import 'react-notifications-component/dist/theme.css'
import Login from "./Pages/Login";

function App() {
  return (
    <>
      <ReactNotifications />
      <Login />
    </>
  );
}

export default App;
