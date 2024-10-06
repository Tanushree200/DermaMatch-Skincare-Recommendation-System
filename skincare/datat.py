import csv

skincare_ingredients_info = {
    # Paste the skincare ingredients info dictionary here
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

# Extract unique skin problems
skin_problems = set()
for ingredient_info in skincare_ingredients_info.values():
    skin_problems.update(ingredient_info['ratings'].keys())

# Create CSV header
csv_header = ['Ingredients'] + sorted(skin_problems)

# Populate CSV rows
csv_rows = []
for ingredient, info in skincare_ingredients_info.items():
    row = [ingredient]
    for problem in sorted(skin_problems):
        row.append(info['ratings'].get(problem, 'N/A'))
    csv_rows.append(row)

# Write to CSV
with open('skincare_.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)

print("CSV file created successfully.")
