const GET_LIKES = "wishlists/GET_LIKES"
const CREATE_LIKES = 'wishlists/CREATE_LIKES'
const DELETE_LIKES = "wishlists/DELETE_LIKES"


const getLikes = (likes) => ({
    type:GET_LIKES,
    data:likes
})

const createLikes = (data) => ({
    type:CREATE_LIKES,
    data
})
const deleteLikes = (likeId) => ({
    type:DELETE_LIKES,
    data:likeId
})

export const thunkGetLikes = (reviewId) => async(dispatch) => {
    const res = await fetch(`/api/likes/${reviewId}`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getLikes(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}
export const thunkCreateLikes = (reviewId) => async (dispatch) => {
    try {
        const response = await fetch(`/api/likes/${reviewId}/new`, {
            method:'POST',
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify()
        })
        if (response.ok)    {
            const res= await response.json()
            dispatch(createLikes(res))
            return res
        }
    } catch (error) {
        const err = await error.json()
        return {errors:err}
    }
}
export const thunkDeleteLikes = (likeId) => async (dispatch) => {
    // try {
        const res = await fetch(`/api/likes/delete/${likeId}`, {
            method:'DELETE'
        })
        if (res.ok)    {
            const data = await res.json()

            dispatch(deleteLikes(data))
            return data
        }else {
                const err = await res.json()
                return {errors:err}
            }
}

// export const thunkEditWishlist = (wishlistId,name) => async (dispatch) => {

//     console.log('are we in the thiunk')
//     const response = await fetch(`/api/wishlists/edit/${wishlistId}`, {
//         method:'PUT',
//         headers:{"Content-Type":"application/json"},
//         body:JSON.stringify({name})
//     })
//     if (response.ok)    {
//         const data = await response.json()
//         dispatch(editWishlist(data))
//         dispatch(thunkGetWishlists())
//         return data
//     }
//     else if (response.status < 500){
//     const err = await response.json()
//     return err
// }
// }
// export const thunkGetSingleWishlist = (wishlistId) => async(dispatch) => {
//     const res = await fetch(`/api/wishlists/${wishlistId}`)
//     if (res.ok) {
//         const data = await res.json()
//         dispatch(getSingleWishlist(data))
//         return data
//     }
//     else {
//         const err = await res.json()
//         return {errors:err}
//     }
// }

const initialState = {allLikes:{}}
export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_LIKES: {
            let newState = {...state, allLikes:{...state.allLikes}}
            newState.allLikes = {}
            action.data.forEach(ele => {
                newState.allLikes[ele.id]= ele
            });
            return newState
        }
        case CREATE_LIKES: {
            const newState = {...state}
            newState.allLikes[action.data.id] = action.data
            return newState
        }
        case DELETE_LIKES:{
            const newState = {...state, allLikes:{...state.allLikes}}
            delete newState.allLikes[action.likeId]
            return newState
        }

        // case EDIT_WiISHLIST: {
        //     const newState = {...state, singleCart:{...state.singleCart},allWishlists:{...state.allWishlists}}
        //     newState.singleCart = action.data
        //     return newState
        // }
        // case GET_SINGLE_WiISHLIST:{
        //     let newState = {...state, singleCart:{...state.singleCart}}
        //     newState.singleCart=action.data
        //     return newState
        // }
        // case ADD_TO_WISHLIST: {
        //     let newState = {...state, allWishlists:{...state.allWishlists}}
        //     newState.allWishlists = {}
        //     action.data.books.forEach(ele => {
        //         newState.allWishlists[ele.id]= ele
        //     });
        //     return newState
        // }
        default:
            return state
    }
}
