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
        <h3 onClick={handleClick}>@{user.username}</h3>
        {user.id === selectedUserId ? 
        <div>
        <BuySellList viewOnly={viewOnly} selectedUserBuySellActions={selectedUserBuySellActions} sellQuantityInput={sellQuantityInput} setSellQuantityInput={setSellQuantityInput} setSentSellOrder={setSentSellOrder} user={user}/> 
        <CallPutList viewOnly={viewOnly} callputOptions={callputOptions}/>

        </div>
        : <></>}
    </li>
    );
}

export default UserItem;