const baseURL = 'http://127.0.0.1:5000/call_put_options'

export const showOptions = (ticker) => {
    return fetch(`${baseURL}/search/${ticker}`)
        .then(res => res.json())
}