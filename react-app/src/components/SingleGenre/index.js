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
        if(reversePrice){
        genre.sort((a,b)=> b.price-a.price)
        }
        if(highestRated){
        genre.sort((c,d)=>d.avgRating-c.avgRating)
        }
        if(lowestRated){
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
            }}>Price low to high</div>:<div style={{color: "blue"}}className="buttonFilterGenre"onClick={()=>{
                setDescending(true)
                setReversePrice(false)
               }}>Price low to high</div>}

            {reversePrice ==false?<div className="buttonFilterGenre"onClick={()=>{
             setReversePrice(true)
             setDescending(false)
            }}>Price high to low</div>:<div style={{color: "blue"}}className="buttonFilterGenre"onClick={()=>{
                setReversePrice(true)
                setDescending(false)
               }}>Price high to low</div>}

            {highestRated ==false?<div className="buttonFilterGenre"onClick={()=>{
                setHighestRated(true)
                setLowestRated(false)
            }}>Rating Highest to Lowest</div>:<div style={{color: "blue"}} className="buttonFilterGenre"onClick={()=>{
                setHighestRated(true)

                setLowestRated(false)
            }}>Rating Highest to Lowest</div>}
            {lowestRated ==false?<div className="buttonFilterGenre"onClick={()=>{
                setLowestRated(true)
                setHighestRated(false)
            }}>Rating Lowest to Highest</div>:<div style={{color: "blue"}} className="buttonFilterGenre"onClick={()=>{
                setLowestRated(true)
                setHighestRated(false)
            }}>Rating Lowest to Highest</div>}
            </div>
            </div>
            {descending === true ?<div className="buttonFilterGenre1"onClick={()=>{
                setDescending(false)
                dispatch(thunkGetSingleGenre(genreId))
            }}>Price lowest to highest X</div>:null}

            {reversePrice === true ?<div className="buttonFilterGenre1"onClick={()=>{
                setReversePrice(false)
                dispatch(thunkGetSingleGenre(genreId))
            }}>Price high to low X</div>:null}

            {lowestRated === true ?<div className="buttonFilterGenre1"onClick={()=>{
               setLowestRated(false)
                dispatch(thunkGetSingleGenre(genreId))
            }}>Rating low to high X</div>:null}

            {highestRated === true ?<div className="buttonFilterGenre1"onClick={()=>{
                setHighestRated(false)
                dispatch(thunkGetSingleGenre(genreId))
            }}>Rating high to low X</div>:null}

            {genre.map(book => {
                return <div key={book.id} >
                    <p>{book.name}</p>
                    <p>{book.price}</p>
                    <p>{book.avgRating}</p>
                    <img onClick={() => {history.push(`/books/${book.id}`)}} className="booksImageHomepage" src={book.book_image} />
                    </div>

            })}
        </div>
        )
    }

    export default SingleGenre
