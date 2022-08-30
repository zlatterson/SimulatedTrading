import React from 'react';

const CallPutItem = ({viewOnly, option,setExerciseOrder}) => {
    let currentContractValue = (option.call_put_contract.current_c_price * 100) - (option.bought_c_price * 100)
    const newSubmit = (e) => {
        e.preventDefault();
        let objectToSend = {call_put_option_id: option.id};
        setExerciseOrder(objectToSend)
    }
    return (
        <li>
            {option.buy_sell_type} {option.n_contracts} {option.call_put_contract.stock.ticker} {option.call_put_contract.call_put_type} @{option.bought_c_price.toFixed(2)}
        <p>Cost: ${(option.bought_contracts_value * option.n_contracts).toFixed(2)} Exercise for: ${((option.bought_contracts_value * option.n_contracts)-(currentContractValue * option.n_contracts)).toFixed(2)} (${(currentContractValue * option.n_contracts).toFixed(2)}) Running P/L:{((currentContractValue / (option.bought_c_price * 100)) * 100).toFixed(2)}%</p>
        {viewOnly === true ?
        <></>
        : <>
        <form onSubmit={newSubmit}>
        <input type="submit" value="Exercise" />
        </form>
        </>
        }
        <h5>{option.timestamp} . Expires: {option.call_put_contract.expires}</h5>
        </li>
        
    );
}

export default CallPutItem;