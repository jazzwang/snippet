#!/bin/bash

# Exit on error
set -e

# Create project folder
mkdir pet-api-express && cd pet-api-express

# Initialize Node.js project
npm init -y

# Install Express
npm install express

# Create index.js with API logic
cat << 'EOF' > index.js
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.post('/pet', (req, res) => {
  const { id, name, status } = req.body;

  if (id === 0) {
    const newId = Math.floor(1000000000 + Math.random() * 9000000000);
    return res.status(200).json({ id: newId, name, status });
  } else {
    return res.sendStatus(405);
  }
});

app.listen(PORT, () => {
  console.log(\`Server is running on http://localhost:\${PORT}\`);
});
EOF

# Run the server
echo "Starting server..."
node index.js
