// lib1.js
document.addEventListener("DOMContentLoaded", () => {
    const searchButton = document.querySelector(".search-bar button");
    const searchInput = document.querySelector(".search-bar input");
  
    // Handle Search functionality
    searchButton.addEventListener("click", () => {
      const searchTerm = searchInput.value.trim();
      if (searchTerm) {
        alert(`Searching for: ${searchTerm}`);
        // You can add functionality to search the book catalog here
      }
    });
  
    // Example: Toggle book availability on button click
    const availabilityButtons = document.querySelectorAll(".availability");
    
    availabilityButtons.forEach(button => {
      button.addEventListener("click", () => {
        button.classList.toggle("available");
        button.classList.toggle("unavailable");
        button.textContent = button.classList.contains("available") ? "Available" : "Checked Out";
      });
    });
  });
  