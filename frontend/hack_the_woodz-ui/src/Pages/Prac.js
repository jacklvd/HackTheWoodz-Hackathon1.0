import React, { useState, useEffect } from "react";
import { PracGet, PracPost, PracUploadImage } from "../Data/GetData";
import { Store } from 'react-notifications-component';
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



const Prac = () => {


    const [image, setImage] = useState(null);


    const onImageChange = (e) => {
        setImage(e.target.files[0]);
    }

    useEffect(() => {

        // const update = async(image) => {
        //     await PracUploadImage(image);
        // }
        // if(image){
        //     update(image);
        // }
        PracPost();
    }, [image]);

    return (
        <>
           <input type="file" accept="image/*" onChange={onImageChange}/>
        </>
    );
}

export default Prac;