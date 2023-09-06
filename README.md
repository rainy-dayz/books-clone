# Pure Fiction

View our site live: https://books-clone-40tf.onrender.com/
Pure Fiction is a book selling website inspired by Barnes & Noble. This website is written in Flask and React/Redux.

## ⚡ Technologies We Used:
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black)
![React](https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black)
![Redux](https://img.shields.io/badge/Redux-764ABC.svg?style=for-the-badge&logo=Redux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white)

## Index
- [Features List](https://github.com/rainy-dayz/books-clone/wiki/Feature-List)

- [Frontend and Backend Routes](https://github.com/rainy-dayz/books-clone/wiki/Routes)

- [React Components List](https://github.com/rainy-dayz/books-clone/wiki/React-Components-List)

- [Redux Store State Tree](https://github.com/rainy-dayz/books-clone/wiki/Redux-store-state)




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
