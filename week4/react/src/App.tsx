import { useState } from 'react'
import { useEffect } from 'react';
import Card from './card'
import RandomJoke from './joke'


function App() {
  const[count,setCount] = useState(0);
  const[theme,setTheme] = useState(false);
  const fruits =["Apple","Banana","Orange","Apple","Orange","Banana"];
  const [fact, setFact] = useState("");

  useEffect(() => {
    fetch("https://catfact.ninja/fact")
      .then((res) => res.json())
      .then((data) => setFact(data.fact))
      .catch((err) => console.log("Error:", err));
  }, []);
  return (
    <div style={theme?{backgroundColor:'black',color:'white'}:{}}>
      <h1>Count {count}</h1>
      <button onClick={()=>setCount(count+1)}>increase</button>
      <button onClick={()=>setCount(count-1)}>decrease</button>
      <h1>Card </h1>
      <Card title="react" description="learnt about the react"/>
      <Card title="angular"description="learnt about the angular"/>
      <Card title="TypeScript"description="learnt about the typescript"/>
     <ul>
      {fruits.map((fruit, index) => (
        <li
          key={index}
          style={{
            color:
              fruit === "Apple"
                ? "red"
                : fruit === "Banana"
                ? "yellow"
                : fruit === "Orange"
                ? "orange"
                : "black"
          }}
        >
          {fruit}
        </li>
      ))}
    </ul>
    <button onClick={()=>setTheme(!theme)}>Toggle </button>
    <RandomJoke/>
     <p>{fact ? fact : "Loading..."}</p>
    </div>
  )

}

export default App
