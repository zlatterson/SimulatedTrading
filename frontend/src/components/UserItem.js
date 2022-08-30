import React from 'react';
import BuySellItem from './BuySellItem';
import BuySellList from './BuySellList';
import CallPutList from './CallPutList';

const UserItem = ({user,viewOnly,setSelectedUserId,selectedUserBuySellActions, selectedUserId, sellQuantityInput, setSellQuantityInput, setSentSellOrder, callputOptions}) => {

    const handleClick = () => {
        setSelectedUserId(user.id)
    }

    return (
    <li>
        <h3 onClick={handleClick}>@{user.username} {user.name} ${user.money}</h3>
        {user.id === selectedUserId ? 
        <div>
        <CallPutList viewOnly={viewOnly} callputOptions={callputOptions}/>
        <BuySellList viewOnly={viewOnly} selectedUserBuySellActions={selectedUserBuySellActions} sellQuantityInput={sellQuantityInput} setSellQuantityInput={setSellQuantityInput} setSentSellOrder={setSentSellOrder} user={user}/> 
        </div>
        : <></>}
    </li>
    );
}

export default UserItem;