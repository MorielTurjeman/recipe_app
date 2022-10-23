"use strict";



class Controller {
    model: Model;


    constructor() {

        this.model = new Model()
        const search = document.querySelector(".search-btn")
        if (search) {
            search.addEventListener('click', (event) => this.getRecipes())
        }
    }

    async getRecipes() {
        const ing = (document.querySelector("#search") as HTMLInputElement).value
        const gluten = (document.querySelector("#gluten") as HTMLInputElement).checked
        const dairy = (document.querySelector("#dairy") as HTMLInputElement).checked
        this.model.getRecipes(ing, dairy, gluten).then(res => renderRecipes(res))

    }
}

const controller = new Controller();
