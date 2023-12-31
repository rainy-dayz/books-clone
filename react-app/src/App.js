import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import Books from "./components/Books";
import SingleGenre from "./components/SingleGenre";
import SingleBook from "./components/SingleBook";
import Cart from "./components/Cart";
import WishList from "./components/WishLists";
import Loading from "./components/Loading";


function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/" >
            <Books />
          </Route>
          <Route exact path="/carts" >
            <Cart />
          </Route>
          <Route exact path="/wishlists" >
            <WishList />
          </Route>
          <Route exact path="/genres/:genreId" >
            <SingleGenre />
          </Route>
          <Route exact path="/books/:bookId" >
            <SingleBook />
          </Route>
         
        </Switch>
      )}
    </>
  );
}

export default App;
