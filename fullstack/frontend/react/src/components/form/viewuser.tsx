import { Pencil, Trash2, ArrowLeft } from "lucide-react";
import { useNavigate } from "@tanstack/react-router";
import { useEffect, useState } from "react";

import { getUsers, deleteUser } from "../../service/Forms.service";
import type { User } from "../../types/user";
import toast from "react-hot-toast";

import "../../index.css";


function ViewUsers() {

  const navigate = useNavigate();

  const [users, setUsers] = useState<User[]>([]);

  const [showConfirm, setShowConfirm] = useState(false);

  const [selectedEmail, setSelectedEmail] = useState("");



  useEffect(() => {

    const fetchUsers = async () => {

      try {

        const data = await getUsers();

        setUsers(data);

      } catch(error) {

        console.error(
          "Failed to fetch users",
          error
        );

        toast.error(
          "Failed to load users"
        );

      }

    };


    fetchUsers();

  }, []);





  const handleDelete = async (email:string) => {

    try {

      await deleteUser(email);


      toast.success(
        "User deleted successfully"
      );


      setUsers(
        users.filter(
          (user)=> user.email !== email
        )
      );


    } catch(error) {


      console.error(error);


      toast.error(
        "Failed to delete user"
      );

    }

  };





  return (

    <div className="min-h-screen bg-gray-800 p-8">


      {/* Top bar */}

      <div className="flex justify-end w-full h-10 bg-yellow-300">


        <button

          onClick={() => navigate({to:"/form"})}

          className="px-3 m-2 bg-gray-300 rounded-lg active:scale-95"

        >

          <ArrowLeft className="text-black"/>

        </button>


      </div>





      <h1 className="text-white text-3xl font-bold mb-6">

        Users

      </h1>





      <div className="bg-white rounded-lg shadow-lg overflow-hidden">



        <div className="h-[500px] overflow-y-auto">



          <table className="w-full">



            <thead className="bg-gray-700 text-white sticky top-0">


              <tr>

                <th className="p-4 text-left">
                  Name
                </th>


                <th className="p-4 text-left">
                  DOB
                </th>


                <th className="p-4 text-left">
                  Email
                </th>


                <th className="p-4 text-center">
                  Actions
                </th>


              </tr>


            </thead>





            <tbody>



              {users.map((user)=>(


                <tr

                  key={user.id}

                  className="border-b hover:bg-gray-100"

                >


                  <td className="p-4">

                    {user.name}

                  </td>



                  <td className="p-4">

                    {user.DOB}

                  </td>



                  <td className="p-4">

                    {user.email}

                  </td>





                  <td className="p-4">


                    <div className="flex justify-center gap-3">





                      {/* Edit button */}

                      <button

                        className="p-2 bg-blue-500 text-white rounded-lg hover:scale-105 active:scale-95"

                        onClick={()=>

                          navigate({

                            to:`/edit_user/${user.email}`

                          })

                        }

                      >

                        <Pencil size={18}/>


                      </button>







                      {/* Delete button */}

                      <button


                        className="p-2 bg-red-500 text-white rounded-lg hover:scale-105 active:scale-95"


                        onClick={()=>{


                          setSelectedEmail(user.email);

                          setShowConfirm(true);


                        }}


                      >


                        <Trash2 size={18}/>


                      </button>




                    </div>


                  </td>



                </tr>



              ))}



            </tbody>



          </table>



        </div>



      </div>








      {/* Confirmation Modal */}



      {showConfirm && (



        <div className="fixed inset-0 bg-black/50 flex items-center justify-center">



          <div className="bg-white rounded-lg p-6 w-96 shadow-lg">



            <h2 className="text-xl font-bold">

              Confirm Delete

            </h2>




            <p className="mt-4 text-gray-600">

              Are you sure you want to delete this user?

            </p>




            <div className="flex justify-end gap-3 mt-6">





              <button

                className="px-4 py-2 bg-gray-400 rounded-lg"

                onClick={()=>{

                  setShowConfirm(false);

                  setSelectedEmail("");

                }}

              >

                Cancel

              </button>







              <button

                className="px-4 py-2 bg-red-500 text-white rounded-lg"

                onClick={()=>{


                  handleDelete(selectedEmail);


                  setShowConfirm(false);

                  setSelectedEmail("");

                }}

              >

                Delete

              </button>




            </div>



          </div>



        </div>



      )}



    </div>


  );

}


export default ViewUsers;