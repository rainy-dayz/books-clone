import { thunkGetReviews } from "./reviews"

const GET_BOOKS = "books/GET_BOOKS"
const GET_SINGLE_BOOK = "books/GET_SINGLE_BOOK"
const UPDATE_BOOK="books/UPDATE_BOOK"
const FILTERED_BOOKS='books/FILTERED_BOOKS'
const getBook = (books) => ({
    type:GET_BOOKS,
    data:books
})

const getSingleBook = (book) => ({
    type:GET_SINGLE_BOOK,
    data:book
})
const updateSingleBook = (book) => ({
    type:UPDATE_BOOK,
    data:book
})
const fileterdBooks = (data) => ({
    type:FILTERED_BOOKS,
    data
})
export const thunkGetBooks = () => async(dispatch) => {
    const res = await fetch(`/api/books`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getBook(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}

export const thunkFilteredBooks = (subgenre) => async(dispatch) => {
    const res = await fetch(`/api/books/filter`,{
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "SubGenre":`${subgenre}`,
		},
    });
    if (res.ok) {
        const data = await res.json()
        dispatch(fileterdBooks(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}
export const thunkGetSingleBook = (bookId) => async(dispatch) => {
    const res = await fetch(`/api/books/${bookId}`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getSingleBook(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}


export const thunkUpdateBook = (types,bookId) => async (dispatch) => {

    const response = await fetch(`/api/books/update/${bookId}`, {
        method:'PUT',
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({types})
    })
    if (response.ok)    {
        const book = await response.json()
        dispatch(updateSingleBook(book))
        // dispatch(thunkGetSingleBook(bookId))
        return book
    }
    else if (response.status < 500){
    const err = await response.json()
    return err
}
}

const initialState = {allBooks:{}, singleBook:{}}
export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_BOOKS: {
            let newState = {...state, allBooks:{...state.allBooks}}
            newState.allBooks = {}
            action.data.forEach(ele => {
                newState.allBooks[ele.id]= ele
            });
            return newState
        }
        case FILTERED_BOOKS: {
            let newState = {...state, allBooks:{...state.allBooks}}
            newState.allBooks = {}
            action.data.forEach(ele => {
                newState.allBooks[ele.id]= ele
            });
            return newState
        }
        case GET_SINGLE_BOOK:{
            let newState = {...state, singleBook:{...state.singleBook}}
            newState.singleBook = {}
            newState.singleBook=action.data
            return newState
        }
        case UPDATE_BOOK: {
            const newState = {...state, singleBook:{...state.singleBook}}
            newState.singleBook = {}
            newState.singleBook = action.data
            return newState
        }
        default:
            return state
    }
}
