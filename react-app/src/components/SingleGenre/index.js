import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import { thunkGetSingleGenre, thunkGetSortedGenre,sortSingleGenre, clearSingleGenre } from '../../store/genres';
import { thunkFilterPriceBooks, thunkFilteredBooks, thunkGetBooks } from '../../store/book'
import './singleGenre.css'
import StarRatingSingleReview from '../Reviews/starRatingSingleReview';
import QuickAdd from '../Quickadd';
import { thunkCreateCart, thunkEditCart } from '../../store/cart';
import Loading from '../Loading';




function SingleGenre() {
    const dispatch = useDispatch()
    let genre = useSelector(state => (state.genres.singleGenre?.books))
    let genreName = useSelector(state => (state.genres.singleGenre))
    const [descending,setDescending]=useState(false)
    const[reversePrice, setReversePrice]=useState(false)
    const [highestRated,setHighestRated]=useState(false)
    const [lowestRated,setLowestRated]=useState(false)
    const [openModal,setOpenModal] = useState(false)
    const user= useSelector(state => state.session.user)
    let cartAll = useSelector(state => Object.values(state.carts.allCarts))

    const history = useHistory()
    const { genreId } = useParams()
    console.log('genre', genre)

    let addthings

    useEffect(async() => {
        dispatch(clearSingleGenre())
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
let chicken
    return (
        <div className="allbooksofgenrecont">
            <h1 className="singlegenreheader">{genreName.name}</h1>
            <div className="sortingstuffout">
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
            }}>Rating High to Low</div>:<div style={{color: "blue"}} className="buttonFilterGenre"onClick={()=>{
                setHighestRated(true)

                setLowestRated(false)
            }}>Rating High to Low</div>}
            {lowestRated ==false?<div className="buttonFilterGenre"onClick={()=>{
                setLowestRated(true)
                setHighestRated(false)
            }}>Rating Low to High</div>:<div style={{color: "blue"}} className="buttonFilterGenre"onClick={()=>{
                setLowestRated(true)
                setHighestRated(false)
            }}>Rating Low to High</div>}
            </div>
            </div>
            {descending === true ?<div className="buttonFilterGenre1"onClick={()=>{
                setDescending(false)
                dispatch(thunkGetSingleGenre(genreId))
            }}>Price low to high X</div>:null}

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
            </div>

<div className="holdsthebooksforgenre">
            {genre.map(book => {
                return <div className="bookandreviewstarsgenre"key={book.id} >
                    <img onClick={() => {history.push(`/books/${book.id}`)}} className="booksImageNotHomepage" src={book.book_image} />
                    <div className="middleQuick">
    <script>
    {chicken=cartAll.map(order => {
        return order.book_id
    })}
    </script>
                    {user && (chicken.find((chick) => book.id===chick) ?<div className="textQuick" onClick={()=>{history.push(`/carts`)}}>Added to Cart!</div>:
                    <div className="textQuick" onClick={() => {
                    return dispatch(thunkCreateCart(user.id,book.id))

                }}>Quick Add</div>)}
                            </div>
                    <div >{<StarRatingSingleReview stars={book.avgRating} />}</div>
                    </div>

            })}
            </div>
        </div>
        )
    }

    export default SingleGenre
