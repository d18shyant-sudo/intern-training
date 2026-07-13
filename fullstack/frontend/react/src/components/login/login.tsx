import '../../index.css'
import { useState } from 'react';
import { useNavigate } from '@tanstack/react-router';
import type { login } from '../../types/user';
import { signin } from '../../service/Forms.service';
import toast from 'react-hot-toast';
import { Link } from '@tanstack/react-router';
function Login() {

const navigate = useNavigate()
const [logindata, setlogindata] = useState<login>({
    username: "",
    password: "",
  });
  const handleSubmit = async () => {
    console.log("handle submitted")
  try {
    const response = await signin(logindata);

    sessionStorage.setItem("token",response.data.access_token);
    toast.success("login succesful");
    navigate({to:"/form"});
   

  } catch (error) {
    
    console.error("Login error:", error);
    toast.error("Login failed");
  }
};
  return (
    <>
<div className="bg-gray-900 ">


  {/* Center form */}
  <div className="flex justify-center items-center h-screen">
    <div className="w-96 h-96 bg-gray-200 rounded-lg">
      <div className='flex flex-col items-center'>
      <h1 className='font-normal text-4xl mt-10'>Login</h1>
       <input type="text" placeholder="Username"value={logindata.username}
              onChange={(e) =>
               setlogindata({  ...logindata,username: e.target.value,})}className="mt-10 border rounded w-80 px-3 py-2"/>
       <input type="password" placeholder="Password"value={logindata.password}
              onChange={(e) =>
                setlogindata({  ...logindata,password: e.target.value,})}className="mt-10 border rounded w-80 px-3 py-2"/>
        {/* <div className=" fixed  inset-0  bg-black/50 "></div> */}
       {/* <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-black"></div> */}
       <button className='mt-10 bg-gray-700 text-black px-4 py-2 rounded-lg active:scale-95'onClick={handleSubmit}>Submit</button>
      <Link to='/sign_up' className='text-blue-400'>does u have an account?</Link>
      </div>
    </div>
  </div>

</div>
   </>
  );
}


export default Login;
