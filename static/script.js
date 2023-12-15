document.getElementById("send-button").addEventListener("click", function () {
    const userMessage = document.getElementById("user-message").value;

    fetch("/chatbot/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        const chatHistory = document.getElementById("chat-history");

        const userMessageElement = document.createElement("div");
        userMessageElement.className = "user-message";
        userMessageElement.innerHTML = `<span class="message-icon">You:</span> ${userMessage}`;
        chatHistory.appendChild(userMessageElement);

        if (data.bot_reply) {
            const botMessageElement = document.createElement("div");
            botMessageElement.className = "bot-message";
            botMessageElement.innerHTML = `<span class="message-icon">Bot:</span> ${data.bot_reply}`;
            chatHistory.appendChild(botMessageElement);
        } else {
            console.error("Invalid bot reply:", data);
        }

        document.getElementById("user-message").value = "";

        chatHistory.scrollTop = chatHistory.scrollHeight;

        const ratingFeedbackContainer = document.createElement("div");
        ratingFeedbackContainer.className = "rating-feedback-container";
        ratingFeedbackContainer.innerHTML = `
            <div class="rating-container">
                <span class="message-icon">Rate the response:</span>
                <select id="rating">
                    <option value="5">5 (Excellent)</option>
                    <option value="4">4 (Good)</option>
                    <option value="3">3 (Average)</option>
                    <option value="2">2 (Poor)</option>
                    <option value="1">1 (Terrible)</option>
                </select>
            </div>
            <div class="feedback-container">
                <span class="message-icon">Provide feedback:</span>
                <textarea id="feedback" rows="2"></textarea>
            </div>
            <button id="submit-rating-feedback">Submit</button>
        `;
        chatHistory.appendChild(ratingFeedbackContainer);

        document.getElementById("submit-rating-feedback").addEventListener("click", function () {
            const selectedRating = document.getElementById("rating").value;
            const userFeedback = document.getElementById("feedback").value;

            fetch("/submit-feedback/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ rating: selectedRating, feedback: userFeedback, feedback_id: chatHistory.children.length - 3 }),
            })
            .then(response => response.json())
            .then(data => {
                console.log("Feedback submitted:", data);

                ratingFeedbackContainer.remove();
                document.getElementById("feedback").value = "";
            });
        });
    });
});
