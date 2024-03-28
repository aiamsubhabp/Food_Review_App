import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import NavBar from './components/NavBar'
import RestaurantList from './components/RestaurantList'

function App() {
  const [restaurants, setRestaurants] = useState([])

  useEffect(() => {
    fetch('/api/restaurants')
    .then(r => r.json())
    .then(data => setRestaurants(data))
  }, [])


  return (
    <div>
      <RestaurantList restaurants={restaurants}/>
      <h1>I am the home page</h1>
    </div>
  )
}

export default App
