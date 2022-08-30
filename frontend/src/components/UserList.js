import React from 'react';
import UserItem from './UserItem';

function UserList({users, viewOnly, setSelectedUserId, selectedUserBuySellActions, selectedUserId, sellQuantityInput, setSellQuantityInput, setSentSellOrder, callputOptions}) {
 
    const userNodes = users.map((user, index) => {
        return <UserItem user={user} key={index} viewOnly={viewOnly} setSelectedUserId={setSelectedUserId} selectedUserId={selectedUserId} selectedUserBuySellActions={selectedUserBuySellActions} sellQuantityInput={sellQuantityInput} setSellQuantityInput={setSellQuantityInput} setSentSellOrder={setSentSellOrder} callputOptions={callputOptions}/>
    })
  return (
    <>
    <ul>{userNodes}</ul>
    </>
  );
}

export default UserList;
