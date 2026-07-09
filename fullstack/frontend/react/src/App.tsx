import { useState } from "react";
import { Toaster } from "react-hot-toast";

import Home from "./components/Form/Home";
import AddUserModal from "./components/Form/AddUserModal";
import UserListModal from "./components/Form/UserListModal";

export default function App() {

  const [showModal, setShowModal] = useState(false);
  const [showUsersModal, setShowUsersModal] = useState(false);


  return (
    <>
      <Toaster />

      <Home
        openAddUser={() => setShowModal(true)}
        openViewUsers={() => setShowUsersModal(true)}
      />


      {showModal ? (
        <AddUserModal
          onClose={() => setShowModal(false)}
        />
      ) : null}


      {showUsersModal ? (
        <UserListModal
          onClose={() => setShowUsersModal(false)}
        />
      ) : null}

    </>
  );
}