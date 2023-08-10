import {useEffect,React} from 'react';
import { NavLink,useHistory } from 'react-router-dom';
import { useDispatch,useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import logo from '../../images/Logo.png'
import { thunkGetGenres } from '../../store/genres';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);
	const history=useHistory()
	const dispatch = useDispatch()
	useEffect(() => {
		dispatch(thunkGetGenres())
    }, [])
	let genreAll = useSelector(state => Object.values(state.genres.allGenres))
	console.log('genreAll',genreAll)
	return (
		<div>
			<img className='logo' src={logo} onClick={() => {history.push('/')}}/>
				<div>
					<ProfileButton user={sessionUser} />
				</div>
				<div onClick={() => {history.push(`/carts`)}}><i class="fa-sharp fa-solid fa-cart-shopping"></i></div>
				{genreAll.map(gen =>{
					return <div key ={gen.id}>
					<p onClick={() => {history.push(`/genres/${gen.id}`)}}>{gen.name}</p>
					</div>
				})}
				</div>
	);
}

export default Navigation;
