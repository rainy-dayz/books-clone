import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { thunkGetSingleBook } from '../../store/book'
import { thunkCreateCart } from '../../store/cart'
import OpenModalButton from '../OpenModalButton'
import SignupFormModal from '../SignupFormModal'
import ProfileButton from '../Navigation'
import Reviews from '../Reviews'




function SingleBook() {
    const dispatch = useDispatch()
    let genre = useSelector(state => Object.values(state.genres.singleGenre))
    let user = useSelector(state => (state.session.user))
    let book = useSelector(state => (state.book.singleBook))
    let cartAll = useSelector(state => Object.values(state.carts.allCarts))
    const history = useHistory()
    const { bookId } = useParams()
    console.log('cart', cartAll)

    useEffect(async() => {
        let book=await dispatch(thunkGetSingleBook(bookId))
    }, [dispatch])

    return (
        <div>
            <p>{book.name}</p>
            <img className='booksImageHomepage' src ={book.book_image}/>
            <p>{book.price}</p>
            <p>{book.description}</p>
            {user ?<button onClick={() => {
                return dispatch(thunkCreateCart(user.id,bookId))
            }}>Add to Cart</button>: <div>Login or Signup to add this book to your cart!</div>}
        <p>{book.id}</p>
        <h1>Reviews</h1>
        <Reviews />

        </div>
        )
    }

    export default SingleBook
