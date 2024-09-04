document.addEventListener('DOMContentLoaded', function() {
    const roomName = document.querySelector('#room-name').textContent;
    const username = document.querySelector('#username').textContent;

    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        document.querySelector('#chat-messages').innerHTML += (
            '<div class="message">' +
            '<strong>' + data.username + '</strong>: ' +
            data.message +
            '<span class="timestamp">' + data.timestamp + '</span>' +
            '</div>'
        );
        document.querySelector('#chat-messages').scrollTop = document.querySelector('#chat-messages').scrollHeight;
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.querySelector('#chat-message-input').focus();
    document.querySelector('#chat-message-input').onkeyup = function(e) {
        if (e.keyCode === 13) {  // Enter key
            document.querySelector('#chat-message-submit').click();
        }
    };

    document.querySelector('#chat-message-submit').onclick = function(e) {
        const messageInputDom = document.querySelector('#chat-message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'username': username,
            'message': message
        }));
        messageInputDom.value = '';
    };
});

