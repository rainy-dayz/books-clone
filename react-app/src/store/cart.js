const GET_CART = "carts/GET_CART"
const CREATE_CART = 'carts/CREATE_CART'
const DELETE_CART = "carts/DELETE_CART"
const EDIT_CART = 'carts/EDIT_CART'
const GET_SINGLE_CART = "carts/GET_SINGLE_CART"

const getCart = (carts) => ({
    type:GET_CART,
    data:carts
})

const createCart = (data) => ({
    type:CREATE_CART,
    data
})
const deleteCart = (cartId) => ({
    type:DELETE_CART,
    data:cartId
})
const editCart = (cartId) => ({
    type:EDIT_CART,
    data:cartId
})
const getSingleCart = (cart) => ({
    type:GET_SINGLE_CART,
    data:cart
})
export const thunkGetCart = (id) => async(dispatch) => {
    const res = await fetch(`/api/carts/user_cart`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getCart(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}

export const thunkCreateCart = (userId,bookId,quantity) => async (dispatch) => {

    const response = await fetch(`/api/carts/${userId}/${bookId}`, {
        method:'POST',
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({userId,bookId,quantity})
    })
    if (response.ok)    {
        const cart = await response.json()
        dispatch(createCart(cart))
        return cart
    }
    else if (response.status < 500){
    const err = await response.json()
    return err
}
}
export const thunkDeleteCart = (cartId) => async (dispatch) => {
    // try {
        const res = await fetch(`/api/carts/delete/${cartId}`, {
            method:'DELETE'
        })
        if (res.ok)    {
            const data = await res.json()

            dispatch(deleteCart(data))
            return data
        }else {
                const err = await res.json()
                return {errors:err}
            }
}

export const thunkEditCart = (cartId,quantity) => async (dispatch) => {

    const response = await fetch(`/api/carts/edit/${cartId}`, {
        method:'PUT',
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({quantity})
    })
    if (response.ok)    {
        const cart = await response.json()
        dispatch(editCart(cart))
        dispatch(thunkGetCart())
        return cart
    }
    else if (response.status < 500){
    const err = await response.json()
    return err
}
}
export const thunkGetSingleCart = (cartId) => async(dispatch) => {
    const res = await fetch(`/api/carts/${cartId}`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getSingleCart(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}

const initialState = {allCarts:{}, singleCart:{}}
export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_CART: {
            let newState = {...state, allCarts:{...state.allCarts}}
            newState.allCarts = {}
            action.data.forEach(ele => {
                newState.allCarts[ele.id]= ele
            });
            return newState
        }
        case CREATE_CART: {
            const newState = {...state}
            newState.allCarts[action.data.id] = action.data
            return newState
        }
        case DELETE_CART:{
            const newState = {...state, allCarts:{...state.allCarts}}
            delete newState.allCarts[action.cartId]
            return newState
        }

        case EDIT_CART: {
            const newState = {...state, singleCart:{...state.singleCart},allCarts:{...state.allCarts}}
            newState.singleCart = action.data
            return newState
        }
        case GET_SINGLE_CART:{
            let newState = {...state, singleCart:{...state.singleCart}}
            newState.singleCart=action.data
            return newState
        }
        default:
            return state
    }
}
