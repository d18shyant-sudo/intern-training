import {useState} from "react";
import {useNavigate,useParams} from "@tanstack/react-router";
import {updateUser} from "../../service/Forms.service";
import type {FormData} from "../../types/user";
import toast from "react-hot-toast";


function Edit_User(){

const navigate = useNavigate();


const {email} = useParams({
 from:"/edit_user/$email"
});


const [formData,setFormData] = useState<FormData>({
 name:"",
 email:email,
 dob:""
});



const handleUpdate = async()=>{

 try{

   await updateUser(
      email,
      formData
   );


   toast.success(
     "User updated successfully"
   );


   navigate({
     to:"/view_user"
   });


 }
 catch(error){

   toast.error(
     "Update failed"
   );

 }

};



return (

<div className="bg-gray-900 min-h-screen">

<div className="flex justify-center items-center min-h-screen">

<div className="w-96 h-96 bg-gray-200 rounded-lg">


<div className="flex flex-col items-center">


<input
className="mt-10 border rounded w-80 px-3 py-2"
value={formData.name}
onChange={(e)=>
setFormData({
 ...formData,
 name:e.target.value
})
}
/>


<input
className="mt-10 border rounded w-80 px-3 py-2"
value={formData.email}
onChange={(e)=>
setFormData({
 ...formData,
 email:e.target.value
})
}
/>


<input
type="date"
className="mt-10 border rounded w-80 px-3 py-2"
value={formData.dob}
onChange={(e)=>
setFormData({
 ...formData,
 dob:e.target.value
})
}
/>


<div className="flex gap-3 mt-10">


<button
className="bg-green-700 px-4 py-2 rounded"
onClick={handleUpdate}
>
Done
</button>



<button
className="bg-red-700 px-4 py-2 rounded"
onClick={()=>
navigate({
to:"/view_user"
})
}
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

export default Edit_User;