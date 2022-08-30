const baseURL = 'http://127.0.0.1:5000/call_put_options'

export const showOptions = (ticker) => {
    return fetch(`${baseURL}/search/${ticker}`)
        .then(res => res.json())
}
export const showOption = (contractName) => {
    return fetch(`${baseURL}/${contractName}`)
        .then(res => res.json())
}

export const postCallPutOption = (data) => {
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