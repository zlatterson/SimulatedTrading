import React from 'react';

const StockOrderCallPutList = ({user, stock, quantityInput, setQuantityInput, setSentBuySellOrder }) => {
    const optionNodes = options.map((user, index) => {
        return <UserItem user={user} key={index} setSelectedUserId={setSelectedUserId} selectedUserId={selectedUserId} selectedUserBuySellActions={selectedUserBuySellActions}/>
    })
  return (
    <>
    <ul>{optionNodes}</ul>
    </>
  );

}

export default StockOrderCallPutList;