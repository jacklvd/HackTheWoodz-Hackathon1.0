import axios from "axios";

export const PracGet = async () => {
    const res = await axios.get("http://localhost:8000/PracGet");
    const data = await res.data;

    console.log(data);
};


export const PracPost = async () => {
    const res = axios.post("http://localhost:8000/PracPost", {
        header: {
            auth: "26000045z45",
        },
        body: {
            name: "David",
            age: 10
        }
    });
};