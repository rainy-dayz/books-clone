const GET_GENRES = "genres/GET_GENRES"
const GET_SINGLE_GENRE = "genres/GET_SINGLE_GENRE"
const CLEAR_SINGLE_GENRE="genres/CLEAR_SINGLE_GENRE"

const getGenres = (genres) => ({
    type:GET_GENRES,
    data:genres
})

const getSingleGenre = (genre) => ({
    type:GET_SINGLE_GENRE,
    data:genre
})
export const clearSingleGenre=()=>{
    return {
        type:CLEAR_SINGLE_GENRE
    }
}


export const thunkGetGenres = () => async(dispatch) => {
    const res = await fetch(`/api/genres`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getGenres(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}
export const thunkGetSingleGenre = (genreId) => async(dispatch) => {
    const res = await fetch(`/api/genres/${genreId}`)
    if (res.ok) {
        const data = await res.json()
        dispatch(getSingleGenre(data))
        return data
    }
    else {
        const err = await res.json()
        return {errors:err}
    }
}

const initialState = {allGenres:{}, singleGenre:{}}
export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_GENRES: {
            let newState = {...state, allGenres:{...state.allGenres}}
            // newState.allGenres = {}
            action.data.forEach(ele => {
                newState.allGenres[ele.id]= ele
            });
            return newState
        }
        case GET_SINGLE_GENRE:{
            let newState = {...state, singleGenre:{...state.singleGenre}}
            newState.singleGenre = {}
            newState.singleGenre=action.data
            return newState
        }
        case CLEAR_SINGLE_GENRE:{
            let newState={...state, singleGenre:null}
            return newState
        }
        default:
            return state
    }
}
