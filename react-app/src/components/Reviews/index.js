import { thunkDeleteReview, thunkGetReviews } from '../../store/reviews'
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import CreateReview from '../Create Review'
import EditReview from '../EditReview'






function Reviews() {
    const dispatch = useDispatch()
    let reviewsAll = useSelector(state => Object.values(state.reviews.allReviews))
    const book =  useSelector(state=> state.book.singleBook)
    const user= useSelector(state => state.session.user)
    const [openModal,setOpenModal] = useState(false)
    const [openModal1,setOpenModal1] = useState(false)
    const history = useHistory()
    const {bookId} =useParams()
    console.log(bookId, '-----------------')

    useEffect(() => {
        dispatch(thunkGetReviews(bookId))
    }, [dispatch])


if(!reviewsAll) return null
    return (
        <div>
            {openModal && <CreateReview closeModal ={setOpenModal} book={book} user={user}/>}
            {reviewsAll.map(review => {
                return <div key={review.id} >
                    {user && user.id !== review.user_id&&<button onClick={()=>setOpenModal(true)}>Post Your Review</button>}
                    {openModal1 && <EditReview closeModal1 ={setOpenModal1} review={review}/>}
                    <p>{review.comment}</p>
                    <p>{review.rating}</p>
                    {user && user.id == review.user_id &&<button onClick={()=>setOpenModal1(true)}>Edit Your Review</button>}
                    {user && user.id == review.user_id &&<button onClick={()=> {
                        return dispatch(thunkDeleteReview(review.id))
                            .then(()=>dispatch(thunkGetReviews(bookId)))
                    }}>Delete</button>}
                    </div>
            })}
        </div>
        )
    }

    export default Reviews
