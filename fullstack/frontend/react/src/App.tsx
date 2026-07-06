import { useState } from "react";
import { createUser } from "./service/Forms.service";
import "./index.css";

type FormData = {
  name: string;
  email: string;
  dob: string;
};

export default function App() {
  const [formData, setFormData] = useState<FormData>({
    name: "",
    email: "",
    dob: ""
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const res = await createUser(formData);
      console.log("Success:", res.data);
    } catch (err) {
      console.log("Error:", err);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-blue-200">
      <form
        onSubmit={handleSubmit}
        className="bg-red-200 p-6 rounded-lg shadow-2xl w-96"
      >
        <h2 className="text-2xl font-bold mb-4">Register</h2>

        <input
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
          className="w-full border border-black rounded px-3 py-2 mb-3"
        />

        <input
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          className="w-full border border-black rounded px-3 py-2 mb-3"
        />

        <input
          name="dob"
          type="date"
          value={formData.dob}
          onChange={handleChange}
          className="w-full border border-black rounded px-3 py-2 mb-4"
        />

        <button className="w-full bg-blue-600 text-white py-2 rounded">
          Submit
        </button>
      </form>
    </div>
  );
}