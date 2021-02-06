> # HTTPS module
---
* ## address to perform test requests for the api
* **https://jsonplaceholder.typicode.com/users**

* ## HTTPS documentation
    * https://nodejs.org/api/https.html
* ## how it works

Let’s walk through the code. First, we require the `https` standard Node module, which is available with `Node.js` installation. No need for a `package.json` file or any `npm install --save` to `get` this running.

We then call our `JSONPlaceholder` URL with the `get method`, which has a callback that provides the response we have put in the res variable.

Next, we initialize data as an empty array, and after that, we log the status code and date from the respone’s header. Subsequently, whenever we get data, we push the chunk to the data array.

Then, on the response end, we concat the array data, change it into a string, and parse the `JSON` to get the list of 10 users as an array of objects. Consequently, we loop through the 10 users and log the `ID` and `name of the user` object one at a time.

One thing to note here: if there is an error on the `request`, the error message is logged on the console. The above code is available as a `pull request` for your reference.

As `HTTPS` is a standard `Node.js` module, there’s been no need for a `package.json`
---

## License
*`HTTPS module` is open source and therefore free to download and use without permission.*

<a href="url"><img src="https://www.holbertonschool.com/holberton-logo.png" align="middle" width="100" height="30"></a>

---