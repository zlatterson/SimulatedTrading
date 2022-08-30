import React from 'react';

const CallPutItem = ({option}) => {

    let currentContractValue = (option.call_put_contract.current_c_price * 100) - (option.bought_c_price * 100)
    console.log((currentContractValue / (option.bought_c_price * 100)) * 100)
    // console.log(((option.call_put_contract.current_c_price * 100) - (option.bought_c_price * 100)) * option.n_contracts)

    return (
        <li>
            {option.bought_c_price} {option.bought_c_value} ${option.bought_contracts_value * option.n_contracts} Running P/L:{((currentContractValue / (option.bought_c_price * 100)) * 100).toFixed(2)}%
        <h5>{option.timestamp} . Expires: {option.call_put_contract.expires}</h5>
        </li>
        
    );
}

export default CallPutItem;