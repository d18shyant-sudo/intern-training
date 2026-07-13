import "../../index.css";
import { useState } from "react";
import { useNavigate, Link } from "@tanstack/react-router";
import toast from "react-hot-toast";

import type { login } from "../../types/user";
import { signup } from "../../service/Forms.service";

function SignUp() {

  const navigate = useNavigate();

  const [logindata, setlogindata] = useState<login>({
    username: "",
    password: "",
  });

  const handleSubmit = async () => {

    try {

      const response = await signup(logindata);

      console.log(response.data);

      toast.success("Account created successfully");

      navigate({
        to: "/",
      });

    } catch (error) {

      console.error("Signup error:", error);

      toast.error("Signup failed");

    }

  };

  return (

    <div className="bg-gray-900 min-h-screen">

      <div className="flex justify-center items-center min-h-screen">

        <div className="w-96 h-96 bg-gray-200 rounded-lg">

          <div className="flex flex-col items-center">

            <h1 className="font-normal text-4xl mt-10">
              Sign Up
            </h1>

            <input
              type="text"
              placeholder="Username"
              value={logindata.username}
              onChange={(e) =>
                setlogindata({
                  ...logindata,
                  username: e.target.value,
                })
              }
              className="mt-10 border rounded w-80 px-3 py-2"
            />

            <input
              type="password"
              placeholder="Password"
              value={logindata.password}
              onChange={(e) =>
                setlogindata({
                  ...logindata,
                  password: e.target.value,
                })
              }
              className="mt-10 border rounded w-80 px-3 py-2"
            />

            <button
              className="mt-10 bg-gray-700 text-white px-4 py-2 rounded-lg active:scale-95"
              onClick={handleSubmit}
            >
              Sign Up
            </button>

            <p className="mt-6 text-gray-700">

              Already have an account?

              <Link
                to="/"
                className="text-blue-600 underline ml-1"
              >
                Login
              </Link>

            </p>

          </div>

        </div>

      </div>

    </div>

  );
}

export default SignUp;