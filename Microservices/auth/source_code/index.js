const http = require('http');
const PORT = 3000;

http.createServer((req, res) => {
  res.writeHead(200);
  res.end('Hello from Node.js Auth Service');
}).listen(PORT, () => {
  console.log(`Auth service running on ${PORT}`);
});
