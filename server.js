const express = require("express");

var app = express();

app.get("/", function(req, res) {
	res.sendFile(__dirname + "\\main.html");
});

app.get("/top", function(req, res) {
	res.sendFile(__dirname + "\\top.png");
});

app.get("/front", function(req, res) {
	res.sendFile(__dirname + "\\front.png");
});

app.get("/left", function(req, res) {
	res.sendFile(__dirname + "\\left.png");
});

app.get("/right", function(req, res) {
	res.sendFile(__dirname + "\\right.png");
});

app.get("/bottom", function(req, res) {
	res.sendFile(__dirname + "\\bottom.png");
});

app.get("/back", function(req, res) {
	res.sendFile(__dirname + "\\back.png");
});


app.listen(4000, function() {
	console.log("Ready");
});