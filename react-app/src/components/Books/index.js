import { thunkGetBooks } from '../../store/book'
import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { useHistory } from "react-router-dom"
import { useParams, useHistory } from 'react-router-dom'
import './books.css'
import fantasy from '../../images/fantasy.png'
import manga from '../../images/manga.png'
import romance from '../../images/romance.png'
import scifi from '../../images/scifi.png'
import thriller from '../../images/thriller.png'
import main from '../../images/main.gif'



function Books() {
    const dispatch = useDispatch()
    let booksAll = useSelector(state => Object.values(state.book.allBooks))
    let singleBook= useSelector(state=> state.book.singleBook)

    const history = useHistory()


    useEffect(() => {
        dispatch(thunkGetBooks())

    }, [dispatch])


    return (
        <>
        <img className="bannerforsales"src="https://dispatch.barnesandnoble.com/content/dam/ccr/global/global-nav-banner/2023/08/PROD-27234_Global_Nav_Banner_BookHaul2023_08-11.jpg"/>
         <div className="holderofimagecarousel">
            <img className="thegifcarousel" src={main}/>

         {/* <div className="slides">
            <input type="radio" name="radio-btn" id='radio1' />
            <input type="radio" name="radio-btn" id='radio2' />
            <input type="radio" name="radio-btn" id='radio3' />
            <input type="radio" name="radio-btn" id='radio4' />
            <input type="radio" name="radio-btn" id='radio5' />

            <div onClick={() => {history.push('/genres/1')}} className="slide first">
            <img
                src={fantasy}
                alt=""
            />
            </div>


            <div onClick={() => {history.push('/genres/5')}} className="slide">
            <img src={manga} alt="" />
            </div>


            <div onClick={() => {history.push('/genres/2')}} className="slide">
            <img src={scifi} alt="" />
            </div>


            <div onClick={() => {history.push('/genres/3')}} className="slide">
            <img src={romance} alt="" />
            </div>

            <div onClick={() => {history.push('/genres/4')}} className="slide">
            <img src={thriller} alt="" />
            </div>

            <div className="navigation-auto">
                <div className='auto-btn1'></div>
                <div className='auto-btn2'></div>
                <div className='auto-btn3'></div>
                <div className='auto-btn4'></div>
                <div className='auto-btn5'></div>
            </div>

            <div className="navigation-manual">
                <label for='radio1'className='manual-btn'></label>
               <label for='radio2'className='manual-btn'></label>
               <label for='radio3'className='manual-btn'></label>
               <label for='radio4'className='manual-btn'></label>
               <label for='radio5'className='manual-btn'></label>
            </div>
            </div> */}
            </div>
            <div className="shelfCont">
            <div className="fheadersforscrolls">Highest Rated:</div>
            <div  className="highestRated">
            {booksAll.map(book => {
                return( <>
                   {parseInt(book.avgRating)>=4.50 &&
                    <div className="cheese">
                   <img onClick={() => {
                    history.push(`/books/${book.id}`)}} className="booksImageHomepage" src={book.book_image} />
                   </div>}
                   </>)

})}
 </div>
</div>
<div className="shelfCont">
    <div className="fheadersforscrolls">Books Under $10:</div>
<div  className="highestRated">
            {booksAll.map(book => {
                return( <>
                   {parseInt(book.price)<=10.00 &&
                    <div className="cheese">
                   <img onClick={() => {
                    // clearInterval(chicken)
                    history.push(`/books/${book.id}`)}} className="booksImageHomepage" src={book.book_image} />
                   </div>}
                   </>)

})}
 </div>
 </div>
 <div className="shelfCont">
    <div className="fheadersforscrolls">New Releases:</div>
<div  className="highestRated">
            {booksAll.map(book => {
                return( <>

                   {book.releaseDate.slice(8,11)== 'Aug' && parseInt(book.releaseDate.slice(5,7)) <10&& parseInt(book.releaseDate.slice(12,17)) ==2023 &&
                    <div className="cheese">
                   <img onClick={() => {
                    // clearInterval(chicken)
                    history.push(`/books/${book.id}`)
                    }} className="booksImageHomepage" src={book.book_image} />
                   </div>}
                   </>)

})}
   </div>

                        <div className="myinfocont">
                            <div className="headersh5">Brought to you by:</div>
                                <div className='LandingDevName'>Emily Breininger  </div>
                                <a className="githibbutton" href='https://github.com/rainy-dayz'
                    ><i className="fa-brands fa-github"></i></a>
                    <a className="githibbutton2" href='https://www.linkedin.com/in/emily-breininger'
                    ><i className="fa-brands fa-linkedin"></i></a>



                    </div>
                    </div>
</>
        )
    }

    export default Books
