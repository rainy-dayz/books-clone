import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";
import { useHistory } from "react-router-dom"
import SignupFormModal from "../SignupFormModal";
import OpenModalButton from "../OpenModalButton";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();
  const history = useHistory()

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login({email, password}));
    if (data) {
      setErrors(data);
    } else {
        closeModal()
    }
  };

  return (
    <div className="loginBtn">
      <h1>Log In</h1>
      <form className="thisistheform"onSubmit={handleSubmit}>
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
            size="50"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <label>
          Password
          <input
          className="input-field"
            type="password"
            size="50"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <button className="login-btn" type="submit">Log In</button>
        <button className="demo-user" onClick={() => {
          setEmail('demo@aa.io')
          setPassword('password')
        }} >Demo User</button>
      <OpenModalButton
              buttonText="Create an account"

              modalComponent={<SignupFormModal />}
            />
      </form>
    </div>
  );
}

export default LoginFormModal;
