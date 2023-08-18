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
const QuickAdd = ({ closeModal,book}) => {
  const dispatch = useDispatch();
  const history = useHistory();
  const {bookId} =useParams()
  const user= useSelector(state => state.session.user)



  return (
    <div className="modals" >
            <div className="backg" >

     </div>
          </div>

              );
            };
export default QuickAdd;
