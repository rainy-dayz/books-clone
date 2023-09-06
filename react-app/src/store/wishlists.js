const GET_WiISHLISTS = "wishlists/GET_WiISHLISTS"
const CREATE_WiISHLIST = 'wishlists/CREATE_WiISHLIST'
const DELETE_WiISHLIST = "wishlists/DELETE_WiISHLIST"
const ADD_TO_WISHLIST="wishlists/ADD_TO_WISHLIST"
const EDIT_WiISHLIST = 'wishlists/EDIT_WiISHLIST'
const GET_SINGLE_WiISHLIST= "wishlists/GET_SINGLE_WiISHLIST"

const getWishlists = (wishlists) => ({
    type:GET_WiISHLISTS,
    data:wishlists
})

const createWishlist = (data) => ({
    type:CREATE_WiISHLIST,
    data
})
const deleteWishlist = (wishlistId) => ({
    type:DELETE_WiISHLIST,
    data:wishlistId
})
const editWishlist = (wishlistId) => ({
    type:EDIT_WiISHLIST,
    data:wishlistId
})
const getSingleWishlist = (wishlist) => ({
    type:GET_SINGLE_WiISHLIST,
    data:wishlist

})
const createWishBook = (wishlistId) => ({
    type: ADD_TO_WISHLIST,
    data:wishlistId
})
export const thunkGetWishlists = () => async(dispatch) => {
    const res = await fetch(`/api/wishlists/wishlist`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getWishlists(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}
export const thunkCreateWishBook = (userId,bookId,wishlistId) => async (dispatch) => {
    try {
        const response = await fetch(`/api/wishlists/${userId}/${bookId}/${wishlistId}`, {
            method:'POST',
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({userId,bookId})
        })
        if (response.ok)    {
            const res= await response.json()
            dispatch(createWishBook(res))
            return res
        }
    } catch (error) {
        const err = await error.json()
        return {errors:err}
    }
}
export const thunkCreateWishlist = (userId,bookId) => async (dispatch) => {

    const response = await fetch(`/api/wishlists/${userId}/${bookId}`, {
        method:'POST',
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({userId,bookId})
    })
    if (response.ok)    {
        const data = await response.json()
        dispatch(createWishlist(data))
        return data
    }
    else if (response.status < 500){
    const err = await response.json()
    return err
}
}
export const thunkDeleteWishlist = (wishlistId) => async (dispatch) => {
    // try {
        const res = await fetch(`/api/wishlists/delete/${wishlistId}`, {
            method:'DELETE'
        })
        if (res.ok)    {
            const data = await res.json()

            dispatch(deleteWishlist(data))
            dispatch(thunkGetWishlists())
            return data
        }else {
                const err = await res.json()
                return {errors:err}
            }
}

export const thunkEditWishlist = (wishlistId,name) => async (dispatch) => {

    console.log('are we in the thiunk')
    const response = await fetch(`/api/wishlists/edit/${wishlistId}`, {
        method:'PUT',
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({name})
    })
    if (response.ok)    {
        const data = await response.json()
        dispatch(editWishlist(data))
        dispatch(thunkGetWishlists())
        return data
    }
    else if (response.status < 500){
    const err = await response.json()
    return err
}
}
export const thunkGetSingleWishlist = (wishlistId) => async(dispatch) => {
    const res = await fetch(`/api/wishlists/${wishlistId}`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getSingleWishlist(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}

const initialState = {allWishlists:{}, singleWishlist:{}}
export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_WiISHLISTS: {
            let newState = {...state, allWishlists:{...state.allWishlists}}
            newState.allWishlists = {}
            action.data.forEach(ele => {
                newState.allWishlists[ele.id]= ele
            });
            return newState
        }
        case CREATE_WiISHLIST: {
            const newState = {...state}
            newState.allWishlists[action.data.id] = action.data
            return newState
        }
        case DELETE_WiISHLIST:{
            const newState = {...state, allWishlists:{...state.allWishlists}}
            delete newState.allWishlists[action.wishlistId]
            return newState
        }

        case EDIT_WiISHLIST: {
            const newState = {...state, singleCart:{...state.singleCart},allWishlists:{...state.allWishlists}}
            newState.singleCart = action.data
            return newState
        }
        case GET_SINGLE_WiISHLIST:{
            let newState = {...state, singleCart:{...state.singleCart}}
            newState.singleCart=action.data
            return newState
        }
        case ADD_TO_WISHLIST: {
            let newState = {...state, allWishlists:{...state.allWishlists}}
            newState.allWishlists = {}
            action.data.books.forEach(ele => {
                newState.allWishlists[ele.id]= ele
            });
            return newState
        }
        default:
            return state
    }
}
