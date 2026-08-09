A content-based movie recommendation system that suggests films based on their structural similarities, like genre, cast, director, and plot keywords.

**[View the Live Demo Here](https://cinematic-matchmaker-a-recommendation.onrender.com/index.html)** 

---

## Overview

Ever finish a great movie and immediately want to watch something with the exact same vibe? This project solves that problem. 

Instead of relying on user behavior (like "other people who watched this also watched..."), this app uses a **Content-Based Recommendation** engine. It analyzes the actual "DNA" of over 5,000 movies from the TMDB dataset[cite: 1]. 

By converting text details into mathematical vectors using `scikit-learn`'s `CountVectorizer`, the system calculates the `cosine_similarity` between movies to find the closest possible match[cite: 1].

## Features

* **FastAPI Backend:** A lightweight, blazing-fast Python API that handles the recommendation math.
* **Modern Frontend:** A custom-built UI featuring a dark "glassmorphism" (frosted glass) aesthetic.
* **Live Posters:** Integrates seamlessly with the TMDB API to fetch high-quality movie posters on the fly.
* **Educational Section:** Includes a "How It Works" page that breaks down the machine learning concepts into plain English.

## Tech Stack

* **Backend:** Python, FastAPI, Uvicorn
* **Data & ML:** Pandas, Scikit-Learn, Pickle/BZ2
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Deployment:** Render
* **External APIs:** TMDB API

---

## How to Run Locally

Want to run this project on your own machine? Follow these simple steps:

### 1. Clone the repository
```bash
git clone [https://github.com/MuhammadSaud60/movie-recommendation-system.git](https://github.com/MuhammadSaud60/movie-recommendation-system.git)
cd movie-recommendation-system
