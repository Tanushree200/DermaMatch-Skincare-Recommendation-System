# Define a dictionary of skincare ingredients along with their application instructions, ratings for each skin problem,
# information about compatibility with other ingredients, and descriptions
skincare_ingredients_info = {
    "Hyaluronic acid": {
        "instructions": "Apply a few drops to clean, damp skin before applying moisturizer. Can be used morning and night.",
        "ratings": {"acne": 4, "eczema": 5, "blackheads": 3, "hyperpigmentation": 4, "sensitive skin": 4, "fine lines and wrinkles": 4, "uneven skin texture": 4, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 4, "dehydrated skin": 5, "redness and irritation": 3, "melasma and age spots": 3},
        "incompatible_with": ["Vitamin C"],
    },
    "Vitamin C": {
        "instructions": "Apply a small amount to clean, dry skin in the morning before sunscreen.",
        "ratings": {"acne": 3, "eczema": 4, "blackheads": 2, "hyperpigmentation": 5, "sensitive skin": 3, "fine lines and wrinkles": 4, "uneven skin texture": 4, "dullness": 4, "dark circles and puffiness": 2, "sun damage": 5, "enlarged pores": 3, "uneven skin tone": 5, "dehydrated skin": 3, "redness and irritation": 3, "melasma and age spots": 4},
        "incompatible_with": ["Niacinamide"],
    },
    "Niacinamide": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 4, "eczema": 4, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 4, "fine lines and wrinkles": 4, "uneven skin texture": 4, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 4, "uneven skin tone": 4, "dehydrated skin": 3, "redness and irritation": 3, "melasma and age spots": 3},
        "incompatible_with": ["Vitamin C"],
    },
    "Retinol": {
        "instructions": "Apply a pea-sized amount to clean, dry skin at night. Start with a lower concentration and gradually increase frequency.",
        "ratings": {"acne": 3, "eczema": 2, "blackheads": 3, "hyperpigmentation": 5, "sensitive skin": 3, "fine lines and wrinkles": 5, "uneven skin texture": 5, "dullness": 4, "dark circles and puffiness": 2, "sun damage": 5, "enlarged pores": 3, "uneven skin tone": 4, "dehydrated skin": 3, "redness and irritation": 3, "melasma and age spots": 5},
        "incompatible_with": [],
    },
    "Glycerin": {
        "instructions": "Apply a small amount to clean, damp skin before applying moisturizer. Can be used morning and night.",
        "ratings": {"acne": 3, "eczema": 5, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 4, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 5, "redness and irritation": 3, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Ceramides": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 5, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 4, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 5, "redness and irritation": 3, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Squalane": {
        "instructions": "Apply a few drops to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 4, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 4, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 5, "redness and irritation": 3, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Salicylic acid": {
        "instructions": "Apply a thin layer to affected areas after cleansing. Use once or twice daily, preferably in the evening.",
        "ratings": {"acne": 5, "eczema": 2, "blackheads": 4, "hyperpigmentation": 3, "sensitive skin": 3, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 2, "sun damage": 3, "enlarged pores": 5, "uneven skin tone": 3, "dehydrated skin": 3, "redness and irritation": 4, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Glycolic acid": {
        "instructions": "Apply a small amount to clean, dry skin at night. Start with a lower concentration and gradually increase frequency.",
        "ratings": {"acne": 3, "eczema": 2, "blackheads": 4, "hyperpigmentation": 5, "sensitive skin": 3, "fine lines and wrinkles": 3, "uneven skin texture": 5, "dullness": 5, "dark circles and puffiness": 2, "sun damage": 4, "enlarged pores": 3, "uneven skin tone": 5, "dehydrated skin": 3, "redness and irritation": 3, "melasma and age spots": 4},
        "incompatible_with": [],
    },
    "Tea tree oil": {
        "instructions": "Dilute with a carrier oil and apply a small amount to affected areas.",
        "ratings": {"acne": 5, "eczema": 3, "blackheads": 4, "hyperpigmentation": 3, "sensitive skin": 4, "fine lines and wrinkles": 2, "uneven skin texture": 2, "dullness": 2, "dark circles and puffiness": 2, "sun damage": 3, "enlarged pores": 5, "uneven skin tone": 3, "dehydrated skin": 2, "redness and irritation": 4, "melasma and age spots": 2},
        "incompatible_with": [],
    },
    "Aloe vera": {
        "instructions": "Apply a thin layer to clean, dry skin morning and night.",
        "ratings": {"acne": 4, "eczema": 5, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 4, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 5, "redness and irritation": 4, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Oat extract": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 5, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 5, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 5, "redness and irritation": 5, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Centella asiatica": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 4, "eczema": 4, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 5, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 5, "redness and irritation": 5, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Alpha arbutin": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 3, "blackheads": 3, "hyperpigmentation": 5, "sensitive skin": 3, "fine lines and wrinkles": 3, "uneven skin texture": 4, "dullness": 4, "dark circles and puffiness": 3, "sun damage": 4, "enlarged pores": 3, "uneven skin tone": 5, "dehydrated skin": 3, "redness and irritation": 3, "melasma and age spots": 4},
        "incompatible_with": [],
    },
    "Vitamin E": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 4, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 4, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 4, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 5, "redness and irritation": 3, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Green tea extract": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 4, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 4, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 4, "enlarged pores": 3, "uneven skin tone": 4, "dehydrated skin": 3, "redness and irritation": 3, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Honey": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 4, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 4, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 5, "redness and irritation": 4, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Peptides": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 3, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 3, "fine lines and wrinkles": 5, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 3, "redness and irritation": 3, "melasma and age spots": 3},
        "incompatible_with": [],
    },
    "Kojic acid": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 2, "blackheads": 4, "hyperpigmentation": 5, "sensitive skin": 3, "fine lines and wrinkles": 3, "uneven skin texture": 4, "dullness": 4, "dark circles and puffiness": 3, "sun damage": 4, "enlarged pores": 3, "uneven skin tone": 5, "dehydrated skin": 3, "redness and irritation": 3, "melasma and age spots": 5},
        "incompatible_with": [],
    },
    "Caffeine": {
        "instructions": "Apply a small amount to the eye area and gently pat until absorbed.",
        "ratings": {"acne": 2, "eczema": 3, "blackheads": 2, "hyperpigmentation": 3, "sensitive skin": 3, "fine lines and wrinkles": 3, "uneven skin texture": 2, "dullness": 2, "dark circles and puffiness": 5, "sun damage": 2, "enlarged pores": 2, "uneven skin tone": 2, "dehydrated skin": 2, "redness and irritation": 2, "melasma and age spots": 2},
        "incompatible_with": [],
    },
    "Collagen": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 3, "eczema": 2, "blackheads": 3, "hyperpigmentation": 4, "sensitive skin": 3, "fine lines and wrinkles": 5, "uneven skin texture": 4, "dullness": 3, "dark circles and puffiness": 2, "sun damage": 4, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 3, "redness and irritation": 3, "melasma and age spots": 4},
        "incompatible_with": [],
    },
    "Cica": {
        "instructions": "Apply a small amount to clean, dry skin morning and night.",
        "ratings": {"acne": 4, "eczema": 4, "blackheads": 3, "hyperpigmentation": 3, "sensitive skin": 5, "fine lines and wrinkles": 3, "uneven skin texture": 3, "dullness": 3, "dark circles and puffiness": 3, "sun damage": 3, "enlarged pores": 3, "uneven skin tone": 3, "dehydrated skin": 5, "redness and irritation": 5, "melasma and age spots": 3},
        "incompatible_with": [],
    }
}

