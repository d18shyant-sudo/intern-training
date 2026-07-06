import axios from "axios";

const API_URL: string = "http://localhost:8000/api/v1/postdetail";

type UserData = {
  name: string;
  email: string;
  dob: string;
};

export const createUser = async (data: UserData) => {
  return await axios.post(API_URL, data);
};