const baseURL = 'http://127.0.0.1:5000/buy_sell_actions'


export const postBuySellAction = (data) => {
return fetch(`${baseURL}`, {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    data
  })
})
}