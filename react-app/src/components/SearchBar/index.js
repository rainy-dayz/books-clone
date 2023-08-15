import { useEffect, useRef, useState } from 'react';
import { useDispatch,useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import'./searchBar.css'
import { thunkGetBooks, thunkGetSingleBook } from '../../store/book';
import { thunkGetReviews } from '../../store/reviews';


function SearchBar(){
const dispatch = useDispatch()
  const [filteredData, setFilteredData] = useState([]);
  const [wordInput, setWordInput] = useState('');
  let books = useSelector(state => Object.values(state.book.allBooks))
  const history = useHistory()
  const urlRef = useRef()

  useEffect(() => {
    dispatch(thunkGetBooks())
}, [])
const onlyBook=books.filter(value=>{return value.types="Hard"})
console.log('onlybook',onlyBook)
 const handleFilter = (event) =>{
    const searchEle=event.target.value
    setWordInput(searchEle)
    const newFilter = books.filter((value)=>{
        return value.name.toLowerCase().includes(searchEle.toLowerCase())
    })
    if(searchEle == ""){
        setFilteredData([])
    }else{
        setFilteredData(newFilter)
    }
 }
 useEffect(()=>{
     const clearInput = () => {
            setFilteredData([])
            setWordInput('')
    }
    window.addEventListener('click',clearInput)

    return ()=>window.removeEventListener('click',clearInput)
},[])

  return (
    <div className="search">
        <div className="searchInputs">
      <input
        type="text"
        className="textbox"
        placeholder="Search by Title"
        value={wordInput}
        onChange={handleFilter}

      />
      {filteredData.length===0 ? <i className="fa-solid fa-magnifying-glass" ></i>: <i className="fa-solid fa-x"></i>}
      </div>
      {filteredData.length !== 0 &&
      <div  className="dataResult">
        {filteredData.slice(0,15).map((value,key) =>{
            return (<div key={value.id}>
            <div className="dataItem" onClick={async()=> {
                 history.push(`/books/${value.id}`)
                  dispatch(thunkGetSingleBook(value.id))
                }}>{value.name}</div>
            </div>
            )
        })}
      </div>}
    </div>
  );
};

export default SearchBar;
