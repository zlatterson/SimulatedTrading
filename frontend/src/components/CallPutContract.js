import React from 'react';

const CallPutContract = ({ contract, user, option, optionQuantityInput, setOptionQuantityInput, setSentOptionOrder,stock}) => {
    let orderPrice = option.call_price * 100

    const handleSearchInput = (e) => {
        let { value, min, max } = e.target;
        value = Math.max(Number(min), Math.min(Number(max), Number(value)));
        setOptionQuantityInput(value)
      }
      const newSubmit = (e) => {
        e.preventDefault();
        let objectToSend = { contract, quantity: optionQuantityInput, buy_sell_type: "BUY",call_put_type:"CALL",user_id: user.id, ticker:stock.ticker};
        setSentOptionOrder(objectToSend)
      }

    return (
        <div>
            Call price: {option.call_price} Strike Price: {option.strike} Day's Range: {option.days_range} Expires: {option.expires} Volume: {option.volume}
            <p>cost: ${(optionQuantityInput * option.call_price * 100).toFixed(2)}</p>
                <form onSubmit={newSubmit}>
                <input type="number" min="1" max={((user.money / orderPrice).toFixed(0)) - 1} onChange={handleSearchInput} placeholder="Quantity..."></input>
                <input type="submit" value="Order" />
                </form>
        </div>
        
    );
}

export default CallPutContract;