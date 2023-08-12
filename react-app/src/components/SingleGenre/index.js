import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { thunkGetSingleGenre, thunkGetSortedGenre,sortSingleGenre } from '../../store/genres';
import { thunkFilterPriceBooks, thunkGetBooks } from '../../store/book'




function SingleGenre() {
    const dispatch = useDispatch()
    let genre = useSelector(state => (state.genres.singleGenre.books))
    const [descending,setDescending]=useState(false)
    const[reversePrice, setReversePrice]=useState(false)
    const [highestRated,setHighestRated]=useState(false)
    const [lowestRated,setLowestRated]=useState(false)
    const history = useHistory()
    const { genreId } = useParams()
    // console.log('genre', genre)

    useEffect(async() => {
            dispatch(thunkGetSingleGenre(genreId))
        setDescending(false)
        setReversePrice(false)
        setHighestRated(false)
        setLowestRated(false)
    }, [genreId])

        if(descending){
        genre.sort((a,b) => a.price-b.price)
        }
        else if(reversePrice){
        genre.sort((a,b)=> b.price-a.price)
        }
        else if(highestRated){
        genre.sort((c,d)=>d.avgRating-c.avgRating)
        }
        else if(lowestRated){
        genre.sort((c,d)=>c.avgRating-d.avgRating)
        }
    if(!genre) return null
    return (
        <div>
            <button onClick={()=>{
             setDescending(true)
             setReversePrice(false)
            setHighestRated(false)
            }}>Price low to high</button>

            <button onClick={()=>{
             setReversePrice(true)
             setDescending(false)
             setHighestRated(false)
            }}>Price high to low</button>

            <button onClick={()=>{
                setHighestRated(true)
                setDescending(false)
                setReversePrice(false)
            }}>Rating Highest to Lowest</button>
            <button onClick={()=>{
                setLowestRated(true)
                setHighestRated(false)
                setDescending(false)
                setReversePrice(false)
            }}>Rating Lowest to Highest</button>
            {genre.map(book => {
                return <div key={book.id} >
                    <p>{book.name}</p>
                    <p>{book.price}</p>
                    <img onClick={() => {history.push(`/books/${book.id}`)}} className="booksImageHomepage" src={book.book_image} />
                    </div>

            })}
        </div>
        )
    }

    export default SingleGenre
