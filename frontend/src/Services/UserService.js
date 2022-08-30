const baseURL = 'http://127.0.0.1:5000/users'

export const showUsers = () => {
    return fetch(baseURL)
        .then(res => res.json())
}
export const showUser = (id) => {
    return fetch(`${baseURL}/${id}`)
        .then(res => res.json())
}
export const showUserBuySellActions = (id) => {
    return fetch(`${baseURL}/${id}/buy_sell_actions`)
        .then(res => res.json())
}
export const showUserCallPutOptions = (id) => {
    return fetch(`${baseURL}/${id}/call_put_options`)
        .then(res => res.json())
}
