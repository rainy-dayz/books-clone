import React, { useEffect } from 'react'
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { useParams } from "react-router-dom";
import "/Users/emilybreininger/books-clone/react-app/src/components/Create Review/reviewModal.css"

import { thunkGetSingleBook } from '../../store/book';
import { thunkCreateReview } from '../../store/reviews';
import { thunkCreateWishlist } from '../../store/wishlists';

// import { useSelector } from "react-redux";
const CreateWish = ({ closeModal,book,user }) => {
  const [name, setName] = useState('')
  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState(false);
  const dispatch = useDispatch();
  const history = useHistory();


  const onSubmit = async() => {

    const err = await dispatch(thunkCreateWishlist(user.id,book.id,name))

}
let disable=true
if(name.length){
   disable=false
}
return (
    <div className="modals">
        <div className="backg" >
            <h3 className="headerCreateChannel2">Create Channel</h3>
        <label className="channelNameLabel" htmlFor="name">CHANNEL NAME </label>
        <input className="channelInput"type="text"
        placeholder="name"
            value={name}
            onChange={(e) => {
                setName(e.target.value)
            }}
        />
                {/* <div className="errormessagescreatechannel">{Object.values(errors).length > 0 ? errors.error : ''}</div> */}

        <div className="buttonContCreateChannel">
            <div className="cancelChannel" onClick={()=>
                closeModal(false)
                }>Cancel</div>
        <button className="createChannelBtn"
            disabled={disable}
            onClick={(e) => {
                onSubmit()

            }}
        >Create Wishlist</button>
        </div>
        </div>
    </div>
)
}
export default CreateWish;
