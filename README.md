# Custom-API

This project consists of a simple Flask-based API server and a client script to interact with it. The API server accepts a hall ticket number, makes a request to an University Results server, and returns the name and SGPA of the student.

## History
I created this custom API to showcase how an API functions, for my university assignment.

## Prerequisites

- Python 3.x
- Flask
- Requests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Custom-API.git
    cd Custom-API
    ```

2. Install the required packages:
    ```sh
    pip install flask requests
    ```

## Usage

### Running the Server

1. Navigate to the project directory:
    ```sh
    cd /project-directory/
    ```

2. Start the Flask server:
    ```sh
    python server.py
    ```

   The server will start running on `http://127.0.0.1:5000` by default.

### Running the Client

1. Open a new terminal and navigate to the project directory:
    ```sh
    cd /project-directory/
    ```

2. Run the client script with the hall ticket number as an argument:
    ```sh
    python client.py <hall_ticket_number>
    ```

   Replace `<hall_ticket_number>` with the actual hall ticket number (1-60).

## Example

```sh
python client.py 25
```

Output:

| Name     | SGPA  |
|----------|-------|
| John Doe | 8.75  |
