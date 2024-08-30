const button = document.getElementById('myButton');
const resultElement = document.getElementById('result');

// Event listener for both click and touch events
button.addEventListener('click', handleButtonClick);
button.addEventListener('touchstart', handleButtonClick);

async function handleButtonClick() {
    try {
        const response = await fetch('/get_data');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        resultElement.textContent = data.message;
    } catch (error) {
        console.error('Error:', error);
    }
}
