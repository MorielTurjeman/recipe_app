class Model {
    async getRecipes(ingredient: string, filterDairy: boolean, filterGluten: boolean) {

        const recipes = await $.get(`/recipes/${ingredient}?filter_dairy=${filterDairy}&filter_gluten=${filterGluten}`)
        return recipes

    }
}