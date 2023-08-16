import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [firstName, setFirstName] = useState('');
	const [lastName, setLastName] = useState('');
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (password === confirmPassword) {
			const data = await dispatch(signUp(username, email, password,firstName,lastName));
			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			setErrors([
				"Confirm Password field must match the Password field",
			]);
		}
	};

	return (
		<div className='signUpForm'>
			<h1>Sign Up</h1>
			<form className="formforsignup" onSubmit={handleSubmit}>
				<ul>
					{errors.map((error, idx) => (
						<div key={idx} style={{color:'red'}}>{error}</div>
					))}
				</ul>
				<label>
					Email
					<input
					className="input-field"
						type="text"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						required
					/>
				</label>
				<label>
					Username
					<input
					className="input-field"
						type="text"
						value={username}
						onChange={(e) => setUsername(e.target.value)}
						required
					/>
				</label>
				<label >
					First Name:
					<input
					className="input-field"
						type="text"
						value={firstName}
						onChange={(e) => setFirstName(e.target.value)}
						required
					/>
				</label>
				<label >
					Last Name:
					<input
					className="input-field"
						type="text"
						value={lastName}
						onChange={(e) => setLastName(e.target.value)}
						required
					/>
				</label >
				<label>
					Password
					<input
					className="input-field"
						type="password"
						value={password}
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
				</label>
				<label>
					Confirm Password
					<input
					className="input-field"
						type="password"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
				</label>
				<button className="signUpBtn" type="submit">Sign Up</button>
				<OpenModalButton
              buttonText="Sign In"
              modalComponent={<LoginFormModal />}
            />
			</form>
		</div>
	);
}

export default SignupFormModal;
