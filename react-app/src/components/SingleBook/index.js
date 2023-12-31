import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { clearSingleBook, thunkGetSingleBook, thunkUpdateBook } from '../../store/book'
import { thunkCreateCart, thunkEditCart, thunkGetCart, thunkGetSingleCart } from '../../store/cart'
import OpenModalButton from '../OpenModalButton'
import SignupFormModal from '../SignupFormModal'
import ProfileButton from '../Navigation'
import Reviews from '../Reviews'
import './singlebook.css'
import StarRatingSingleReview from '../Reviews/starRatingSingleReview'
import LoginFormModal from '../LoginFormModal'
import OpenModalButton2 from '../OpenModalButton/index2'

import { thunkCreateWishlist, thunkGetWishlists } from '../../store/wishlists'
import Loading from '../Loading'




function SingleBook() {
    const dispatch = useDispatch()
    let genre = useSelector(state => Object.values(state.genres.singleGenre))
    let user = useSelector(state => (state.session.user))
    let book = useSelector(state => (state.book.singleBook))
    let book2 = useSelector(state => (state.book.singleBook?.reviews))
    let cartAll = useSelector(state => Object.values(state.carts.allCarts))
    let wishAll = useSelector(state => Object.values(state.wishlists.allWishlists))
    let cart=useSelector(state => (state.carts.singleCart))
    const history = useHistory()
    const { bookId } = useParams()
    const [openModal,setOpenModal] = useState(false)
    const [types, setTypes] = useState(false)

    useEffect(() => {
        dispatch(clearSingleBook())
        dispatch(thunkGetSingleBook(bookId))
        dispatch(thunkGetWishlists())
    }, [bookId])

    const addthings=async()=>{
        if(cartAll){
            cartAll.map(cart=>{
                if(cart.book_id==bookId){
                    dispatch(thunkEditCart(cart.id, cart.quantity+1))
                    history.push(`/carts`)
                }
            })
        }
    }
    const chicken=cartAll.map(order => {
        return order.book_id
    })
    const wishes=wishAll.map(wish => {
        return wish.book_id
    })
if(!book2)return null
    return (
        <div>
        <div className="singlebookcont">
            <div className='bookimagecont'>
            <img className='booksImageSingleBook' src ={book.book_image}/>
{user&&(!wishes.find((chick) => book.id===chick)&&<button className="wishesbttn" onClick={()=>{
    return dispatch(thunkCreateWishlist(user.id,book.id))
    .then(()=>{history.push(`/wishlists`)})
    }}><i className="fa-regular fa-heart"></i> Add to WishList</button>)}
            </div>
        <div className="infoaboutsinglebookcont">
            <div className="titleofbook">{book.name}</div>
            <div className="authorofbook">by {book.author}</div>
            <div className="ratingsininfoofsinglebook">
            <div >{<StarRatingSingleReview stars={book.avgRating} />}</div>
            <div>{Number.parseFloat(book.avgRating).toFixed(2)}</div>
            <div>({book2?.length})</div>
            </div>
            <div className='holderofpriceandtype'>
                {book.types==false?<div className="thetypeoutsidebutton">Hardcover</div>:<div className="thetypeoutsidebutton">Paperback</div>}
            <div className="priceofbook">${book.price}</div>
            </div>
            <div className='buttoncontforinglestuff'>
            {book.types == false ?<button style={{color: "blue"}} className="serverInput2"
                onClick={() => {setTypes(false)}}>Hardcover <span>${book.price}</span></button>
                :<button className="serverInput" style={{color: "grey"}}onClick={()=>alert("Currently out of stock")} >Hardcover <span>${book.price}</span></button>}

            {book.types == true ?<button  className="serverInput2"
                onClick={() => {setTypes(true)}}>Paperback <span>${book.price}</span></button>
                :<button className="serverInput" style={{color: "grey"}} onClick={()=>alert("Currently out of stock")}  >Paperback <span>${book.price}</span></button> }
                </div>
                <div className="addtocartadnshippingcont">
                    <div className='shippingtextcont'>
                    <div>SHIP THIS ITEM <i className="fa-solid fa-truck"></i></div>
                    <div>Guaranteed Free Shipping</div>
                    </div>
                {user ?(chicken.find((chick) => book.id===chick)
                ?<button className="addtocart" onClick={addthings}>Add to Cart Again!</button>:
                <button className="addtocart"onClick={() => {
                    return dispatch(thunkCreateCart(user.id,bookId))
                    .then(()=>{history.push(`/carts`)})
                }}>Add to Cart</button>
                ):<div>{<OpenModalButton2
                  buttonText="Log In"
                  modalComponent={<LoginFormModal />}
                />} or {<OpenModalButton2
                      buttonText="Sign Up"
                      style={{color:'blue'}}
                      modalComponent={<SignupFormModal />}
                    />} to add this book to your cart!</div>}
                    </div>
            </div>
        </div>
                <div className='descboxcont'>
                   <div className='thisisoverview'>Overview</div>

                <div className='descwords'>{book.description}</div>
                </div>


        <Reviews />

        </div>
        )
    }

    export default SingleBook
