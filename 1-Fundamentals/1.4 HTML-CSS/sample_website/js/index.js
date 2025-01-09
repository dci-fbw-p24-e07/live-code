const email = document.getElementById("email");

email.addEventListener("input", (event) => {
    if (email.validity.typeMismatch) {
        // perform if true
        email.setCustomValidity("I am expecting an email address!");
    } else {
        // perform if false
        email.setCustomValidity("");
    }
});

// Get hold of button element
const button = document.querySelector("button");

// Listen for a click on the button
button.addEventListener("click", updateName);

// Define updateName function
function updateName() {
    // Ask user for input
    const name = prompt("Enter a new name:");
    // change the content of the button element
    button.textContent = name;
}