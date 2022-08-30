import React from 'react';

const CallPutItem = ({option}) => {
    console.log(option.bought_c_price)
    return (
        <li>
            {option.bought_c_price} {option.bought_c_value} ${option.bought_contracts_value * option.n_contracts}
        <h5>{option.timestamp} . Expires: {option.call_put_contract.expires}</h5>
        </li>
        
    );
}

export default CallPutItem;