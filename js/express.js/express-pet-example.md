# implement petstore swagger using express.js

## 2025-09-01

- By Microsoft 365 Copilot

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you create a bash script in order to meet the following requirements using express.js?

- Given a Swagger document
  - https://petstore.swagger.io/#/pet/addPet
- Limitations:
  - this will be time-boxed (usually **20 minutes**, at most 30 minutes)
    - think about your strategy before coding
- keep in mind:
  - you don't need to deal with the database (e.g. store request JSON data to the database.)
  - to keep it simple, you can simplify the request JSON to include "id", "name", and "status" only (ignore the nested fields).
  - try to write part of the code and validate it:
    - can listen on `http://localhost:PORT`
    - can handle POST request to `/pet`
    - can return `200` if the request `id` is zero
    - can generate a 10-digit random number as response `id`
    - can return `405` if the request `id` is not zero or does not exist
- Describe the expected business logic:
  - if the request ID is 0,
    replace the ID with a 10-digit random number,
    and return HTTP Status Code `200` and the updated JSON object as a response.
  - if the request ID is not zero or does not exist, then return HTTP Status Code `405`.
- Test Cases:
  - there will be 3 test cases based on expected business logic
  - you can use `curl` or `postman` to validate your API endpoint
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Here's a **Bash script** that sets up a minimal Express.js server to meet your requirements. It includes logic to handle a POST request to `/pet`, validate the `id` field, and respond accordingly.

---

### 🛠️ **Step-by-Step Strategy**
1. **Initialize a Node.js project**.
2. **Install Express.js**.
3. **Create a simple server** that:
   - Listens on a port.
   - Handles POST requests to `/pet`.
   - Checks the `id` field in the request body.
   - Responds with:
     - `200` and a random 10-digit `id` if `id === 0`.
     - `405` if `id` is missing or not zero.

---

### 📜 **Bash Script: `setup_pet_api.sh`**

```bash
#!/bin/bash

# Exit on error
set -e

# Create project folder
mkdir pet-api && cd pet-api

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
```

---

### ✅ **Test Cases (using curl)**

```bash
# Test Case 1: Valid request with id = 0
curl -X POST http://localhost:3000/pet \
  -H "Content-Type: application/json" \
  -d '{"id":0,"name":"Fluffy","status":"available"}'

# Test Case 2: Invalid request with id = 123
curl -X POST http://localhost:3000/pet \
  -H "Content-Type: application/json" \
  -d '{"id":123,"name":"Fluffy","status":"available"}'

# Test Case 3: Missing id field
curl -X POST http://localhost:3000/pet \
  -H "Content-Type: application/json" \
  -d '{"name":"Fluffy","status":"available"}'
```

---

Would you like me to package this into a downloadable `.zip` file or help you run it in a Docker container for easier testing?
</td></tr></table>
