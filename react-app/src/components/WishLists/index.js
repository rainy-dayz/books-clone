
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'

import { useParams, useHistory } from 'react-router-dom'

import { thunkDeleteWishlist, thunkGetWishlists } from '../../store/wishlists'
import { thunkCreateCart, thunkEditCart } from '../../store/cart'
import './wishlist.css'


function WishList() {
    const dispatch = useDispatch()
    let wishAll = useSelector(state => Object.values(state.wishlists.allWishlists))
    let booksAll = useSelector(state => Object.values(state.book.allBooks))
    let cartAll = useSelector(state => Object.values(state.carts.allCarts))
    let cart=useSelector(state => (state.carts.singleCart))
    let user = useSelector(state => (state.session.user))
    const [openModal,setOpenModal] = useState(false)
    const history = useHistory()
    console.log('wiskes',wishAll)

    useEffect(() => {
        dispatch(thunkGetWishlists())
    }, [dispatch])

    let addthings
    const chicken=cartAll.map(order => {
        return order.book_id
    })

    if(!wishAll)return null
    return (
        <div className='holderoftheuniverse2'>
            <div className="holderoftheheadofcustomerreviews2">
            <div className="reviewheades3"><span>WishList</span></div>
            </div>
        {wishAll.map(wish =>{
            return <div className='bookincart2'key={wish.id}>
                    <div className='middlest'>
                    <img className='possmiddlepic2' onClick={() => {history.push(`/books/${wish.books.id}`)}} src={wish.books.book_image}/>
                    <div className="possinnermiddle2">
                <div className="bookTitleName">{wish.books.name}</div>
                <div className="authoorName">by {wish.books.author}</div>
                {wish.books.types == false? <div>Hardcover</div>: <div>Paperback</div>}
                <div className='singularprice2'>${wish.books.price}</div>

    <script>{
        addthings=async()=>{
            if(cartAll){
                cartAll.map(cart=>{
                    if(cart.book_id==wish.book_id){
                        dispatch(thunkEditCart(cart.id, cart.quantity+1))
                        dispatch(thunkDeleteWishlist(wish.id))
                        history.push(`/carts`)
                    }
                })
            }
        }
    }</script>
    <div className="buttonContwishes">
    {chicken.find((chick) =>wish.book_id===chick)
                ?<button  onClick={addthings}>Add to Cart Again!</button>:
                <button onClick={() => {
                    dispatch(thunkCreateCart(user.id,wish.book_id))
                    dispatch(thunkDeleteWishlist(wish.id))
                    dispatch(thunkGetWishlists())
                }}>Add to Cart</button>}
                <button onClick={()=> {
                    dispatch(thunkDeleteWishlist(wish.id))
                    dispatch(thunkGetWishlists())
                    }}>Delete</button>

                </div>
                </div>
</div>
</div>
        })}
                </div>

        )
    }

    export default WishList
