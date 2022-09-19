const express = require("express");

let app = express();

app.get("/", function (request, response) {
    response.send("Hi Human!")
})

app.listen(3000, () => {
    console.log("Server running !!");
})