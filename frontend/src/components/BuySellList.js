import React from 'react';
import BuySellItem from './BuySellItem';

const BuySellList = ({selectedUserBuySellActions}) => {
    let userBuySellActions = []
    if (selectedUserBuySellActions != null){
        userBuySellActions = selectedUserBuySellActions.map((buySellAction, index)=>{
            return <BuySellItem buySellAction = {buySellAction} key={index}/>
        })
    }
    return (
    <ul>{userBuySellActions}</ul>
    );
}

export default BuySellList;