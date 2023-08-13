import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { thunkGetSingleGenre, thunkGetSortedGenre,sortSingleGenre } from '../../store/genres';
import { thunkFilterPriceBooks, thunkGetBooks } from '../../store/book'
import './singleGenre.css'



function SingleGenre() {
    const dispatch = useDispatch()
    let genre = useSelector(state => (state.genres.singleGenre.books))
    let genreName = useSelector(state => (state.genres.singleGenre))
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
            <h1 className="singlegenreheader">{genreName.name}</h1>
            <div className="buttonFilterGenreCont">
                <button className="dropBtnt">Sort By</button>
                <div className="dropdown-content">
            {descending ==false?<div className="buttonFilterGenre"onClick={()=>{
             setDescending(true)
            setReversePrice(false)
            setHighestRated(false)
            setLowestRated(false)
            }}>Price low to high</div>:<div style={{color: "blue"}}className="buttonFilterGenre"onClick={()=>{
                setDescending(true)
                setReversePrice(false)
                setHighestRated(false)
                setLowestRated(false)
               }}>Price low to high</div>}

            {reversePrice ==false?<div className="buttonFilterGenre"onClick={()=>{
             setReversePrice(true)
             setDescending(false)
             setHighestRated(false)
             setLowestRated(false)
            }}>Price high to low</div>:<div style={{color: "blue"}}className="buttonFilterGenre"onClick={()=>{
                setReversePrice(true)
                setDescending(false)
                setHighestRated(false)
                setLowestRated(false)
               }}>Price high to low</div>}

            {highestRated ==false?<div className="buttonFilterGenre"onClick={()=>{
                setHighestRated(true)
                setDescending(false)
                setReversePrice(false)
                setLowestRated(false)
            }}>Rating Highest to Lowest</div>:<div style={{color: "blue"}} className="buttonFilterGenre"onClick={()=>{
                setHighestRated(true)
                setDescending(false)
                setReversePrice(false)
                setLowestRated(false)
            }}>Rating Highest to Lowest</div>}
            {lowestRated ==false?<div className="buttonFilterGenre"onClick={()=>{
                setLowestRated(true)
                setHighestRated(false)
                setDescending(false)
                setReversePrice(false)
            }}>Rating Lowest to Highest</div>:<div style={{color: "blue"}} className="buttonFilterGenre"onClick={()=>{
                setLowestRated(true)
                setHighestRated(false)
                setDescending(false)
                setReversePrice(false)
            }}>Rating Lowest to Highest</div>}
            </div>
            </div>
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
