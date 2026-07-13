import '../../index.css'
import { SunMoon, BellCheck, LogOut } from 'lucide-react';
import { useNavigate } from '@tanstack/react-router';
import { useState } from 'react';
import toast from 'react-hot-toast';
function Form() {

    const navigate = useNavigate();

    const [darkMode, setDarkMode] = useState(false);


    function toggleTheme() {
        setDarkMode(!darkMode);

        document.documentElement.classList.toggle("dark");
    }


    return (

        <div className="min-h-screen bg-gray-900 dark:bg-black">

            {/* Top bar */}
            <div className="flex justify-end w-full h-10 bg-yellow-300 dark:bg-white">

                <button
                    onClick={toggleTheme}
                    className="px-3 m-2 bg-gray-300 dark:bg-black rounded-lg active:scale-95"
                >
                    <SunMoon className="text-black dark:text-white" />
                </button>


                <button
                    className="px-3 m-2 bg-gray-300 dark:bg-black rounded-lg active:scale-95"
                >
                    <BellCheck className="text-black dark:text-white" />
                </button>


                <button
                    onClick={() => {toast.success("logout successfully");navigate({ to: '/' })}}
                    className="px-3 m-2 bg-gray-300 dark:bg-black rounded-lg active:scale-95"
                >
                    <LogOut className="text-black dark:text-white" />
                </button>

            </div>


            {/* Form */}
            <div className="flex justify-center items-center h-screen">

                <div className="w-96 h-96 bg-gray-200 ">

                    <div className="flex flex-col items-center">

                        <h1 className="font-normal text-4xl mt-10 text-black ">
                            Form
                        </h1>


                        <button
                            className="
                            mt-10 
                            bg-gray-700 
                            dark:bg-black
                            text-black 
                            dark:text-white
                            px-4 py-2 
                            rounded-lg 
                            active:scale-95"onClick={()=>{navigate({to:'/add_user'})}}
                        >
                            ADD USER
                        </button>


                        <button
                            className="
                            mt-10 
                            bg-gray-700 
                            dark:bg-black
                            text-black 
                            dark:text-white
                            px-4 py-2 
                            rounded-lg 
                            active:scale-95"onClick={()=>{navigate({to:'/view_user'})}}
                        >
                            VIEW USER
                        </button>

                    </div>

                </div>

            </div>

        </div>
    );
}

export default Form;