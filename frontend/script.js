document.addEventListener("DOMContentLoaded", () => {
    const searchBtn = document.getElementById("search-btn");
    const movieInput = document.getElementById("movie-input");
    const resultsContainer = document.getElementById("results-container");
    const statusMessage = document.getElementById("status-message");

    // Allow user to hit 'Enter' to search
    movieInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            searchBtn.click();
        }
    });

    searchBtn.addEventListener("click", async () => {
        const movieTitle = movieInput.value.trim();
        
        if (!movieTitle) {
            showStatus("Please enter a movie title.", "#ef4444");
            return;
        }

        // Clear previous results and show loading state
        resultsContainer.innerHTML = "";
        showStatus("Analyzing cinematic patterns...", "#94a3b8");

        try {
          
            const response = await fetch(`/recommend/${encodeURIComponent(movieTitle)}`);
            
            
            const data = await response.json();
            
            if (!response.ok) {
                
                throw new Error(data.detail || "Movie not found. Please check your spelling.");
            }

            
            
            statusMessage.classList.add("hidden");

            
            console.log(data);
            
            

            data.forEach(movie => {
                const card = document.createElement("div");
                card.classList.add("movie-card");
                
                const img = document.createElement("img");
                img.src = movie.poster; 
                img.alt = movie.title;
                img.classList.add("movie-poster");
                
               
                const title = document.createElement("div");
                title.classList.add("movie-title");
                title.innerText = movie.title; 
                
                // Add both to the card
                card.appendChild(img);
                card.appendChild(title);
                resultsContainer.appendChild(card);
            });

        } catch (error) {
            showStatus(error.message, "#ef4444");
        }
    });

    function showStatus(text, color) {
        statusMessage.innerText = text;
        statusMessage.style.color = color;
        statusMessage.classList.remove("hidden");
    }
});