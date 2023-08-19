
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'

import { useParams, useHistory } from 'react-router-dom'

import { thunkDeleteWishlist, thunkGetWishlists } from '../../store/wishlists'



function WishList() {
    const dispatch = useDispatch()
    let wishAll = useSelector(state => Object.values(state.wishlists.allWishlists))
    let booksAll = useSelector(state => Object.values(state.book.allBooks))
    let cart=useSelector(state => (state.carts.singleCart))
    const [openModal,setOpenModal] = useState(false)
    const history = useHistory()
    console.log('wiskes',wishAll)

    useEffect(() => {
        dispatch(thunkGetWishlists())
    }, [dispatch])

    if(!wishAll)return null
    return (
        <>
        <h1 >WishList</h1>
        {wishAll.map(wish =>{
            return <div key={wish.id}>
                <div>{wish.books.name}</div>
                <button onClick={()=> {
                    dispatch(thunkDeleteWishlist(wish.id))
                    dispatch(thunkGetWishlists())
                    }}>Delete</button>
            </div>
        })}
                </>
        )
    }

    export default WishList
