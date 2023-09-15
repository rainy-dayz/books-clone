# Pure Fiction

View my site live: https://books-clone-40tf.onrender.com/
Pure Fiction is a book selling website inspired by Barnes & Noble. In which a user can buy books, leave reviews for each book, and add books to their personal wishlists.

## ⚡ Technologies Used:
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black)
![React](https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black)
![Redux](https://img.shields.io/badge/Redux-764ABC.svg?style=for-the-badge&logo=Redux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white)

## Index
- [Link to my Wiki](https://github.com/rainy-dayz/books-clone/wiki)

- [Frontend and Backend Routes](https://github.com/rainy-dayz/books-clone/wiki/Routes)

- [React Components List](https://github.com/rainy-dayz/books-clone/wiki/React-Components-List)

- [Redux Store State Tree](https://github.com/rainy-dayz/books-clone/wiki/Redux-store-state)
  
- [User Stories](https://github.com/rainy-dayz/books-clone/wiki/User-Stories))


# Features 

## Orders:
- Users should be able to view all books in their cart.
- Users should be able to add books to their cart.
- Users should be able to update the quantity of books in their cart.
- Users should be able to delete books from their cart.

## WishList:
- Users should be able to view all books in their wishlist.
- Users should be able to add books to their wishlist.
- Users should be able to delete books from their wishlist.

## Reviews:
- Users should be able to view all public reviews for a book.
- Users should be able to create new reviews for the book they bought.
- Users should be able to update reviews they created.
- Users should be able to delete reviews they created.

## Liking Reviews:
- Users should be able to view all likes for reviews of a book.
- Users should be able to like a review.
- Users should be able to delete their like for a review.

# Photos
### Landing Page
![Screen Shot 2023-09-06 at 4 11 25 PM](https://github.com/rainy-dayz/books-clone/assets/124620939/5a61a29c-ba89-48c3-9a92-1aafd9190515)


### Single Genre Page
![Screen Shot 2023-09-06 at 4 12 04 PM](https://github.com/rainy-dayz/books-clone/assets/124620939/0257775c-bc26-45b4-8c7a-da8357c91d77)



### Single Book Page
![Screen Shot 2023-09-06 at 4 12 48 PM](https://github.com/rainy-dayz/books-clone/assets/124620939/640c2bd8-227c-4ea7-9f1a-ad3e629e50a4)


### Cart
![Screen Shot 2023-09-06 at 4 13 01 PM](https://github.com/rainy-dayz/books-clone/assets/124620939/deabc95d-463f-495d-a9f6-a4ef5dd995cc)


### Wishlist
![Screen Shot 2023-09-06 at 5 04 09 PM](https://github.com/rainy-dayz/books-clone/assets/124620939/092da07b-ba7f-4216-a7a7-7ec0d27e6896)



### Search Bar
![Screen Shot 2023-09-06 at 5 04 38 PM](https://github.com/rainy-dayz/books-clone/assets/124620939/a03fe757-535e-466d-8a85-99c595e05c3d)


## Installation Instructions

1. Install dependencies
```bash
pipenv install -r requirements.txt
```
2. Create a **.env** file based on the example with proper settings for your development environment

4. Replace the value for `SCHEMA` with a unique name, **making sure you use the snake_case convention**.

6. Get into your pipenv, migrate your database, seed your database, and run your Flask app

```bash
pipenv shell
```
```bash
flask db upgrade
```
```bash
flask seed all
```
```bash
flask run
```

7. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.

## To-dos/Future Features
- Allowing the user to view previous orders
- Allowing the user to make multiple wishlists
