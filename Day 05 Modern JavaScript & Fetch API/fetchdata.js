
let loadBtn = document.getElementById("loadBtn");
let employeeList = document.getElementById("employeeList");
let message = document.getElementById("message");

loadBtn.addEventListener("click", async function() {
    message.textContent = "Loading employees...";
    employeeList.innerHTML = "";

    try {
        let response = await fetch(
            "https://jsonplaceholder.typicode.com/users"
        );

        if (!response.ok) {
            throw new Error("Failed to fetch employee data");
        }

        let employees = await response.json();

        employees.forEach(function(employee) {
            let row = document.createElement("tr");

            row.innerHTML = `
                <td>${employee.id}</td>
                <td>${employee.name}</td>
                <td>${employee.email}</td>
                <td>${employee.company.name}</td>
            `;

            employeeList.appendChild(row);
        });

        message.textContent = "Employees loaded successfully!";

    } catch (error) {
        message.textContent = "Error loading data. Please try again.";
        console.log(error);
    }
});
