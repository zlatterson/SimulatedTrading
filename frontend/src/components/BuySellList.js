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
    <>
    <table>
      <tbody>
      <tr>
        <th> Symbol </th>
        <th> Type </th>
        <th> Shares </th>
        <th> Value </th>
        <th> Return </th>
        <th> Average Buy Price</th>
        <th> Price/Share</th>
        <th> Sell </th>
      </tr>
      {userBuySellActions}
      </tbody>
    </table>

    </>
    


    );
}

export default BuySellList;