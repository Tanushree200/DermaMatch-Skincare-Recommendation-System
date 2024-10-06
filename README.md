# Dermamatch - Skincare Recommendation System

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## Introduction

Welcome to **Dermamatch**, your personalized skincare recommendation system! Dermamatch leverages a comprehensive database of skincare ingredients and user-specific skin profiles to provide tailored skincare routines. Whether you're dealing with acne, dryness, sensitivity, or any other skin concerns, Dermamatch helps you discover the best ingredients and products to achieve your skin goals.

## Features

- **Personalized Recommendations:** Get skincare ingredient suggestions based on your skin type and specific skin concerns.
- **Comprehensive Ingredient Database:** Access detailed information about various skincare ingredients, including application instructions, effectiveness ratings, compatibility with other ingredients, and more.
- **Ingredient Compatibility:** Avoid potential ingredient conflicts by specifying ingredients you wish to exclude.
- **Skincare Routine Generator:** Automatically generate a complete skincare routine tailored to your needs.
- **User-Friendly Interface:** Intuitive web interface built with Flask for easy interaction and seamless experience.

## How It Works

1. **Select Your Skin Type:** Choose from options like normal, dry, oily, combination, or sensitive.
2. **Identify Your Skin Concerns:** Select one or more skin problems you want to address, such as acne, hyperpigmentation, fine lines, etc.
3. **Exclude Ingredients (Optional):** Specify any ingredients you wish to avoid due to allergies, sensitivities, or personal preferences.
4. **Get Recommendations:** Dermamatch analyzes your inputs and provides the top recommended skincare ingredients for each of your concerns.
5. **Generate Routine:** View a structured skincare routine detailing when and how to apply each recommended product.

## Installation

### Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package installer)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/dermamatch.git
   cd dermamatch
   ```

2. **Run the Application**

   ```bash
   python app.py
   ```

3. **Access the Application**

   Open your web browser and navigate to `http://127.0.0.1:5000/` to start using Dermamatch.

## Usage

1. **Home Page**

   - **Skin Type Selection:** Choose your skin type from the dropdown menu.
   - **Select Skin Problems:** Check the boxes corresponding to your skin concerns.
   - **Avoid Ingredients (Optional):** Enter any ingredients you wish to avoid.

2. **Recommendations Page**

   - **Ingredient Suggestions:** View the top recommended ingredients for each of your selected skin problems.
   - **Skincare Routine:** See a suggested skincare routine with product forms (e.g., serum, moisturizer, cleanser) based on your recommendations.



## Technologies Used

- **Python 3.7+**
- **Flask:** Web framework for building the application.
- **HTML/CSS:** Frontend design and styling.
- **JavaScript (Optional):** For enhanced interactivity.


*Disclaimer: Dermamatch provides skincare recommendations based on general information. For personalized medical advice, consult a dermatologist.*


© 2024 Dermamatch
