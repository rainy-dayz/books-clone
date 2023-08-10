import React from 'react'
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { useParams } from "react-router-dom";
import "./reviewModal.css"
import StarRatingInput from './StarInputRating';
import { thunkGetSingleBook } from '../../store/book';
import { thunkCreateReview } from '../../store/reviews';

// import { useSelector } from "react-redux";
const CreateReview = ({ closeModal }) => {
  const [comment, setComment] = useState('')
  const [rating, setRating] = useState('')
  const [error, setErrors] = useState({});
  const dispatch = useDispatch();
  const history = useHistory();
//   const {bookId} =useParams()

  const book =  useSelector(state=> state.book.singleBook)
  const user= useSelector(state => state.session.user)
  console.log('user review',user.id)
  console.log('book review',book.id)
  const handleSubmit = async (e) => {
      e.preventDefault();
      setErrors({});
    //   reviews = {comment,rating};
          let reviews = await dispatch(thunkCreateReview(comment,rating,book.id,user.id));
        //   await dispatch(thunkGetSingleBook(book.id))

      if (reviews.error) {
        setErrors(reviews.error);
      }else {
          closeModal(false)
      }
    };
    const onChange = (number) => {
      setRating(parseInt(number));
    };
    let disable=true
    if(comment.length >9 && rating >= 1){
       disable=false
    }
  return (
    <div className="modals" >
      <form onSubmit={handleSubmit}>
            <div className="backg" >
        <h2>How was your Stay?</h2>
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
                closeModal(false)
                }>Cancel</button>
          </div>
       </form>
          </div>

              );
            };
export default CreateReview;
