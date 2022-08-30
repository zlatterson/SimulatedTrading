import React from 'react';

const BuySellItem = ({buySellAction, sellQuantityInput, setSellQuantityInput, setSentSellOrder, user}) => {

  const handleSearchInput = (e) => {
    let { value, min, max } = e.target;
    value = Math.max(Number(min), Math.min(Number(max), Number(value)));
    setSellQuantityInput(value)
  }
  const newSubmit = (e) => {
    e.preventDefault();
    let objectToSend = {stock_id: buySellAction.stock.id ,quantity: sellQuantityInput, buy_sell_type: "SELL",user_id: user.id};
    setSentSellOrder(objectToSend)
  }

  return (
<li>
{buySellAction.buy_sell_type} {buySellAction.quantity} {buySellAction.stock.ticker} @ ${buySellAction.average_price.toFixed(2)} {buySellAction.score.toFixed(2)}%
<h5>{buySellAction.last_action}</h5>
  <form onSubmit={newSubmit}>

  <input type="number" min="1" max={buySellAction.quantity} onChange={handleSearchInput} placeholder="Quantity..."></input>
  <input type="submit" value="Sell" />
  </form>

</li>
  );
}

export default BuySellItem;