
let form = document.getElementById("registerForm");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let position = document.getElementById("position").value.trim();
    let message = document.getElementById("message");

    if (name === "" || email === "" || position === "") {
        message.textContent = "Please fill in all fields.";
        message.style.color = "red";
    } else {
        message.textContent = "Employee registered successfully!";
        message.style.color = "green";

        form.reset();
    }
});
