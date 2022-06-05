import axios from "axios";

export const PracGet = async () => {
    const res = await axios.get("http://localhost:8000/projectmanager/projects/");
    const data = await res.data;

    console.log(data);
};


export const PracPost = async () => {

    var bodyFormData = new FormData();

    bodyFormData.append('title', 'title');
    bodyFormData.append('tools', 'also tools');
    bodyFormData.append('description', 'other');

    const res = await axios.post("http://localhost:8000/projectmanager/create/", bodyFormData);
    console.log(res);
    const data = await res.data;
    console.log(data);

};