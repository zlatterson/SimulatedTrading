import React from 'react';
import UserItem from './UserItem';

function UserList({users, setSelectedUserId}) {
 
    const userNodes = users.map((user, index) => {
      console.log(user)
        return <UserItem user={user} key={index} setSelectedUserId={setSelectedUserId}/>
    })
  return (
    <>
    <ul>{userNodes}</ul>
    </>
  );
}

export default UserList;
