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