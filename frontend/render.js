"use strict";
const recipeSource = $("#recipes-template").html();
function renderRecipes(recipes) {
    console.log(recipes);
    $("#results").empty();
    const template = Handlebars.compile(recipeSource);
    console.log(template);
    // console.log(template)
    const newHtml = template({ recipes });
    console.log(newHtml);
    $("#results").append(newHtml);
}
