import { thunkGetReviews } from '../../store/reviews'
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import CreateReview from '../Create Review'





function Reviews() {
    const dispatch = useDispatch()
    let reviewsAll = useSelector(state => Object.values(state.reviews.allReviews))
    const [openModal,setOpenModal] = useState(false)
    const history = useHistory()
    const {bookId} =useParams()
    console.log(bookId, '-----------------')

    useEffect(() => {
        dispatch(thunkGetReviews(bookId))
    }, [dispatch])


if(!reviewsAll) return null
    return (
        <div>
            {openModal && <CreateReview closeModal ={setOpenModal} />}
            <button onClick={()=>setOpenModal(true)}>Post Your Review</button>
            {reviewsAll.map(review => {
                return <div key={review.id} >
                    <p>{review.comment}</p>
                    <p>{review.rating}</p>
                    </div>
            })}
        </div>
        )
    }

    export default Reviews
