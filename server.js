const express = require('express');
const path = require('path');
const app = express();

app.use(express.static('.'));

// URL rewriting rules - map clean paths to actual files
app.get('/values', (req, res) => res.sendFile(path.join(__dirname, 'values.html')));
app.get('/values/pets', (req, res) => res.sendFile(path.join(__dirname, 'values_pets.html')));
app.get('/values/eggs', (req, res) => res.sendFile(path.join(__dirname, 'values_eggs.html')));
app.get('/values/petwear', (req, res) => res.sendFile(path.join(__dirname, 'values_petwear.html')));
app.get('/values/strollers', (req, res) => res.sendFile(path.join(__dirname, 'values_strollers.html')));
app.get('/values/food', (req, res) => res.sendFile(path.join(__dirname, 'values_food.html')));
app.get('/values/vehicles', (req, res) => res.sendFile(path.join(__dirname, 'values_vehicles.html')));
app.get('/values/toys', (req, res) => res.sendFile(path.join(__dirname, 'values_toys.html')));
app.get('/values/gifts', (req, res) => res.sendFile(path.join(__dirname, 'values_gifts.html')));
app.get('/values/stickers', (req, res) => res.sendFile(path.join(__dirname, 'values_stickers.html')));
app.get('/values/houses', (req, res) => res.sendFile(path.join(__dirname, 'values_houses.html')));

app.get('/trades', (req, res) => res.sendFile(path.join(__dirname, 'trades.html')));
app.get('/calculator', (req, res) => res.sendFile(path.join(__dirname, 'calculator.html')));
app.get('/blog', (req, res) => res.sendFile(path.join(__dirname, 'blog.html')));
app.get('/credits', (req, res) => res.sendFile(path.join(__dirname, 'credits.html')));
app.get('/value-updates', (req, res) => res.sendFile(path.join(__dirname, 'value-updates.html')));
app.get('/servers', (req, res) => res.sendFile(path.join(__dirname, 'servers.html')));

app.listen(6969, () => {
  console.log('Server running at http://localhost:6969');
});
