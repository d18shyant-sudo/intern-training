import { useEffect, useState } from "react";
import { getUsers } from "../service/Forms.service";
import type { User } from "../types/user";

type Props = {
  onClose: () => void;
};

export default function UserListModal({
  onClose,
}: Props) {

  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {

    const loadUsers = async () => {
      try {
        const data = await getUsers();
        setUsers(data);
      } catch(error) {
        console.log(error);
      }
    };

    loadUsers();

  }, []);

  return (
    <div className="fixed inset-0 bg-black/50 flex justify-center items-center">
      <div className="bg-white p-6 rounded-lg">
        <button
          className="float-right"
          onClick={onClose}
        >
          ✕
        </button>

        <h2 className="text-xl font-bold mb-4">
          Users List
        </h2>

        <table className="border-collapse border border-black">
          <thead>
            <tr>
              <th className="border border-black px-4 py-2">
                Name
              </th>
              <th className="border border-black px-4 py-2">
                Email
              </th>
              <th className="border border-black px-4 py-2">
                DOB
              </th>
            </tr>
          </thead>

          <tbody>
            {users.map((user, index) => (
              <tr key={index}>
                <td className="border border-black px-4 py-2">
                  {user.name}
                </td>

                <td className="border border-black px-4 py-2">
                  {user.email}
                </td>

                <td className="border border-black px-4 py-2">
                  {user.DOB}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}