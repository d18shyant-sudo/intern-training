import { useState } from 'react'


interface User {
  name: {
    first: string;
    last: string;
  };
  email: string;
}

function App() {
  const [user, setUser] = useState<User | null>(null);

  const fetchUser = async () => {
    const res = await fetch("https://randomuser.me/api/");
    const data = await res.json();

    setUser(data.results[0]);
  };

  return (
    <div>
      <button onClick={fetchUser}>Fetch User</button>

      {user && (
        <div>
          <p>{user.name.first} {user.name.last}</p>
          <p>{user.email}</p>
        </div>
      )}
    </div>
  );
}

export default App
