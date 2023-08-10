const GET_REVIEWS = "reviews/GET_REVIEWS"
const GET_SINGLE_REVIEW = "reviews/GET_SINGLE_REVIEW"
const CREATE_REVIEW = 'reviews/CREATE_REVIEW'
const DELETE_REVIEW= 'reviews/DELETE_REVIEW'
const EDIT_REVIEW = 'reviews/EDIT_REVIEW'

const getReview = (reviews) => ({
    type:GET_REVIEWS,
    data:reviews
})

const getSingleReview = (review) => ({
    type:GET_SINGLE_REVIEW,
    data:review
})
const createReview = (data) => ({
    type:CREATE_REVIEW,
    data
})
const deleteReview = (reviewId) => ({
    type:DELETE_REVIEW,
    data:reviewId
})
const editReview = (reviewId) => ({
    type:EDIT_REVIEW,
    data:reviewId
})

export const thunkGetReviews = (bookId) => async(dispatch) => {
    const res = await fetch(`/api/reviews/${bookId}`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getReview(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}
export const thunkGetSingleReview = (reviewId) => async(dispatch) => {
    const res = await fetch(`/api/reviews/${reviewId}`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getSingleReview(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}
export const thunkCreateReview = (comment, rating,userId,bookId) => async (dispatch) => {
try{
    const response = await fetch(`/api/reviews/${userId}/${bookId}`, {
        method:'POST',
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({comment,rating})
    })
    if (response.ok)    {
        const review = await response.json()
        console.log('review thunk',review)
        dispatch(createReview(review))
        return review
    }
    }catch(error){
        const err = await error.json()
        return {error:err}
    }
//     else if (response.status < 500){
//     const err = await response.json()
//     return err
// }
}

export const thunkDeleteReview = (reviewId) => async (dispatch) => {
// try {
    const res = await fetch(`/api/reviews/delete/${reviewId}`, {
        method:'DELETE'
    })
    if (res.ok)    {
        const data = await res.json()

        dispatch(deleteReview(data))
        return data
    }else {
            const err = await res.json()
            return {errors:err}
        }
}

const initialState = {allReviews:{}, singleReview:{}}
export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_REVIEWS: {
            let newState = {...state, allReviews:{...state.allReviews}}
            newState.allReviews = {}
            action.data.forEach(ele => {
                newState.allReviews[ele.id]= ele
            });
            return newState
        }
        case GET_SINGLE_REVIEW:{
            let newState = {...state, singleReview:{...state.singleReview}}
            newState.singleReview = {}
            newState.singleReview=action.data
            return newState
        }
        case CREATE_REVIEW: {
            const newState = {...state}
            newState.allReviews[action.data.id] = action.data
            return newState
        }
        case DELETE_REVIEW: {
            const newState = {...state, allReviews:{...state.allReviews}}//try this to reshresh {...state,allGroups:{...state.allGroups}}
            delete newState.allReviews[action.eventId]
            return newState
        }
        // case EDIT_REVIEW: {
        //     const newState = {...state, singleReview:{...state.singleReview}}
        //     newState.singleReview = {}
        //     newState.singleReview = action.data
        //     return newState
        // }
        default:
            return state
    }
}
