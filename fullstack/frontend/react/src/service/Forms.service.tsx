import axios from "axios";
import type { FormData } from "../types/user";

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