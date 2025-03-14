function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    if (userInput.trim() === "") return;

    let chatbox = document.getElementById("chatbox");

    // Display user message
    let userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = userInput;
    chatbox.appendChild(userMessage);

    // Scroll to latest message
    chatbox.scrollTop = chatbox.scrollHeight;

    // Send user input to FastAPI backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = document.createElement("div");
        botMessage.className = "bot-message";
        botMessage.textContent = data.response;
        chatbox.appendChild(botMessage);
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    // Clear input field
    document.getElementById("userInput").value = "";
}

// Allow pressing Enter to send messages
function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}
