import { useEffect, useState } from 'react'
import RestaurantCard from './RestaurantCard'
import NavBar from './NavBar'

function RestaurantList({restaurants}){
    const restaurantCards = restaurants.map(restaurant => (
        <RestaurantCard 
            key = {restaurant.id}
            name = {restaurant.name}
            cuisine_type = {restaurant.cuisine_type}
            image = {restaurant.image}
            id = {restaurant.id}
        />
    ))
    return (
        <div className='app'>
            <NavBar />
            <h1>Restaurants</h1>
            <ul className='cards'>
                {restaurantCards}
            </ul>
        </div>
    )
}


export default RestaurantList