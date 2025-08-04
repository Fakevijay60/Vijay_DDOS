const express = require('express');
const app = express();
const port = 8000;

app.get('/test', (req, res) => {
  console.log('Received request');
  res.send('Request received');
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});