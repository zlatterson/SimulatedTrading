import React from 'react';
import BuySellItem from './BuySellItem';
import BuySellList from './BuySellList';

const UserItem = ({user,setSelectedUserId,selectedUserBuySellActions, selectedUserId}) => {

    const handleClick = () => {
        setSelectedUserId(user.id)
    }

    return (
    <li>
        <h3 onClick={handleClick}>@{user.username} {user.name} ${user.money}</h3>
        {user.id === selectedUserId ? <BuySellList selectedUserBuySellActions={selectedUserBuySellActions}/> : <></>}
    </li>
    );
}

export default UserItem;