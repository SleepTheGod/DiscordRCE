// Discord Remote Code Execution
// Use this endpoint
// http://127.0.0.1:6463/rpc?v=1&payload=%7B"cmd"%3A"BROWSER_HANDOFF"%2C"args"%3A%7B"handoffToken"%3A"MTEzMjA0OTg4MDQxMjU5NDMyNg.ZuAKbA.arhOQxpLjiAXQGIah6HKbGv8rOw"%2C"fingerprint"%3Anull%7D%2C"nonce"%3A"9414fdad-c891-44d0-ba5b-848f93f7ec0b"%7D&callback=https%3A%2F%2Fdiscord.com%2Fhandoff%3Fdone%3Dtrue
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
