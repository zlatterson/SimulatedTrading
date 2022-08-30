import React from 'react';

const BuySellItem = ({viewOnly, buySellAction, sellQuantityInput, setSellQuantityInput, setSentSellOrder, user}) => {

  const sellQuantity = () => {
    if(sellQuantityInput === null){
      return buySellAction.quantity
    }else{
      return sellQuantityInput
    }
  }

  const handleSearchInput = (e) => {
    let { value, min, max } = e.target;
    value = Math.max(Number(min), Math.min(Number(max), Number(value)));
    setSellQuantityInput(value)
  }
  const newSubmit = (e) => {
    e.preventDefault();
    let objectToSend = {stock_id: buySellAction.stock.id ,quantity: sellQuantity(), buy_sell_type: "SELL",user_id: user.id};
    setSentSellOrder(objectToSend)
  }

  return (
<li>
{buySellAction.buy_sell_type} {buySellAction.quantity} {buySellAction.stock.ticker} @ ${buySellAction.average_price.toFixed(2)} {buySellAction.score.toFixed(2)}%
  {viewOnly === true ?
     <></>
     : <>
  <form onSubmit={newSubmit}>
  <input type="number" min="1" max={buySellAction.quantity} onChange={handleSearchInput} placeholder="Quantity..."></input>
  <input type="submit" value="Sell" />
  </form>
     </>
  }
  <h5>{buySellAction.last_action}</h5>

</li>
  );
}

export default BuySellItem;