import React from 'react';

const StockOrderBuySell = ({user, stock, quantityInput, setQuantityInput, setSentBuySellOrder }) => {

    const handleSearchInput = (e) => {
        setQuantityInput(e.target.value)
      }
      const newSubmit = (e) => {
        e.preventDefault();
        setSentBuySellOrder(quantityInput)
      }

    return (
        <div>
        {user !== null && stock !== null ? 
            <div>
                <h5>Current price is: ${stock._current_price.toFixed(2)}</h5>
                <h5>Available Balance: ${user.money.toFixed(2)}</h5>
                <h5>Estimated Cost: ${(quantityInput * stock._current_price).toFixed(2)}</h5>
                <h5>{quantityInput * stock._current_price > user.money ? "Not Enough money" : "Confirm Order"}</h5>
                <form onSubmit={newSubmit}>
                <input type="number" onChange={handleSearchInput} placeholder="Quantity..."></input>
                <input type="submit" value="Order" />
                </form>
            </div>
        : <></>}
        </div>
    );
}

export default StockOrderBuySell;