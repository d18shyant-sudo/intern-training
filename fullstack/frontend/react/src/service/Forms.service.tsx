import axios from "axios";
import type { FormData,login } from "../types/user";

const API_URL = "http://localhost:8000/api/v1";

export const createUser = async (data: FormData) => {
  return await axios.post(`${API_URL}/postdetail`, data);
};

export const getUsers = async () => {
  const response = await axios.get(
    `${API_URL}/getdetail`
  );

  return response.data;
};
export const deleteUser = async (email: string) => {
  return await axios.delete(
    `${API_URL}/deletedetail/${email}`
  );
};
export const updateUser = async (email:string,data:FormData) => {
    return await axios.put(
        `${API_URL}/updatedetail/${email}`,
        data
    );
};
export const signin = async (data:login) => {
  const response =  await axios.post(`${API_URL}/login`, data);
  return response;
};
export const signup = async (data:login) => {
  const response =  await axios.post(`${API_URL}/sign_up`, data);
  return response;
};
