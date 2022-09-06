import React from 'react';

const StockOrderBuySell = ({user, stock, quantityInput, setQuantityInput, setSentBuySellOrder }) => {

    const handleSearchInput = (e) => {
        let { value, min, max } = e.target;
        value = Math.max(Number(min), Math.min(Number(max), Number(value)));
        setQuantityInput(value)
      }
      const newSubmit = (e) => {
        e.preventDefault();
        let objectToSend = {stock_id: stock.id ,quantity: quantityInput, buy_sell_type: "BUY",user_id: user.id};
        setSentBuySellOrder(objectToSend)
      }

    return (
        <div>
        {user !== null && stock !== null ? 
            <div>
                <h5>Current price is: ${stock._current_price.toFixed(2)}</h5>
                <h5>Available Balance: ${(user.money.toFixed(2))}</h5>
                <h5 style={{color:'red'}}>Estimated Cost: ${(quantityInput * stock._current_price).toFixed(2)}</h5>
                <form onSubmit={newSubmit}>
                <input type="number" min="1" max={((user.money / stock._current_price).toFixed(0)) - 1} onChange={handleSearchInput} placeholder="Quantity..."></input>
                <input type="submit" value="Order" class="btn btn-warning"/>
                </form>
            </div>
        : <></>}
        </div>
    );
}

export default StockOrderBuySell;