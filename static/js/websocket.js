const socket = new WebSocket('ws://127.0.0.1:8001/ws/strem/');

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    console.log(data.message);
};

socket.onopen = function() {
    socket.send(JSON.stringify({ message: 'Hello from client!' }));
};