import { thunkDeleteCart, thunkEditCart, thunkGetCart, thunkGetSingleCart } from '../../store/cart'
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { thunkGetBooks } from '../../store/book'

import './cart.css'



function Cart() {
    const dispatch = useDispatch()
    let cartAll = useSelector(state => Object.values(state.carts.allCarts))
    let booksAll = useSelector(state => Object.values(state.book.allBooks))
    let cart=useSelector(state => (state.carts.singleCart))
    const [openModal,setOpenModal] = useState(false)
    const history = useHistory()

    useEffect(() => {
        dispatch(thunkGetCart())
        dispatch(thunkGetBooks())
    }, [dispatch])

    let records =Object.values(cartAll)
    console.log('recrod',records)
    const checkout = async()=>{
    records.forEach(async(record)=>{
    await dispatch(thunkEditCart(record.id,0))

})
    let popup = document.getElementById('myPopup');
    popup.classList.toggle('show')

    if(popup.classList.contains("show")){ // Check if the popup is shown
     setTimeout(() => popup.classList.remove("show"), 4850) // If yes hide it after 10000 milliseconds
}
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
                    <p>Price: {Number.parseFloat(cart.books.price*cart.quantity).toFixed(2)}</p>
                    <button onClick={async()=> {
                        cart.quantity +=1
                        dispatch(thunkEditCart(cart.id,cart.quantity))
                    }}>+</button>
                    <button onClick={async()=> {
                        cart.quantity -=1
                       dispatch(thunkEditCart(cart.id,cart.quantity))
                    }}>-</button>
                    <button onClick={()=>{
                        return dispatch(thunkDeleteCart(cart.id))
                        .then(()=> dispatch(thunkGetCart()))
                    }}>Delete</button>

</div>
            })
            : <div>Your Cart is currently empty!</div>}
            {cartAll.length >0 && <div className='checkoutDiv'>
            <button onClick={checkout}>Checkout</button>
            <div>SubTotal</div>
            <p>${total.toFixed(2)}</p>
            <div>Shipping:</div>
            <div>FREE</div>
            <div>${total.toFixed(2)}</div>
            <div>Total</div>
            </div>}
            <div className="popuptext" id="myPopup" >
            <div className="modals" >
            <div className="backg2">
            <img className='gifatcheckout'src="https://cdn.dribbble.com/users/470545/screenshots/1848275/gift-3.gif" />
            <h1 className="thankyoumess">Thank you for the order!</h1>
            </div>
            </div>
            </div>
             </div>
        )
    }

    export default Cart
