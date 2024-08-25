const questions = [
    "Question 1: What is the capital of France?",
    "Question 2: Explain the theory of relativity.",
    "Question 3: What is the boiling point of water?",
    "Question 4: Describe the process of photosynthesis.",
    "Question 5: What is the Pythagorean theorem?"
];

let currentQuestionIndex = 0;

function updateQuestion() {
    document.getElementById('question').textContent = questions[currentQuestionIndex];
    document.getElementById('pageIndex').textContent = `Question ${currentQuestionIndex + 1} of ${questions.length}`;
    document.getElementById('answer').value = ""; // Clear the textarea for a new answer
}

function nextQuestion() {
    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        updateQuestion();
    }
}

function previousQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        updateQuestion();
    }
}

function submitTest() {
    alert('Test Submitted! Thank you.');
    // Here, you could also implement logic to collect the answers and send them to a server
}

// Initialize the first question on page load
updateQuestion();
