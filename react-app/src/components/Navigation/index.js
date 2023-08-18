import {useEffect,React} from 'react';
import { NavLink,useHistory } from 'react-router-dom';
import { useDispatch,useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import logo from '../../images/Logo.png'
import { thunkGetGenres } from '../../store/genres';
import SearchBar from '../SearchBar'
function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);
	let cartAll = useSelector(state => Object.values(state.carts.allCarts))
	let booksAll = useSelector(state => Object.values(state.book.allBooks))
	const history=useHistory()
	const dispatch = useDispatch()
	let totalQuantity = 0;
	return (
		<div>
			<div className="mainNavLineCont2">
			<img className='logo' src={logo} onClick={() => {history.push('/')}}/>
				<SearchBar/>
				<div className="cartInNav">
				{sessionUser &&<div onClick={() => {history.push(`/carts`)}}><i className="fa-sharp fa-solid fa-cart-shopping"></i></div>}
				{sessionUser &&cartAll && cartAll.length>0 &&<div className="cartbubble">{cartAll.forEach(item => {
									totalQuantity += item.quantity
								})}
								{totalQuantity}
								</div>}
				</div>
				<div>
					<ProfileButton user={sessionUser} />
				</div>
				</div>
				<div className="navLinksCont">
				<div className="navLinks2"onClick={() => {history.push('/genres/1')}}>Fantasy</div>
				<div className="navLinks2"onClick={() => {history.push('/genres/5')}}>Manga</div>
				<div className="navLinks2"onClick={() => {history.push('/genres/2')}}>SciFi</div>
				<div className="navLinks2"onClick={() => {history.push('/genres/3')}}>Romance</div>
				<div className="navLinks2"onClick={() => {history.push('/genres/4')}}>Thriller</div>
				</div>
				</div>
	);
}

export default Navigation;
