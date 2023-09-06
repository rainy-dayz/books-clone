import { thunkDeleteReview, thunkGetReviews } from '../../store/reviews'
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import CreateReview from '../Create Review'
import EditReview from '../EditReview'
import StarRatingSingleReview from './starRatingSingleReview'
import { thunkGetSingleBook } from '../../store/book'
import './reviews.css'
import { thunkCreateLikes, thunkDeleteLikes, thunkGetLikes } from '../../store/likes'





function Reviews() {
    const dispatch = useDispatch()
    let reviewsAll = useSelector(state => Object.values(state.reviews.allReviews))
    let likesAll = useSelector(state => (state.likes.allLikes))
    const book =  useSelector(state=> state.book.singleBook)
    let book2 = useSelector(state => (state.book.singleBook.reviews))
    const user= useSelector(state => state.session.user)
    // const user2= useSelector(state => state.session.user.reviews)
    const [openModal,setOpenModal] = useState(false)
    const [openModal1,setOpenModal1] = useState(false)
    const history = useHistory()
    const {bookId} =useParams()
    console.log(reviewsAll, '-----------------')

    useEffect(() => {
        dispatch(thunkGetReviews(bookId))
    }, [dispatch,bookId])
    // useEffect(() => {
    //     dispatch(thunkGetLikes(bookId))
    // }, [bookId])
    let createReviewButton = false
    reviewsAll.map((review)=> {
        console.log('reviewwewant',review)
        return (
         !user || review.user_id == user.id ? createReviewButton = false : createReviewButton= true
        )
    })
    // if(!likesAll)return null
    // if(!user)return



if(!reviewsAll) return null
let chicken

    return (
        <div className='holderofthereviews'>
            <div className="holderoftheheadofcustomerreviews">
            <div className="reviewheades"><span>Customer Reviews</span></div>
            </div>
            <div className='individualsarehere'>
            {openModal && <CreateReview closeModal ={setOpenModal} book={book} user={user}/>}
            <div className="overallRatingandpostingofreview">
            <div className="displayofavgratingperbook">{<StarRatingSingleReview stars={book.avgRating} />} </div>
            <div>{Number.parseFloat(book.avgRating).toFixed(2)}</div>
            <div>({book2?.length})</div>
            {user && !reviewsAll.find(review=> review.user_id === user?.id)?<button className="checkoutbttn2"onClick={()=>setOpenModal(true)}>Post Your Review</button>:null}
            {user && !reviewsAll.length ?<button className="checkoutbttn2"onClick={()=>setOpenModal(true)}>Post Your Review</button>:null }
            </div>
            {reviewsAll.toReversed().map(review => {
                return <div className="eachreview" key={review.id} >
                    {openModal1 && user && user.id == review.user_id &&<EditReview closeModal1 ={setOpenModal1} review={review} comments={review.comment} ratings={review.rating}/>}
                    <div className="userandlikes">
                    <div className='userwhomadereview'>{review.user_username}</div>
                    <div>Likes:{review.likes_count}</div>
                    </div>
                    <div className='meep'>
                        <div className="meepJR">
                    <div >{<StarRatingSingleReview stars={review.rating} />} </div>
                    <div>~ {`${review.created_at.slice(8,11)} ${review.created_at.slice(5,7)}, ${review.created_at.slice(12,17)}`}</div>
                    </div>
                    <div className="reviewcomment">{review.comment}</div>
                    <div className="editanddeletecontreview">
                    {user && user.id == review.user_id &&<button className="openingoftheeditmodal" onClick={()=>setOpenModal1(true)}>Edit Your Review</button>}
                    {user && user.id == review.user_id &&<button className="reviewwillenterthevoid"onClick={()=> {
                        dispatch(thunkDeleteReview(review.id))
                        .then(()=>dispatch(thunkGetReviews(bookId)))
                        .then(()=>dispatch(thunkGetSingleBook(bookId)))
                    }}>Delete</button>}
                                <script>{chicken=review.likes.map(like => like.user_id)}</script>
                    {user && (chicken.find((chick) => user.id ==chick)|| review.user_id==user.id?null: <button className="openingoftheeditmodal" onClick={()=>{
                        dispatch(thunkCreateLikes(review.id))
                        .then(()=>dispatch(thunkGetReviews(bookId)))
                        }}>Like</button>)}

                                {user &&review.likes.map(like =>{
                                    return <>
                            {review?.id==like?.review_id && user.id == like?.user_id ?<button className="reviewwillenterthevoid" onClick={()=>{
                                dispatch(thunkDeleteLikes(like.id))
                                .then(()=>dispatch(thunkGetReviews(bookId)))
                                .then(()=>dispatch(thunkGetLikes(bookId)))}}>Unlike</button>:null}</>})}
                    </div>
                    </div>

                    </div>

            })}
            </div>
        </div>
        )
    }

    export default Reviews
