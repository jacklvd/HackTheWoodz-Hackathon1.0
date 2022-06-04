import React, { useEffect } from "react";
import { PracGet, PracPost } from "../Data/GetData";
import "../CSS/Login.css";

const Login = () => {

    useEffect(() => {

        PracGet();

    }, [])


    return (
        <>
            <h1>Login</h1>
        </>
    );
}