import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

function RestaurantCard({key, id, name, cuisine_type, image}){





    return (
        <li className='card'>
            <img src = {image} />
            <h4>{name}</h4>
            <h6>{cuisine_type}</h6>
            <Link key={id} to={`/restaurants/${id}`}>
                <br></br>
                Reviews
            </Link>

        </li>
    )
}

export default RestaurantCard