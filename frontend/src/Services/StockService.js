const baseURL = 'http://127.0.0.1:5000/stocks'

export const searchStockByTicker = (ticker) => {
    return fetch(`${baseURL}/search/${ticker}`)
        .then(res => res.json())
}