# Python RMI Lab

## Translating Java RMI Architecture to Python Distributed Objects

This project translates a Java Remote Method Invocation (RMI)
application into a Python distributed object system using Pyro5.

## Requirements
- Python 3
- Pyro5

## Installation

Install Pyro5:

    py -m pip install Pyro5

## Project Structure

- `product.py` - Defines the Product class and its methods.
- `server.py` - Creates and registers remote product objects.
- `client.py` - Connects to the server and retrieves laptop details.

## How to Run

Open three terminals in the project directory.

### Terminal 1: Start the name server

    py -m Pyro5.nameserver

### Terminal 2: Start the product server

    py server.py

### Terminal 3: Run the client

    py client.py

## Expected Output

    Client is starting...

    --- PRODUCT DETAILS ---
    Name: Laptop
    Description: Lenovo laptop
    Price: 800000.0

## How It Works

The Pyro5 name server allows the client to locate a remote
product object. The server registers the product objects,
and the client uses a Pyro5 proxy to invoke their methods.

## Features

- Remote method invocation
- Product information retrieval
- Client-server communication using Pyro5

## Author

Junalea Mhae F. Gallogo
