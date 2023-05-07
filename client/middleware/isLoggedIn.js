import { getItem, setItem } from "~/helpers/persistanceStorage"
export default async function(ctx) {
    let user = ctx.app.$cookiz.get('user')
    if (!user) {
        return await ctx.redirect('/auth')
    }
}