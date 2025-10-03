#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Create and enter project directory
mkdir pet-api-springboot && cd pet-api-springboot

# Download Spring Boot Gradle project with Web dependency
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d type=maven-project \
  -d name=pet-api \
  -d packageName=com.example.petapi \
  -o pet-api.zip

# Unzip and enter project directory
unzip pet-api.zip

# Create model directory and Pet.java
mkdir -p src/main/java/com/example/petapi/model
cat <<EOF > src/main/java/com/example/petapi/model/Pet.java
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
EOF

# Create controller directory and PetController.java
mkdir -p src/main/java/com/example/petapi/controller
cat <<EOF > src/main/java/com/example/petapi/controller/PetController.java
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
            long randomId = 1_000_000_000L + new Random().nextInt(900_000_000);
            pet.setId(randomId);
            return ResponseEntity.ok(pet);
        } else {
            return ResponseEntity.status(HttpStatus.METHOD_NOT_ALLOWED).build();
        }
    }
}
EOF

# Run the application
./mvnw spring-boot:run &
sleep 20

# Test Case 1: Valid ID = 0
echo "Test Case 1: Valid ID = 0"
curl -v -X POST http://localhost:8080/pet \
-H "Content-Type: application/json" \
-d '{"id": 0, "name": "Fluffy", "status": "available"}'
echo -e "\n"

# Test Case 2: Invalid ID Γëá 0
echo "Test Case 2: Invalid ID Γëá 0"
curl -v -X POST http://localhost:8080/pet \
-H "Content-Type: application/json" \
-d '{"id": 123, "name": "Fluffy", "status": "available"}'
echo -e "\n"

# Test Case 3: Missing ID
echo "Test Case 3: Missing ID"
curl -v -X POST http://localhost:8080/pet \
-H "Content-Type: application/json" \
-d '{"name": "Fluffy", "status": "available"}'
echo -e "\n"
