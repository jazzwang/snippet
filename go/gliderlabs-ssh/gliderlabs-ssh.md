# gliderlabs/ssh

- Git Rpo
  - https://github.com/gliderlabs/ssh
- Go Package
  - https://pkg.go.dev/github.com/gliderlabs/ssh

## 2025-11-13

- 緣起：
  - 想試試看能否在沒有管理者權限的 Winodws VM 上啟動 SSH Server。想要跑 SSH Tunnel，來做一些簡單的操作。
- 備註：
  - 後來想一想，如果 WSL 裡面可以裝 Ubuntu 的 openssh-server，好像也不用多此一舉。 
- 構想：
  - 來跟 Gemini 2.5 Flash 腦力激盪一下
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there ssh server implement in golang or python?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, there are SSH server implementations and libraries available in both **Go** and **Python**.

---

## 💻 Go (Golang) SSH Server Libraries

Go is very well-suited for network programming due to its strong standard library and excellent concurrency model, making it a natural choice for building performant network services like an SSH server.

* **Standard Library:** The core SSH implementation is provided by the `golang.org/x/crypto/ssh` package. This package is robust and provides the foundational components for both SSH clients and servers.
* **Higher-Level Wrappers:** Libraries like **`github.com/gliderlabs/ssh`** wrap the low-level `crypto/ssh` package to provide a simpler, higher-level API, often compared to Go's standard `net/http` package for ease of use in building custom SSH servers.

Many specialized tools and services written in Go (like `Teleport` or SSH bastions) embed a custom SSH server built using these libraries.

---

## 🐍 Python SSH Server Libraries

While Python is not as commonly used as Go or C for production-grade, standalone SSH servers like OpenSSH, it does have powerful libraries for creating custom SSH server functionality.

* **Paramiko:** The most well-known library is **`Paramiko`**. It is a pure-Python implementation of the SSHv2 protocol and provides both client and **server** functionality. You can subclass its components to create a custom server that handles connections, authentication, and commands.
* **PyserSSH:** This is a scriptable Python SSH server library that builds on top of Paramiko, offering a simpler and more flexible API for creating customized SSH terminal environments.

Python libraries are often used to build **honeypots**, specialized SSH frontends, or simple testing/scripting servers.

---

Would you like to know more about the **capabilities** or see a **simple code example** for implementing an SSH server in one of these languages?
</td></tr></table>
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
can I run a SSH server implemented by golang on Windows without System Admin permission?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, you **can** run an SSH server implemented in Go (Golang) on Windows without System Administrator permission, with one major caveat.

## Key Requirement: The Listening Port

The ability to run a network server without administrative privileges on any operating system, including Windows, comes down to the **port** it attempts to listen on.

* **Non-Admin Allowed Ports (The Goal):** You can run any Go SSH server (which is a single executable binary) as a regular user if it is configured to listen on a port number **greater than 1024** (e.g., 2222, 8022, 50000, etc.). Ports below 1024 are considered privileged ports and require administrator rights to bind to.
    * **Action:** Change the default SSH port from **22** to something like **2222** in your Go server's configuration.

* **Admin Required Port (The Caveat):** If you try to run the Go SSH server on the standard default port, **port 22**, it will fail immediately with a "permission denied" error because only processes running as an Administrator or the built-in Windows `System` account can bind to privileged ports on Windows.

---

## 🔒 Summary of Go SSH on Windows

1.  **Go Binary:** Go programs compile into single, standalone executables, so you don't need admin rights to install or run the program itself—just place the `.exe` in your user directory and execute it.
2.  **Permissions:** The only permission issue is binding to a port.
3.  **Solution:** Run your custom Go SSH server on a non-privileged port (e.g., $2222$) to operate it entirely without admin privileges.

**Example Go Server Configuration (Conceptual):**

Instead of using `ssh.Listen("0.0.0.0:22", config)`, you would use:
`ssh.Listen("0.0.0.0:2222", config)`
</td></tr></table>
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a golang example running SSH server on Windows 11?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, here is a working Go example for an SSH server.

This example uses the popular and high-level `github.com/gliderlabs/ssh` library, which simplifies server creation compared to the low-level standard package. As discussed, it's configured to run on a non-privileged port (**2222**) so you won't need System Admin permissions on your Windows 11 machine.

## 💾 Go SSH Server Example

### 1\. Setup

First, make sure you have Go installed, then initialize a module and get the required package:

```bash
# Create a project folder
mkdir go-ssh-server
cd go-ssh-server

# Initialize a Go module
go mod init go-ssh-server

# Install the high-level SSH library
go get github.com/gliderlabs/ssh
```

### 2\. The Code (`main.go`)

Create a file named `main.go` and paste the following code. This server will print a **"Hello from Windows 11\!"** banner when a client connects and then immediately disconnects.

```go
package main

import (
	"fmt"
	"log"
	"os"

	gossh "github.com/gliderlabs/ssh"
)

// The port to run the server on. Must be > 1024 to avoid needing Admin rights.
const ListenPort = 2222

func main() {
	// 1. Define a Handler function for new SSH connections
	// This simple handler will write a message and close the connection.
	handler := func(s gossh.Session) {
		// Log the connection attempt
		log.Printf("New connection from %s", s.RemoteAddr().String())

		// Write a greeting message to the connected client
		_, err := s.Write([]byte("Hello from Windows 11! Disconnecting now...\n"))
		if err != nil {
			log.Printf("Error writing to session: %v", err)
		}

		// Note: Since we are not running a shell, the session will close shortly after the handler finishes.
	}

	// 2. Configure the server
	server := gossh.Server{
		Addr:    fmt.Sprintf(":%d", ListenPort),
		Handler: handler,
		// Optionally, add a HostKey. If not provided, one will be generated for you.
		// For production, you would load this from a file: gossh.HostKeyFile("/path/to/key")
	}

	log.Printf("Starting SSH server on port %d...", ListenPort)

	// 3. Start the server
	if err := server.ListenAndServe(); err != nil && err != gossh.ErrServerClosed {
		log.Fatalf("SSH server failed to start: %v", err)
	}

	// This line is rarely reached, but included for completeness
	fmt.Println("Server stopped.")
	os.Exit(0)
}
```

### 3\. Build and Run

1.  **Build:** Compile the Go code into a Windows executable:
    ```bash
    go build .
    ```
2.  **Run:** Execute the compiled binary (`go-ssh-server.exe`):
    ```bash
    .\go-ssh-server.exe
    ```
    The console output will show: `2025/11/13 13:21:19 Starting SSH server on port 2222...`

### 4\. Test the Server

Open a new PowerShell window or a Linux/macOS terminal and use the SSH client to connect to your running server:

```bash
# Replace 'localhost' with your Windows machine's IP if connecting from another device
ssh user@localhost -p 2222
```

**Expected Client Output:**

```
Hello from Windows 11! Disconnecting now...
Connection to localhost closed.
```

**Expected Server Output (in the running `go-ssh-server.exe` window):**

```
2025/11/13 13:21:19 New connection from 127.0.0.1:xxxxx
```
</td></tr></table>