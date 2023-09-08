import { thunkDeleteCart, thunkEditCart, thunkGetCart } from '../../store/cart'
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { thunkGetBooks } from '../../store/book'

import './cart.css'



function Cart() {
    const dispatch = useDispatch()
    let cartAll = useSelector(state => Object.values(state.carts.allCarts))
    const history = useHistory()

    useEffect(() => {
        dispatch(thunkGetCart())
        // dispatch(thunkGetBooks())
    }, [])

    let records =Object.values(cartAll)
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
        <div className='holderoftheuniverse'>
            <div className="holderoftheheadofcustomerreviews">
            <div className="reviewheades2"><span>My Shopping Cart</span></div>
            </div>
            <div className='contforpositionshoop'>
            <div className='contforpositionshoop2'>
            {cartAll.length ?
            cartAll.toReversed().map(cart => {
                total+=cart.quantity*cart.books.price
                return <div className='bookincart' key={cart.id} >
                    <div className='infoonbookatuhname'>
                    <div className="booknameincare">{cart.books.name}</div>
                    <div>by {cart.books.author}</div>
                    </div>
                    <div classname="everthingelseinhere">
                    <div className='possmiddle'>
                    <img className='possmiddlepic' onClick={() => {history.push(`/books/${cart.books.id}`)}} src={cart.books.book_image}/>
                    <div className="possinnermiddle">
                    {cart.books.types == false? <div>Hardcover</div>: <div>Paperback</div>}
                    <div className='singularprice'>${cart.books.price}</div>
                    <button className='reviewwillenterthevoid' onClick={()=>{
                        return dispatch(thunkDeleteCart(cart.id))
                        .then(()=> dispatch(thunkGetCart()))
                    }}>Delete</button>
                    </div>
                    <div className='quantityprices'>
                    <div >Quantity</div>
                    <div><button className="changequanbtnadd" onClick={async()=> {
                        cart.quantity +=1
                        dispatch(thunkEditCart(cart.id,cart.quantity))
                    }}>+</button>{cart.quantity} <button className="changequanbtnminus" onClick={async()=> {
                        cart.quantity -=1
                       dispatch(thunkEditCart(cart.id,cart.quantity))
                    }}>-</button></div>
                    <div className="priceinbook">${Number.parseFloat(cart.books.price*cart.quantity).toFixed(2)}</div>
                    </div>

                    </div>
                    </div>

</div>
            })
            : <div className="emptymessage">Your Cart is currently empty!</div>}
            </div>
            {cartAll.length >0 && <div className='checkoutDiv'>
            <div className="order-summary">Order Summary</div>

            <div className='ordersummarytinydivs'>
            <div className='wordsintinydiv'>SubTotal</div>
            <div className='wordsintinydiv'>${total.toFixed(2)}</div>
            </div>
            <div className='ordersummarytinydivs'>
            <div className='wordsintinydiv'>Shipping:</div>
            <div className='wordsintinydiv'>FREE</div>
            </div>
            <div className="totalandcheckoutbttn">
            <div className='ordersummarytinydivs2'>
            <div className='wordsintinydiv2'>Order Total:</div>
            <div className='wordsintinydiv2' >${total.toFixed(2)}</div>
            </div>
            <div className="holderofcheckoutbttnonly">
            <button className="checkoutbttn" onClick={checkout}>Checkout</button>
            </div>
            </div>
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
             </div>
        )
    }

    export default Cart
