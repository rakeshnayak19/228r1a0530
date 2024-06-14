document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("recipe-modal");
    const closeButton = document.querySelector(".close-button");
    const recipeDetails = document.getElementById("recipe-details");
    const recipeSection = document.getElementById("recipe-section");
    let nextRecipeId = 10; // Updated nextRecipeId

    const recipes = {
        1: {
            title: "Strawberry Custard",
            description: "A creamy, dreamy dessert that combines the rich flavor of custard with fresh strawberries.",
            ingredients: "Milk, Sugar, Eggs, Strawberries",
            instructions: "Mix ingredients, cook over medium heat, chill before serving.",
            calories: "330 kcal",
            proteins: "6 grams",
            image: "dish-1.jpg"
        },
        2: {
            title: "Blueberry Pancakes",
            description: "Fluffy pancakes with fresh blueberries.",
            ingredients: "Flour, Milk, Eggs, Blueberries, Sugar, Baking Powder",
            instructions: "Mix dry ingredients, add wet ingredients, cook on griddle.",
            calories: "350 kcal",
            proteins: "10 grams",
            image: "dish-2.jpg"
        },
        3: {
            title: "Chicken Salad",
            description: "A healthy mix of chicken, veggies, and a light dressing.",
            ingredients: "Chicken, Lettuce, Tomato, Cucumber, Olive Oil, Lemon",
            instructions: "Grill chicken, chop veggies, mix together with dressing.",
            calories: "350 kcal",
            proteins: "25 grams",
            image: "dish-3.jpg"
        },
        4: {
            title: "Vegan Tacos",
            description: "Packed with fresh vegetables and savory plant-based protein.",
            ingredients: "Tortillas, Black Beans, Corn, Avocado, Salsa, Lettuce",
            instructions: "Warm tortillas, add fillings, serve with salsa.",
            calories: "200 kcal",
            proteins: "8 grams",
            image: "dish-4.jpg"
        },
        5: {
            title: "Grilled Salmon",
            description: "A perfect blend of succulent fish and flavorful spices.",
            ingredients: "Salmon, Lemon, Olive Oil, Garlic, Salt, Pepper",
            instructions: "Marinate salmon, grill until cooked through.",
            calories: "400 kcal",
            proteins: "40 grams",
            image: "fish-dish.jpg"
        },
        6: {
            title: "Milk Tea",
            description: "A refreshing and popular beverage combining the richness of milk with the robust flavor of tea.",
            ingredients: "Black Tea, Milk, Sugar, Water",
            instructions: "Brew tea, mix with milk and sugar, serve hot or cold.",
            calories: "150 kcal",
            proteins: "5 g",
            image: "milk-tea.jpg"
        }
    };

    document.querySelectorAll(".view-recipe").forEach(function(button) {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            const recipeId = this.closest(".recipe-card").getAttribute("data-recipe");
            showRecipe(recipeId);
        });
    });

    function showRecipe(recipeId) {
        const recipe = recipes[recipeId];
        recipeDetails.innerHTML = `
            <h2>${recipe.title}</h2>
            <p>${recipe.description}</p>
            <h3>Ingredients</h3>
            <p>${recipe.ingredients}</p>
            <h3>Instructions</h3>
            <p>${recipe.instructions}</p>
            <h3>Calories</h3>
            <p>${recipe.calories}</p>
            <h3>Proteins</h3>
            <p>${recipe.proteins}</p>
        `;
        modal.style.display = "block";
    }

    closeButton.addEventListener("click", function() {
        modal.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });

    document.getElementById("search-form").addEventListener("submit", function(event) {
        event.preventDefault();
        const searchInput = document.getElementById("search-input").value.toLowerCase();
        for (const key in recipes) {
            if (recipes[key].title.toLowerCase().includes(searchInput)) {
                showRecipe(key);
                break;
            }
        }
    });

    document.getElementById("add-recipe-form").addEventListener("submit", function(event) {
        event.preventDefault();
        const title = document.getElementById("recipe-title").value;
        const description = document.getElementById("recipe-description").value;
        const ingredients = document.getElementById("recipe-ingredients").value;
        const instructions = document.getElementById("recipe-instructions").value;
        const image = document.getElementById("recipe-image").value;
        const calories = document.getElementById("recipe-calories").value;
        const proteins = document.getElementById("recipe-proteins").value;

        const newRecipe = {
            title,
            description,
            ingredients,
            instructions,
            calories,
            proteins,
            image
        };

        recipes[nextRecipeId] = newRecipe;

        const newRecipeCard = document.createElement("div");
        newRecipeCard.classList.add("recipe-card");
        newRecipeCard.setAttribute("data-recipe", nextRecipeId);
        newRecipeCard.innerHTML = `
            <img src="${image}" alt="not available">
            <h2>${title}</h2>
            <p><strong>${title}</strong> ${description}</p>
            <p><strong>Calories:</strong> ${calories}</p>
            <p><strong>Proteins:</strong> ${proteins}</p>
            <a href="#" class="view-recipe">View Recipe</a>
        `;

        newRecipeCard.querySelector(".view-recipe").addEventListener("click", function(event) {
            event.preventDefault();
            showRecipe(nextRecipeId);
        });

        recipeSection.appendChild(newRecipeCard);
        nextRecipeId++;
    });

    // Adding new recipe cards to the recipe section
    const newRecipes = []; // If you have new recipes, add them to this array
    newRecipes.forEach(function(recipe) {
        const newRecipeCard = document.createElement("div");
        newRecipeCard.classList.add("recipe-card");
        newRecipeCard.setAttribute("data-recipe", nextRecipeId);
        newRecipeCard.innerHTML = `
            <img src="${recipe.image}" alt="not available">
            <h2>${recipe.title}</h2>
            <p><strong>${recipe.title}</strong> ${recipe.description}</p>
           c</strong> ${recipe.calories}</p>
            <p><strong>Proteins:</strong> ${recipe.proteins}</p>
            <a href="#" class="view-recipe">View Recipe</a>
        `;

        newRecipeCard.querySelector(".view-recipe").addEventListener("click", function(event) {
            event.preventDefault();
            showRecipe(nextRecipeId);
        });

        recipeSection.appendChild(newRecipeCard);
        nextRecipeId++;
    });
});
