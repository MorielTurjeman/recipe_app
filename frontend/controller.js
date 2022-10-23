"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
class Controller {
    constructor() {
        this.model = new Model();
        const search = document.querySelector(".search-btn");
        if (search) {
            search.addEventListener('click', (event) => this.getRecipes());
        }
        $("#results").on("click", ".card-img-top", (event) => this.alert_ing(event));
    }
    getRecipes() {
        return __awaiter(this, void 0, void 0, function* () {
            const ing = document.querySelector("#search").value;
            const gluten = document.querySelector("#gluten").checked;
            const dairy = document.querySelector("#dairy").checked;
            this.model.getRecipes(ing, dairy, gluten).then(res => renderRecipes(res));
        });
    }
    // $("#results").on("click", ".addToDreamTeam", (event) => this.addToDreamTeam(event))
    alert_ing(event) {
        const recipe = event.target.closest(".card").dataset.ing;
        alert(recipe);
    }
}
const controller = new Controller();
