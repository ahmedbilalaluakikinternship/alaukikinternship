alert("JavaScript is working!");
let form = document.getElementById("employeeForm");
let employeeList = document.getElementById("employeeList");

let editingRow = null;

form.addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let position = document.getElementById("position").value.trim();

    if (name === "" || email === "" || position === "") {
        alert("Please fill in all fields.");
        return;
    }

    if (editingRow === null) {
        let row = employeeList.insertRow();

        row.insertCell(0).textContent = name;
        row.insertCell(1).textContent = email;
        row.insertCell(2).textContent = position;

        let actionCell = row.insertCell(3);

        let editButton = document.createElement("button");
        editButton.textContent = "Edit";
        editButton.onclick = function() {
            editEmployee(this);
        };

        let deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.onclick = function() {
            deleteEmployee(this);
        };

        actionCell.append(editButton, deleteButton);
    } else {
        editingRow.cells[0].textContent = name;
        editingRow.cells[1].textContent = email;
        editingRow.cells[2].textContent = position;

        editingRow = null;
        form.querySelector("button[type='submit']").textContent = "Add Employee";
    }

    form.reset();
});

function editEmployee(button) {
    editingRow = button.parentElement.parentElement;

    document.getElementById("name").value = editingRow.cells[0].textContent;
    document.getElementById("email").value = editingRow.cells[1].textContent;
    document.getElementById("position").value = editingRow.cells[2].textContent;

    form.querySelector("button[type='submit']").textContent = "Update Employee";
}

function deleteEmployee(button) {
    let row = button.parentElement.parentElement;

    if (confirm("Are you sure you want to delete this employee?")) {
        if (editingRow === row) {
            editingRow = null;
            form.reset();
            form.querySelector("button[type='submit']").textContent = "Add Employee";
        }

        row.remove();
    }
}
