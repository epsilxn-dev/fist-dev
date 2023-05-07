import { getItem, setItem } from "~/helpers/persistanceStorage"
export default async function({ app, store, redirect }) {
    let user = app.$cookiz.get('user')
    let resume = await (await app.store.dispatch('lk/setResume', user.id))

    return
    if (resume) {
        return redirect(`/job/resumes/edit/${user.id}`)
    }
}