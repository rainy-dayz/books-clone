import React from 'react';
import { NavLink,useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import logo from '../../images/Logo.png'

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);
	const history=useHistory()

	return (
		<ul>
			{/* <li>
				<NavLink exact to="/">Home</NavLink>
			</li> */}

			<img className='logo' src={logo} onClick={() => {history.push('/')}}/>
				<li>
					<ProfileButton user={sessionUser} />
				</li>

		</ul>
	);
}

export default Navigation;
