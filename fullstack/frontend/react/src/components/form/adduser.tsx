import "../../index.css";
import { useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import toast from "react-hot-toast";

import { createUser } from "../../service/Forms.service";
import type { FormData } from "../../types/user";

function Add_User() {

  const navigate = useNavigate();

  const [formData, setFormData] = useState<FormData>({
    name: "",
    email: "",
    dob: "",
  });

  const handleSubmit = async () => {
    try {

      const response = await createUser(formData);

      console.log(response.data);

      toast.success("User created successfully");

     

    } catch (error) {

      console.error(error);

      toast.error("Failed to create user");

    }
  };

  return (
    <div className="bg-gray-900 min-h-screen">

      <div className="flex justify-center items-center min-h-screen">

        <div className="w-96 h-96 bg-gray-200 rounded-lg">

          <div className="flex flex-col items-center">

            <input
              type="text"
              placeholder="Name"
              value={formData.name}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  name: e.target.value,
                })
              }
              className="mt-10 border rounded w-80 px-3 py-2"
            />

            <input
              type="email"
              placeholder="Email"
              value={formData.email}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  email: e.target.value,
                })
              }
              className="mt-10 border rounded w-80 px-3 py-2"
            />

            <input
              type="date"
              value={formData.dob}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  dob: e.target.value,
                })
              }
              className="mt-10 border rounded w-80 px-3 py-2"
            />

            <div className="flex justify-end gap-3 mt-10">

              <button
                className="bg-green-700 text-black px-4 py-2 rounded-lg active:scale-95"
                onClick={handleSubmit}
              >
                Submit
              </button>

              <button
                className="bg-red-700 text-black px-4 py-2 rounded-lg active:scale-95"
                onClick={() => navigate({ to: "/form" })}
              >
                Cancel
              </button>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default Add_User;