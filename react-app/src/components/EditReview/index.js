import React, { useEffect } from 'react'
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { useParams } from "react-router-dom";
// import "../Create Review/reviewModal.css"
import StarRatingInput from '../Create Review/StarInputRating';
import { thunkGetReviews } from '../../store/reviews';
import { thunkEditReview } from '../../store/reviews';
import { thunkGetSingleBook } from '../../store/book';
// import { useSelector } from "react-redux";
const EditReview = ({ closeModal1,review,comments,ratings}) => {
  const [comment, setComment] = useState(comments)
  const [rating, setRating] = useState(ratings)
  const [error, setErrors] = useState({});
  const dispatch = useDispatch();
  const history = useHistory();
  const {bookId} =useParams()
  const user= useSelector(state => state.session.user)

  // const book =  useSelector(state=> state.book.singleBook)
  // const user= useSelector(state => state.session.user)

  const handleSubmit = async (e) => {
      e.preventDefault();
      // setErrors({});
      const data = {comment,rating,user_username:user.username};


          let reviews = await dispatch(thunkEditReview(review.id,data,bookId));
          await dispatch(thunkGetSingleBook(bookId))

      // if (reviews.error) {
      //   setErrors(reviews.error);
      // }else {
          closeModal1(false)
      // }
    };
    const onChange = (number) => {
      setRating(number);
    };

    useEffect(() => {
      setComment(review.comment)
      setRating(parseInt(review.rating))
  },[review])
    let disable=true
    if(comment.length >6 && rating >= 1){
       disable=false
    }

  return (
    <div className="modals" >
      <form onSubmit={handleSubmit}>
            <div className="backg" >
        <h2>{`How was the book?`}</h2>
        {/* <div className="errors">{error.review}</div> */}
        <label>
          <textarea
          rows="4" cols="50"
            placeholder="Leave your review here ..."
            value={comment}
            onChange={(e) => setComment(e.target.value)}
          />
        </label>
        {/* <div className="errors">{error.stars}</div> */}
        <div className="stars">
        <label className='stars'>
          <StarRatingInput
          disabled={false}
          onChange={onChange}
          rating={rating}
          />
          Stars
        </label>
          </div>
          <div className='bttninreviewmodal'>
              <button className="cancelreviewmodal" onClick={()=>
                closeModal1(false)
                }>Cancel</button>
        <button  className="submitreviewmodal" disabled={disable} type="submit" onClick={handleSubmit}>Submit your Review</button>
          </div>
          </div>
       </form>
          </div>

              );
            };
export default EditReview;
