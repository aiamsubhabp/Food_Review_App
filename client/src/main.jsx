// import React from 'react'
// import ReactDOM from 'react-dom/client'
// import App from './App.jsx'
// import './index.css'

// ReactDOM.createRoot(document.getElementById('root')).render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
// )

import React from 'react';
import ReactDOM from 'react-dom';
import { createBrowserRouter, RouterProvider, BrowserRouter } from 'react-router-dom';
import App from './App.jsx';


import './index.css';
import NewReviewForm from './components/NewReviewForm.jsx';
import RestaurantProfilePage from './components/RestaurantProfile.jsx';


const router = createBrowserRouter([
  {
    path: '/',
    element: <App />
  },
  {
    path: '/create_review',
    element: <NewReviewForm />
  },
  {
    path: '/restaurants/:id',
    element: <RestaurantProfilePage />
  },

]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);