import React from 'react'
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { useParams } from "react-router-dom";
// import "../Create Review/reviewModal.css"
import StarRatingInput from '../Create Review/StarInputRating';
import { thunkGetReviews } from '../../store/reviews';
import { thunkEditReview } from '../../store/reviews';
// import { useSelector } from "react-redux";
const EditReview = ({ closeModal1,review }) => {
  const [comment, setComment] = useState(review.comment)
  const [rating, setRating] = useState(review.rating)
  const [error, setErrors] = useState({});
  const dispatch = useDispatch();
  const history = useHistory();
  const {bookId} =useParams()

  // const book =  useSelector(state=> state.book.singleBook)
  // const user= useSelector(state => state.session.user)

  const handleSubmit = async (e) => {
      e.preventDefault();
      // setErrors({});
      // reviews = {comment,rating};
          let reviews = await dispatch(thunkEditReview(review.id,comment,rating));
          await dispatch(thunkGetReviews(bookId))

      // if (reviews.error) {
      //   setErrors(reviews.error);
      // }else {
          closeModal1(false)
      // }
    };
    const onChange = (number) => {
      setRating(number);
    };
    let disable=true
    if(comment.length >9 && rating >= 1){
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
        <button type="submit" disabled={disable}onClick={()=>
          {
          return handleSubmit
          }}>Submit your Review</button>
              <button onClick={()=>
                closeModal1(false)
                }>Cancel</button>
          </div>
       </form>
          </div>

              );
            };
export default EditReview;
