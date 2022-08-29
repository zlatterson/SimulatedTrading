import React from 'react';

const StockOrderBuySell = ({user, stock, quantityInput, setQuantityInput, setSentBuySellOrder }) => {

    const handleSearchInput = (e) => {
        let { value, min, max } = e.target;
        value = Math.max(Number(min), Math.min(Number(max), Number(value)));
        setQuantityInput(value)
      }
      const newSubmit = (e) => {
        e.preventDefault();
        let jsonArray = [];
        let jsonObject = { name : 'abc',quantity : quantityInput, gender : 'Male'};
        jsonArray.push(jsonObject);
        setSentBuySellOrder(jsonArray)
      }

    return (
        <div>
        {user !== null && stock !== null ? 
            <div>
                <h5>Current price is: ${stock._current_price.toFixed(2)}</h5>
                <h5>Available Balance: ${(user.money.toFixed(2))}</h5>
                <h5>Estimated Cost: ${(quantityInput * stock._current_price).toFixed(2)}</h5>
                <h5>{quantityInput * stock._current_price > user.money ? "Not Enough money" : "Confirm Order"}</h5>
                <form onSubmit={newSubmit}>
                <input type="number" min="1" max={((user.money / stock._current_price).toFixed(0)) - 1} onChange={handleSearchInput} placeholder="Quantity..."></input>
                <input type="submit" value="Order" />
                </form>
            </div>
        : <></>}
        </div>
    );
}

export default StockOrderBuySell;