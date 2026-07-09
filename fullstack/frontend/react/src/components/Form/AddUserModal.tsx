import { useState } from "react";
import toast from "react-hot-toast";
import { createUser } from "../service/Forms.service";
import type { FormData } from "../types/user";

type Props = {
  onClose: () => void;
};

export default function AddUserModal({
  onClose,
}: Props) {
  const [formData, setFormData] =
    useState<FormData>({
      name: "",
      email: "",
      dob: "",
    });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (
    e: React.FormEvent<HTMLFormElement>
  ) => {
    e.preventDefault();

    try {
      await createUser(formData);

      toast.success(
        "User added successfully"
      );

      onClose();
    } catch {
      toast.error(
        "Failed to add user"
      );
    }
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex justify-center items-center">
      <div className="bg-white p-6 rounded">
        <button
          className="float-right"
          onClick={onClose}
        >
          ✕
        </button>

        <form
          onSubmit={handleSubmit}
          className="bg-blue-200 p-6 rounded-lg shadow-2xl w-96"
        >
          <h2 className="text-2xl font-bold mb-4">
            Register
          </h2>

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
    </div>
  );
}