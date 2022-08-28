const baseURL = 'http://127.0.0.1:5000/users'

export const all_users = () => {
    return fetch(`${baseURL}`)
        .then(res => res.json())
}