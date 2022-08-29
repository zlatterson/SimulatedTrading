import React from 'react';
import UserItem from './UserItem';

function UserList({users, setSelectedUserId, selectedUserBuySellActions, selectedUserId}) {
 
    const userNodes = users.map((user, index) => {
        return <UserItem user={user} key={index} setSelectedUserId={setSelectedUserId} selectedUserId={selectedUserId} selectedUserBuySellActions={selectedUserBuySellActions}/>
    })
  return (
    <>
    <ul>{userNodes}</ul>
    </>
  );
}

export default UserList;
