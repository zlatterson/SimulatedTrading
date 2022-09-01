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
    <>
    
<tr>
<td>{buySellAction.stock.ticker}</td>
<td>{buySellAction.buy_sell_type}</td>
<td>{buySellAction.quantity}</td>
<td>${(buySellAction.stock._current_price * buySellAction.quantity).toFixed(2)}</td>
<td style={{color: ((buySellAction.stock._current_price - buySellAction.average_price)* buySellAction.quantity) >= 0 ? "green" : "red"}}>${((buySellAction.stock._current_price - buySellAction.average_price)* buySellAction.quantity).toFixed(2)} ({buySellAction.score.toFixed(2)})%</td>
<td>{buySellAction.average_price.toFixed(2)}</td>
<td>{buySellAction.stock._current_price.toFixed(2)}</td>
<td>
{viewOnly === true ?
     <></>
     : <>
  <form onSubmit={newSubmit}>
  <input className="form-color" type="number" min="1" max={buySellAction.quantity} onChange={handleSearchInput} placeholder="ALL"></input>
  <input type="submit" value="Sell" class="btn btn-success"/>
  </form>
     </>
  }
</td>
</tr>
</>
  );
}

export default BuySellItem;