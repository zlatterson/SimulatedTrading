import React from 'react';

const BuySellItem = ({buySellAction}) => {
  
  return (
<li>
{buySellAction.buy_sell_type} {buySellAction.quantity} {buySellAction.stock.ticker} @ ${buySellAction.average_price} +{buySellAction.score}%
<h5>{buySellAction.last_action}</h5>
</li>
  );
}

export default BuySellItem;