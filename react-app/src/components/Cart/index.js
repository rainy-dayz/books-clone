import { thunkDeleteCart, thunkEditCart, thunkGetCart, thunkGetSingleCart } from '../../store/cart'
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { thunkGetBooks } from '../../store/book'




function Cart() {
    const dispatch = useDispatch()
    let cartAll = useSelector(state => Object.values(state.carts.allCarts))
    let booksAll = useSelector(state => Object.values(state.book.allBooks))
    let cart=useSelector(state => (state.carts.singleCart))
    console.log('cart',cart)
    const history = useHistory()

    useEffect(() => {
        dispatch(thunkGetCart())
        dispatch(thunkGetBooks())
    }, [dispatch])


let price1
    return (
        <div>
            <h1>Cart:</h1>
            {cartAll.length ?
            cartAll.toReversed().map(cart => {

                return <div key={cart.id} >
                    <p>{cart.books.name}</p>
                    <img onClick={() => {history.push(`/books/${cart.books.id}`)}} className="booksImageHomepage" src={cart.books.book_image}/>
                    <p>{cart.books.price}</p>
                    <p>Book Id:{cart.books.id}</p>
                    {cart.books.types == false? <p>Hardcover</p>: <p>Paperback</p>}
                    <p>Quantity: {cart.quantity}</p>
                    <button onClick={async()=> {
                            cart.quantity +=1
                        dispatch(thunkEditCart(cart.id,cart.quantity))
                        // dispatch(thunkGetCart())
                    }}>+</button>
                    <button onClick={async()=> {
                        cart.quantity -=1
                       price1 = cart.books.price*cart.quantity
                       dispatch(thunkEditCart(cart.id,cart.quantity))
                    //    dispatch(thunkGetCart())
                    }}>-</button>
                    <button onClick={()=>{
                            return dispatch(thunkDeleteCart(cart.id))
                            .then(()=> dispatch(thunkGetCart()))
                            }}>Delete</button>
</div>
            }): <div>Your Cart is currently empty!</div>}
        </div>
        )
    }

    export default Cart
