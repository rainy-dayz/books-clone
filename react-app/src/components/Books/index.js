import { thunkGetBooks } from '../../store/book'
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import './books.css'




function Books() {
    const dispatch = useDispatch()
    let booksAll = useSelector(state => Object.values(state.book.allBooks))

    const history = useHistory()
    console.log(booksAll, '-----------------')

    useEffect(() => {
        dispatch(thunkGetBooks())
    }, [dispatch])



    return (
        <div>
            {booksAll.map(book => {
                return <div key={book.id} >
                    <p>{book.name}</p>
                    <img onClick={() => {history.push(`/books/${book.id}`)}} className="booksImageHomepage" src={book.book_image} />
                    </div>
            })}
        </div>
        )
    }

    export default Books
