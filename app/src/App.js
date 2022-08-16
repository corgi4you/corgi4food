import React, {useState, useEffect} from 'react'
import ButtonLoad from './ButtonLoad'

function App() {
  const [data, setData] = useState([{}])
 
  useEffect(() => {
    fetch("/foods/random")
    .then(res => res.json())
    .then(data => {
      setData(data)
      console.log(data)
    })
  }, [])

  return (
    <ButtonLoad/>
  )
}

export default App