import React from 'react';
import UserItem from './UserItem';

function UserList({users, setSelectedUserId, selectedUserBuySellActions, selectedUserId, sellQuantityInput, setSellQuantityInput, setSentSellOrder}) {
 
    const userNodes = users.map((user, index) => {
        return <UserItem user={user} key={index} setSelectedUserId={setSelectedUserId} selectedUserId={selectedUserId} selectedUserBuySellActions={selectedUserBuySellActions} sellQuantityInput={sellQuantityInput} setSellQuantityInput={setSellQuantityInput} setSentSellOrder={setSentSellOrder}/>
    })
  return (
    <>
    <ul>{userNodes}</ul>
    </>
  );
}

export default UserList;
