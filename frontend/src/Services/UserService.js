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


// export const insertData = (body) =>{
//     return fetch(`http://localhost:5000/users`,{
//         'method':'POST',
//          headers : {
//         'Content-Type':'application/json'
//   },
//   body:JSON.stringify(body)
// })
// .then(response => response.json())
// .catch(error => console.log(error))
// }
