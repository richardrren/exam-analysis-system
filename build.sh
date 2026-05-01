#!/bin/bash

echo "========================================"
echo "Exam Analysis System - Build Script (Linux/UOS)"
echo "========================================"
echo ""

if [ ! -d "node/node-v20.10.0-linux-x64" ]; then
    echo "WARNING: Linux version of Node.js not found in node/node-v20.10.0-linux-x64"
    echo "Please download Node.js v20.10.0 for Linux x64 from:"
    echo "https://nodejs.org/dist/v20.10.0/node-v20.10.0-linux-x64.tar.xz"
    echo ""
    echo "Then extract it to node/node-v20.10.0-linux-x64"
    echo "And make sure to install mineru-open-api:"
    echo "cd node/node-v20.10.0-linux-x64 && npm install mineru-open-api"
    echo ""
    echo "Continuing anyway (but PDF parsing will fail without Node.js)..."
    echo ""
fi

python3 build.py
