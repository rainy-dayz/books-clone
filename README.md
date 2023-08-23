# Pure Fiction

View our site live: https://books-clone-40tf.onrender.com/
Pure Fiction is a book selling website inspired by Barnes & Noble. This website is written in Flask and React/Redux.


## Index
- Features List: https://github.com/rainy-dayz/books-clone/wiki/Feature-List

- Database Schema: https://github.com/rainy-dayz/books-clone/wiki/Schema

- Frontend and Backend Routes:https://github.com/rainy-dayz/books-clone/wiki/Routes

- React Components List: https://github.com/rainy-dayz/books-clone/wiki/React-Components-List

- Redux Store State Tree: https://github.com/rainy-dayz/books-clone/wiki/Redux-store-state



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
- Allowing the user to like a review
- Allowing the user to make a wishlist
