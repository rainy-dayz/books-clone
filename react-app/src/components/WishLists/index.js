
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'

import { useParams, useHistory } from 'react-router-dom'

import { thunkDeleteWishlist, thunkGetWishlists } from '../../store/wishlists'
import { thunkCreateCart} from '../../store/cart'
import './wishlist.css'


function WishList() {
    const dispatch = useDispatch()
    let wishAll = useSelector(state => Object.values(state.wishlists.allWishlists))
    let cartAll = useSelector(state => Object.values(state.carts.allCarts))
    let user = useSelector(state => (state.session.user))
    const history = useHistory()

    useEffect(() => {
        dispatch(thunkGetWishlists())
    }, [dispatch])

    const chicken=cartAll.map(order => {
        return order.book_id
    })

    if(!wishAll)return null
    return (
        <div className='holderoftheuniverse2'>
            <div className="holderoftheheadofcustomerreviews2">
            <div className="reviewheades3"><span>WishList</span></div>
            </div>
        {wishAll.length?(wishAll.map(wish =>{
            return <div className='bookincart2'key={wish.id}>
                    <div className='middlest'>
                    <img className='possmiddlepic2' onClick={() => {history.push(`/books/${wish.books.id}`)}} src={wish.books.book_image}/>
                    <div className="possinnermiddle2">
                <div className="bookTitleName">{wish.books.name}</div>
                <div className="authoorName">by {wish.books.author}</div>
                {wish.books.types == false? <div>Hardcover</div>: <div>Paperback</div>}
                <div className='singularprice2'>${wish.books.price}</div>

    <div className="editanddeletecontreview2">
    {chicken.find((chick) =>wish.book_id===chick)
                ?<div className="addedtocartmess"><img width="30" height="30" src="https://img.icons8.com/bubbles/100/checked.png" alt="checked"/>Added to Cart!</div>:
                <button className="addtocart2"onClick={() => {
                    dispatch(thunkCreateCart(user.id,wish.book_id))
                    dispatch(thunkDeleteWishlist(wish.id))

                }}>Add to Cart</button>}
                <button className='reviewwillenterthevoid' onClick={()=> {
                    dispatch(thunkDeleteWishlist(wish.id))
                    dispatch(thunkGetWishlists())
                    }}>Delete</button>

                </div>
                </div>
</div>
</div>
        })):<div className="emptymessage">No books added yet! </div>}
                </div>

        )
    }

    export default WishList
