# Implement Petstore swagger using Spring Boot

## 2025-09-01

- By Microsoft 365 Copilot

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me step-by-step command line instruction using Java SpringBoot to meet the following requirements?

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
Here’s a **step-by-step command line guide** to quickly build and test a minimal **Java Spring Boot** API in **GitHub Codespaces** that meets your requirements. This setup is optimized for a **20–30 minute time-box**.

---

## ✅ Step 1: Create a GitHub Repository

```bash
gh repo create pet-api-springboot --public --clone
cd pet-api-springboot
```

---

## ✅ Step 2: Open in GitHub Codespaces

From the GitHub repo page, click **Code > Codespaces > Create codespace on main**.

---

## ✅ Step 3: Initialize Spring Boot Project

Use Spring Initializr or CLI:

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d name=pet-api \
  -d packageName=com.example.petapi \
  -o pet-api.zip

unzip pet-api.zip
cd pet-api
```

---

## ✅ Step 4: Create Pet Model

Create `Pet.java` in `src/main/java/com/example/petapi/model/`:

```java
package com.example.petapi.model;

public class Pet {
    private Long id;
    private String name;
    private String status;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
```

---

## ✅ Step 5: Create Controller

Create `PetController.java` in `src/main/java/com/example/petapi/controller/`:

```java
package com.example.petapi.controller;

importapi.model.Pet;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Random;

@RestController
public class PetController {

    @PostMapping("/pet")
    public ResponseEntity<Pet> addPet(@RequestBody Pet pet) {
        if (pet.getId() != null && pet.getId() == 0) {
            long randomId = 1_000_000_000L + new Random().nextInt(900_000_000);
            pet.setId(randomId);
            ResponseEntity.ok(pet);
        } else {
            return ResponseEntity.status(HttpStatus.METHOD_NOT_ALLOWED).build();
        }
    }
}
```

---

## ✅ Step 6: Run the App

```bash
./mvnw spring-boot:run
```

App will be available at:

```
http://localhost:8080/pet
```

---

## ✅ Step 7: Test with `curl`

### ✅ Test Case 1: Valid ID = 0

```bash
curl -X POST http://localhost:8080/pet \
-H "Content-Type: application/json" \
-d '{"id": 0, "name": "Fluffy", "status": "available"}'
```

Expected: Returns `200` with a 10-digit random `id`.

---

### ❌ Test Case 2: Invalid ID ≠ 0

```bash
curl -X POST http://localhost:8080/pet \
-H "Content-Type: application/json" \
-d '{"id": 123, "name": "Fluffy", "status": "available"}'
```

Expected: Returns `405`.

---

### ❌ Test Case 3: Missing ID

```bash
curl -X POST http://localhost:8080/pet \
-H "Content-Type: application/json" \
-d '{"name": "Fluffy", "status": "available"}'
```

Expected: Returns `405`.

---

Would you like me to generate a `README.md`, a Postman collection, or a Swagger annotation for this controller?
</td></tr></table>
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you fix the step to use `gradlew` instead of `mvnw`?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Absolutely! Here's the **updated step-by-step guide using `gradlew` (Gradle Wrapper)** instead of `mvnw` for your **Java Spring Boot** API setup in GitHub Codespaces.

---

## ✅ Step 1: Create a GitHub Repository

```bash
gh repo create pet-api-springboot --public --clone
cd pet-api-springboot
```

---

## ✅ Step 2: Open in GitHub Codespaces

From the GitHub repo page, click **Code > Codespaces > Create codespace on main**.

---

## ✅ Step 3: Initialize Spring Boot Project with Gradle

Use Spring Initializr or CLI:

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d type=gradle-project \
  -d name=pet-api \
  -d packageName=com.example.petapi \
  -o pet-api.zip

unzip pet-api.zip
cd pet-api
```

---

## ✅ Step 4: Create Pet Model

Create `Pet.java` in `src/main/java/com/example/petapi/model/`:

```java
package com.example.petapi.model;

public class Pet {
    private Long id;
    private String name;
    private String status;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
```

---

## ✅ Step 5: Create Controller

Create `PetController.java` in `src/main/java/com/example/petapi/controller/`:

```java
package com.example.petapi.controller;

import com.example.petapi.model.Pet;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Random;

@RestController
public class PetController {

    @PostMapping("/pet")
    public ResponseEntity<Pet> addPet(@RequestBody Pet pet) {
        if (pet.getId() != null && pet.getId() == 0) {
           Entity.ok(pet);
        } else {
            return ResponseEntity.status(HttpStatus.METHOD_NOT_ALLOWED).build();
        }
    }
}
```

---

## ✅ Step 6: Run the App with Gradle

```bash
./gradlew bootRun
```

App will be available at:

```
http://localhost:8080/pet
```

---

## ✅ Step 7: Test with `curl`

### ✅ Test Case 1: Valid ID = 0

```bash
curl -X POST http://localhost:8080/pet \
-H "Content-Type: application/json" \
-d '{"id": 0, "name": "Fluffy", "status": "available"}'
```

Expected: Returns `200` with a 10-digit random `id`.

---

### ❌ Test Case 2: Invalid ID ≠ 0

```bash
curl -X POST http://localhost:8080/pet \
-H "Content-Type: application/json" \
-d '{"id": 123, "name": "Fluffy", "status": "available"}'
```

Expected: Returns `405`.

---

### ❌ Test Case 3: Missing ID

```bash
curl -X POST http://localhost:8080/pet \
-H "Content-Type: application/json" \
-d '{"name": "Fluffy", "status": "available"}'
```

Expected: Returns `405`.

---

Would you like me to generate a `README.md`, add Swagger annotations, or help you containerize this with Docker for deployment?
</td></tr></table>
