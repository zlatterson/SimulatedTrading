import React from 'react';
import BuySellItem from './BuySellItem';

const BuySellList = ({viewOnly, selectedUserBuySellActions, sellQuantityInput, setSellQuantityInput, setSentSellOrder, user}) => {
    let userBuySellActions = []
    if (selectedUserBuySellActions != null){
        userBuySellActions = selectedUserBuySellActions.map((buySellAction, index)=>{
            return <BuySellItem viewOnly={viewOnly} buySellAction = {buySellAction} key={index} sellQuantityInput={sellQuantityInput} setSellQuantityInput={setSellQuantityInput} setSentSellOrder={setSentSellOrder} user={user}/>
        })
    }
    return (
    <ul>{userBuySellActions}</ul>
    );
}

export default BuySellList;