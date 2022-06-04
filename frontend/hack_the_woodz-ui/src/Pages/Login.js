import React, { useEffect } from "react";
import { PracGet, PracPost } from "../Data/GetData";
import { Store } from 'react-notifications-component';
import "../CSS/Login.css";
import 'animate.css/animate.min.css';


// Store.addNotification({
//     title: "Failed",
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



const Login = () => {

    useEffect(() => {

        PracGet();

    }, [])

    return (
        <>
            <h1>Hello World</h1>
        </>
    );
}

export default Login;