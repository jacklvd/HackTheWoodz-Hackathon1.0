import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../CSS/Login.css";
import { Store } from 'react-notifications-component';
import 'animate.css/animate.min.css';
import 'react-notifications-component/dist/theme.css'


const Login = ({ setOverlays }) => {

    const [loginState, setLoginState] = useState({"username": '', "password": ''});

    const handleSubmit = (e) => {

        e.preventDefault();
        // Store.addNotification({
        //     title: "Login Failed",
        //     message: "Username or Password incorrect",
        //     type: "danger",
        //     insert: "top",
        //     container: "top-right",
        //     animationIn: ["animate__animated", "animate__fadeIn"],
        //     animationOut: ["animate__animated", "animate__fadeOut"],
        //     dismiss: {
        //         duration: 4000,
        //         onScreen: false
        //     }
        // });

        // setOverlays({loading: true, background: true});
    }

    return (
        <div className="login-wrapper">
            <div className="login-box">
                <h4>Sign In</h4>
                <p>or <Link className="create-account-link" to="./create-account">create an account</Link></p>
                <form onSubmit={(e) => handleSubmit(e)}>
                    <input value={loginState.username} onChange={(e) => setLoginState({...loginState, "username": e.target.value})} type="text" placeholder="Username" required />
                    <br />
                    <input value={loginState.password} onChange={(e) => setLoginState({...loginState, "password": e.target.value})} type="password" placeholder="Password" required autoComplete="on" />
                    <br />
                    <button className="login-btn">Sign In</button>
                </form>
            </div>
            <p className="forgot-p">Fogot Password? <span className="forgot-btn">Reset Password</span></p>
        </div>
    );
}

export default Login;