# Define a dictionary of skin types and corresponding skincare concerns
skincare_recommendations = {
    "normal": ["Hyaluronic acid", "Vitamin C", "Niacinamide", "Retinol", "Glycolic acid", "Ceramides", "Squalane", "Green tea extract", "Honey", "Centella asiatica", "Alpha arbutin", "Vitamin E", "Peptides"],
    "dry": ["Hyaluronic acid", "Vitamin C", "Niacinamide", "Glycerin", "Ceramides", "Squalane", "Aloe vera", "Oat extract", "Honey", "Centella asiatica", "Vitamin E", "Peptides"],
    "oily": ["Niacinamide", "Salicylic acid", "Glycolic acid", "Tea tree oil", "Squalane", "Green tea extract", "Honey", "Centella asiatica", "Vitamin E", "Peptides"],
    "combination": ["Hyaluronic acid", "Niacinamide", "Retinol", "Squalane", "Salicylic acid", "Glycolic acid", "Ceramides", "Aloe vera", "Centella asiatica", "Vitamin E", "Peptides"],
    "sensitive": ["Hyaluronic acid", "Niacinamide", "Ceramides", "Squalane", "Aloe vera", "Oat extract", "Centella asiatica", "Vitamin E", "Peptides"]
}

# Define a list of skin problems for the user to choose from
skin_problems_list = [
    "acne", "eczema", "blackheads", "hyperpigmentation", "sensitive skin", "fine lines and wrinkles",
    "uneven skin texture", "dullness", "dark circles and puffiness", "sun damage", "enlarged pores",
    "uneven skin tone", "dehydrated skin", "redness and irritation", "melasma and age spots"
]


