import React from 'react';

const CallPutContract = ({ contract, user, option, optionQuantityInput, setOptionQuantityInput, setSentOptionOrder}) => {
    let orderPrice = option.call_price * 100

    const handleSearchInput = (e) => {
        let { value, min, max } = e.target;
        value = Math.max(Number(min), Math.min(Number(max), Number(value)));
        setOptionQuantityInput(value)
      }
      const newSubmit = (e) => {
        e.preventDefault();
        let objectToSend = { contract, optionQuantityInput, buy_sell_type: "BUY",user_id: user.id};
        setSentOptionOrder(objectToSend)
      }

    return (
        <div>
            Call price: {option.call_price} Strik Price: {option.strike} Day's Range: {option.days_range} Expires: {option.expires} Volume: {option.volume}
        
                <form onSubmit={newSubmit}>
                <input type="number" min="1" max={((user.money / orderPrice).toFixed(0)) - 1} onChange={handleSearchInput} placeholder="Quantity..."></input>
                <input type="submit" value="Order" />
                </form>
        </div>
        
    );
}

export default CallPutContract;