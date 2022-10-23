"use strict";



class Controller {
    model: Model;


    constructor() {

        this.model = new Model()
        const search = document.querySelector(".search-btn")
        if (search) {
            search.addEventListener('click', (event) => this.getRecipes())
        }

        $("#results").on("click", ".card-img-top", (event) => this.alert_ing(event))
    }

    async getRecipes() {
        const ing = (document.querySelector("#search") as HTMLInputElement).value
        const gluten = (document.querySelector("#gluten") as HTMLInputElement).checked
        const dairy = (document.querySelector("#dairy") as HTMLInputElement).checked
        this.model.getRecipes(ing, dairy, gluten).then(res => renderRecipes(res))

    }

    // $("#results").on("click", ".addToDreamTeam", (event) => this.addToDreamTeam(event))

    alert_ing(event: JQuery.ClickEvent) {

        const recipe = ((event.target as HTMLElement).closest(".card") as HTMLElement).dataset.ing
        alert(recipe)


    }
}

const controller = new Controller();
