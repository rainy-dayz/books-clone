import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { thunkGetSingleGenre } from '../../store/genres';
import { thunkGetBooks } from '../../store/book'



function SingleGenre() {
    const dispatch = useDispatch()
    let genre = useSelector(state => Object.values(state.genres.singleGenre))
    let booksAll = useSelector(state => Object.values(state.book.allBooks))
    const history = useHistory()
    const { genreId } = useParams()
    console.log('genre', genre[0])

    useEffect(() => {
        dispatch(thunkGetSingleGenre(genreId))
        dispatch(thunkGetBooks())
    }, [dispatch])

    if(!genre) return null
    return (
        <div>
            {booksAll.map(book => {
                return <div key={book.id} >
                    {book.genre_id == genreId &&  <p>{book.name}</p>}
                    {book.genre_id == genreId && <img onClick={() => {history.push(`/books/${book.id}`)}} className="booksImageHomepage" src={book.book_image} />}
                    {book.genre_id == genreId &&  <p>{book.description}</p>}
                    </div>

            })}
        </div>
        )
    }

    export default SingleGenre