skincare_ingredient_forms = {
    "Hyaluronic acid": "serum",
    "Vitamin C": "serum",
    "Niacinamide": "serum",
    "Retinol": "serum",
    "Glycerin": "moisturizer",
    "Ceramides": "moisturizer",
    "Squalane": "moisturizer",
    "Salicylic acid": "cleanser",
    "Glycolic acid": "toner",
    "Tea tree oil": "spot treatment",
    "Aloe vera": "moisturizer",
    "Oat extract": "moisturizer",
    "Centella asiatica": "moisturizer",
    "Alpha arbutin": "serum",
    "Vitamin E": "moisturizer",
    "Green tea extract": "toner",
    "Honey": "mask",
    "Peptides": "serum",
    "Kojic acid": "serum",
    "Caffeine": "eye cream",
    "Collagen": "serum",
    "Cica": "moisturizer"
}

def generate_skincare_routine(recommendations):
    skincare_routine = {}
    for problem, ingredients in recommendations.items():
        for ingredient in ingredients:
            form = skincare_ingredient_forms.get(ingredient, "unknown")
            if form in skincare_routine:
                # Check if ingredient is already in the routine for this form
                if ingredient not in skincare_routine[form]:
                    skincare_routine[form].append(ingredient)
            else:
                skincare_routine[form] = [ingredient]
    return skincare_routine






def recommend_skincare(skin_type, skin_problems, avoid_ingredients):
    # Get the recommended ingredients for the specified skin type
    recommended_ingredients = skincare_recommendations.get(skin_type.lower(), [])
    
    # Remove duplicates and filter out ingredients to avoid
    recommended_ingredients = list(set(recommended_ingredients) - set(avoid_ingredients))
    
    # Initialize a dictionary to store recommendations for each skin problem
    recommendations = {} 
    
    # Find the two best-rated ingredients for each skin problem
    for problem in skin_problems:
        sorted_ingredients = sorted(recommended_ingredients, key=lambda x: skincare_ingredients_info[x]["ratings"][problem], reverse=True)
        top_two_ingredients = sorted_ingredients[:2]
        recommendations[problem] = top_two_ingredients
        
    
    return recommendations



from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    skin_types = list(skincare_recommendations.keys())
    skin_problems = skin_problems_list
    return render_template('index.html', skin_types=skin_types, skin_problems=skin_problems, skincare_ingredients_info=skincare_ingredients_info)


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        skin_type = request.form['skin_type']
        skin_problems = request.form.getlist('skin_problems')
        avoid_ingredients = request.form.getlist('avoid_ingredients')
        
        recommendations = recommend_skincare(skin_type, skin_problems, avoid_ingredients)
        skincare_routine = generate_skincare_routine(recommendations)
        return render_template('recommendations.html', recommendations=recommendations, skin_problems=skin_problems, skincare_ingredients_info=skincare_ingredients_info,skincare_routine=skincare_routine)

if __name__ == '__main__':
    app.run(debug=True)

