// login.js
document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent default form submission
  
    const username = document.querySelector("#username").value;
    const password = document.querySelector("#password").value;
  
    // Here, you would typically make an AJAX request to check credentials against your database
    if (username === "admin" && password === "admin123") {
      // Redirect to homepage if login is successful
      window.location.href = "lib1.html";
    } else {
      alert("Invalid credentials");
    }
  });
  