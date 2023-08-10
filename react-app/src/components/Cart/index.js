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


    return (
        <div>
            {cartAll.map(cart => {
                return <div key={cart.id} >

                    {booksAll.map(book => {
                    return <div key={book.id}>
                        {cart.book_id == book.id && <p>{book.name}</p>}
                        {cart.book_id == book.id && <p>Book Id:{book.id}</p>}
                        {cart.book_id == book.id && <img onClick={() => {history.push(`/books/${book.id}`)}} className="booksImageHomepage" src={book.book_image} />}
                        {cart.book_id == book.id && <p>{book.price}</p>}
                        {cart.book_id == book.id &&<p>Quantity: {cart.quantity}</p>}
                        {cart.book_id == book.id &&<button onClick={async()=> {
                            cart.quantity +=1
                            book.price*=cart.quantity
                        dispatch(thunkEditCart(cart.id,cart.quantity))
                            dispatch(thunkGetSingleCart(cart.id))
                        }}>+</button>}
                        {cart.book_id == book.id &&<button onClick={async()=> {
                            cart.quantity -=1
                            book.price/=cart.quantity
                        dispatch(thunkEditCart(cart.id,cart.quantity))
                            dispatch(thunkGetSingleCart(cart.id))
                        }}>-</button>}
                        {cart.book_id == book.id &&<button onClick={()=>{
                            return dispatch(thunkDeleteCart(cart.id))
                            .then(()=> dispatch(thunkGetCart()))
                            }}>Delete</button>}
                            </div>

})}
</div>
            })}
        </div>
        )
    }

    export default Cart
