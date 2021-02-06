> # Axios
---
* ## Address to perform test requests for the api
* **https://jsonplaceholder.typicode.com/users**

* ## Axios documentation
    **https://www.npmjs.com/package/axios#response-schema**

* ## Install Axios
    * npm install --save axios

* ## how it works
First, we require the `Axios library`, then we call the `JSONPlaceholder` users `API` with `axios.get` (which is promise-based).

We use the then method to `get` the result when the promise is resolved and get the response object as a res variable. In the then method, we log the status code and date from the response header.

We get the `JSON` data as an array easily with `res.data` thanks to `Axios`’ auto transformations. Consequently, we loop through the users, logging the `ID` and the `name`. In case of any error, we log the error message on the console.

---

## License
*`Axios` is open source and therefore free to download and use without permission.*

<a href="url"><img src="https://www.holbertonschool.com/holberton-logo.png" align="middle" width="100" height="30"></a>

---