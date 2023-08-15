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
        dispatch(thunkGetSingleCart(cart.id))
       dispatch(thunkGetBooks())
    }, [])

let records =Object.values(cartAll)
console.log('recrod',records)
const checkout = async(record)=>{
    records.forEach(async(record)=>{
    await dispatch(thunkEditCart(record.id,0))
})
}
    let total=0
    return (
        <div>
            <h1>Cart:</h1>
            {cartAll.length ?
            cartAll.toReversed().map(cart => {
                total+=cart.quantity*cart.books.price
                return <div key={cart.id} >
                    <p>{cart.books.name}</p>
                    <img onClick={() => {history.push(`/books/${cart.books.id}`)}} className="booksImageHomepage" src={cart.books.book_image}/>
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
                    //    price1 = cart.books.price*cart.quantity
                       dispatch(thunkEditCart(cart.id,cart.quantity))
                    //    dispatch(thunkGetCart())
                    }}>-</button>
                    <button onClick={()=>{
                        return dispatch(thunkDeleteCart(cart.id))
                        .then(()=> dispatch(thunkGetCart()))
                    }}>Delete</button>
                    {/* <p>{price1.push(cart.books.price *cart.quantity)}</p>
                    {console.log('price1',price1)} */}
                    {/* <p>{sum}</p> */}
</div>
            }): <div>Your Cart is currently empty!</div>}
            <button onClick={checkout}>Checkout</button>
            <div>Total</div>
            <p>{total.toFixed(2)}</p>
            {/* <button onClick={()=>{
                return dispatch(thunkDeleteWholeCart())
                .then(()=> dispatch(thunkGetCart()))}}>Checkout</button> */}
        </div>
        )
    }

    export default Cart
