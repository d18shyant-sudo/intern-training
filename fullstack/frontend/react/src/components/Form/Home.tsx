type Props = {
  openAddUser: () => void;
  openViewUsers: () => void;
};

export default function Home({
  openAddUser,
  openViewUsers,
}: Props) {
  return (
    <div className="flex justify-center items-center h-screen">
      <div className="bg-green-200 rounded-xl w-96 h-96 border-black">
        <h1 className="text-blue-400 m-4 flex justify-center text-4xl font-bold">
          Form
        </h1>

        <div className="mx-34 my-20">
          <button
            onClick={openAddUser}
            className="bg-blue-500 text-white px-4 py-2 mb-5 rounded-lg w-28"
          >
            ADD USER
          </button>

          <button
            onClick={openViewUsers}
            className="bg-blue-500 text-white px-4 py-2 rounded-lg w-28"
          >
            VIEW USER
          </button>
        </div>
      </div>
    </div>
  );
}