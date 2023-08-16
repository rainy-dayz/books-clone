import React, { useEffect } from 'react'
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { useParams } from "react-router-dom";
import "./reviewModal.css"
import StarRatingInput from './StarInputRating';
import { thunkGetSingleBook } from '../../store/book';
import { thunkCreateReview } from '../../store/reviews';

// import { useSelector } from "react-redux";
const CreateReview = ({ closeModal,book,user }) => {
  const [comment, setComment] = useState('')
  const [rating, setRating] = useState(1)
  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState(false);
  const dispatch = useDispatch();
  const history = useHistory();


  const handleSubmit = async (e) => {
      e.preventDefault();
      // setErrors({});
      const data = {comment,rating, user_username:user.username};
          let reviews = await dispatch(thunkCreateReview(data,user.id,book.id));
          await dispatch(thunkGetSingleBook(book.id))
          closeModal(false)

    };
    const onChange = (number) => {
      setRating(number);
    };
    let disable=true
    if(comment.length >5 && rating >= 1){
       disable=false
    }
  return (
    <div className="modals" >
      <form onSubmit={handleSubmit}>
            <div className="backg" >
        <h2>{`How was the book?`}</h2>

        <label>
          <textarea
          rows="4" cols="50"
            placeholder="Leave your review here, it must be longer than 6 characters..."
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
