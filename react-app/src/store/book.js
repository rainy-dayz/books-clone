const GET_BOOKS = "books/GET_BOOKS"
const GET_SINGLE_BOOK = "books/GET_SINGLE_BOOK"

const getBook = (books) => ({
    type:GET_BOOKS,
    data:books
})

const getSingleBook = (book) => ({
    type:GET_SINGLE_BOOK,
    data:book
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
        case GET_SINGLE_BOOK:{
            let newState = {...state, singleBook:{...state.singleBook}}
            newState.singleBook = {}
            newState.singleBook=action.data
            return newState
        }
        default:
            return state
    }
}
