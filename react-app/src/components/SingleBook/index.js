import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { thunkGetSingleBook, thunkUpdateBook } from '../../store/book'
import { thunkCreateCart, thunkEditCart, thunkGetCart, thunkGetSingleCart } from '../../store/cart'
import OpenModalButton from '../OpenModalButton'
import SignupFormModal from '../SignupFormModal'
import ProfileButton from '../Navigation'
import Reviews from '../Reviews'
import './singlebook.css'
import StarRatingSingleReview from '../Reviews/starRatingSingleReview'




function SingleBook() {
    const dispatch = useDispatch()
    let genre = useSelector(state => Object.values(state.genres.singleGenre))
    let user = useSelector(state => (state.session.user))
    let book = useSelector(state => (state.book.singleBook))
    let book2 = useSelector(state => (state.book.singleBook.reviews))
    let cartAll = useSelector(state => Object.values(state.carts.allCarts))
    let cart=useSelector(state => (state.carts.singleCart))
    const history = useHistory()
    const { bookId } = useParams()
    // console.log('cart', book2.length )
    const [types, setTypes] = useState(false)
    const [name] = useState(book.name)
    const [author] = useState(book.author)
    const [price] = useState(book.price)
    const [description] = useState(book.description)
    const [bookImage, setImage] = useState(book.bookImage)
    useEffect(() => {
        dispatch(thunkGetSingleBook(bookId))
    }, [bookId])

    // useEffect(() =>{
    //     dispatch(thunkUpdateBook(types,bookId))
    // },[types])
    const addthings=async()=>{
        if(cartAll){
            cartAll.map(cart=>{
                {console.log('carttypes',cart.books.types)}
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

    return (
        <div>
        <div className="singlebookcont">
            <div className='bookimagecont'>
            <img className='booksImageSingleBook' src ={book.book_image}/>
            </div>
        <div className="infoaboutsinglebookcont">
            <div>{book.name}</div>
            <div>by {book.author}</div>
            <p>${book.price}</p>
            <div >{<StarRatingSingleReview stars={book.avgRating} />}</div>
            <div>{book.avgRating} ({book2?.length})       Write a Review Below</div>
            <div className='buttoncontforinglestuff'>
            {book.types == false ?<button style={{color: "blue"}} className="serverInput"
                onClick={() => {setTypes(false)}}>Hardcover</button>
                :<button className="serverInput" style={{color: "grey"}}onClick={()=>alert("Currently out of Stock")} >Hardcover</button>}

            {book.types == true ?<button style={{color: "blue"}} className="serverInput"
                onClick={() => {setTypes(true)}}>Paperback</button>
                :<button className="serverInput" style={{color: "grey"}} onClick={()=>alert("Currently out of Stock")}  >Paperback</button> }
                {user ?(chicken.find((chick) => book.id==chick)
                ?<button onClick={addthings}>+</button>:
                <button onClick={() => {
                    return dispatch(thunkCreateCart(user.id,bookId))
                    .then(()=>{history.push(`/carts`)})
                }}>Add to Cart</button>
                ):<div>Login or Signup to add this book to your cart!</div>}
                </div>
            {/* {!user && <div>Login or Signup to add this book to your cart!</div>} */}
            </div>
        </div>
                <p>{book.description}</p>
        <p>{book.id}</p>
        <h1>Reviews</h1>
        <Reviews />

        </div>
        )
    }

    export default SingleBook
