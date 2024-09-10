# Discord Remote Code Execution Proof of Concept

This repository provides a proof of concept for a remote code execution (RCE) vulnerability in Discord. The provided Python script automates the setup of a Node.js RPC server and sends a request to demonstrate the exploit.
Repository Structure

    main.py: A Python script to automate the setup and interaction with the RPC server.
    server.js (generated by the script): The Node.js server file that handles RPC requests.

Setup and Usage
Prerequisites

    Python: Ensure Python 3.x is installed. You can download it from python.org.
    Node.js and npm: Ensure Node.js and npm are installed. You can download them from nodejs.org.

Install Python Dependencies

Install the required Python library using pip:

pip install requests

Running the Script

    Clone the repository:

    git clone https://github.com/SleepTheGod/DiscordRCE.git cd DiscordRCE

    Run the Python script to set up and start the RPC server, and send a request to demonstrate the exploit:

    python main.py

Script Explanation

The Python script performs the following steps:

    Setup Node.js Environment:
        Creates a directory named rpc-server.
        Initializes a new Node.js project and installs necessary dependencies (express and body-parser).

    Generate server.js:
        Writes the Node.js server code to server.js. This code sets up an RPC server that listens for requests on port 6463 and executes commands if the correct authorization token is provided.

    Start the RPC Server:
        Starts the Node.js server in the background.

    Send RPC Request:
        Sends a POST request to the RPC server to execute a specific command. This command demonstrates the RCE vulnerability by writing a message to a file.

Important Notes

    Security: This script and server setup is for educational and proof-of-concept purposes only. Do not use this for malicious activities. Ensure you have permission to test and use this in your environment.
    Token: The authorization token used in the script is hardcoded for demonstration purposes. In a real application, tokens should be handled securely.
