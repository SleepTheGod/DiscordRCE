import subprocess
import os
import json
import requests

def run_command(command):
    """ Helper function to run a shell command and handle errors """
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {result.stderr}")
        raise Exception(f"Command failed with return code {result.returncode}")
    return result.stdout

def setup_rpc_server():
    """ Setup the RPC server """
    # Create a directory for the RPC server
    if not os.path.exists('rpc-server'):
        os.makedirs('rpc-server')
    os.chdir('rpc-server')
    
    # Initialize npm and install dependencies
    run_command('npm init -y')
    run_command('npm install express body-parser')
    
    # Create server.js file with the provided content
    server_js_content = """
const express = require('express');
const bodyParser = require('body-parser');

// Initialize Express
const app = express();
const port = 6463;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Simple in-memory token store (for demonstration purposes)
const VALID_TOKEN = 'MTEzMjA0OTg4MDQxMjU5NDMyNg.ZuAKbA.arhOQxpLjiAXQGIah6HKbGv8rOw';

// Authentication middleware
const authenticate = (req, res, next) => {
  const token = req.headers['authorization'];
  if (token && token === VALID_TOKEN) {
    next();
  } else {
    res.status(401).json({ error: 'Unauthorized' });
  }
};

// Apply authentication middleware
app.use(authenticate);

// RPC endpoint
app.post('/rpc', (req, res) => {
  const { cmd, args, nonce } = req.body;

  // Basic command processing
  if (cmd === 'EXECUTE_CODE') {
    // For security reasons, avoid executing arbitrary code
    // In a real application, you would need to sanitize and validate input
    console.log(`Executing code: ${args.code}`);
    res.json({ status: 'Code executed' });
  } else {
    res.status(400).json({ error: 'Invalid command' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`RPC server listening at http://127.0.0.1:${port}`);
});
    """
    
    with open('server.js', 'w') as f:
        f.write(server_js_content)
    
    # Start the server
    print("Starting the RPC server...")
    subprocess.Popen('node server.js', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
def send_rpc_request():
    """ Send a POST request to the RPC server """
    url = "http://127.0.0.1:6463/rpc"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "MTEzMjA0OTg4MDQxMjU5NDMyNg.ZuAKbA.arhOQxpLjiAXQGIah6HKbGv8rOw"
    }
    data = {
        "cmd": "EXECUTE_CODE",
        "args": {
            "code": "echo 'Hello World' > /tmp/testfile"
        },
        "nonce": "9414fdad-c891-44d0-ba5b-848f93f7ec0b"
    }
    
    response = requests.post(url, headers=headers, json=data)
    print(f"RPC server response: {response.status_code} {response.text}")

if __name__ == "__main__":
    setup_rpc_server()
    
    # Wait for the server to start (give it some time)
    import time
    time.sleep(5)
    
    send_rpc_request()
