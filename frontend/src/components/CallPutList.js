import React from 'react';
import BuySellItem from './BuySellItem';
import CallPutItem from './CallPutItem';

const CallPutList = ({callputOptions, setExerciseOrder, viewOnly}) => {
    let userCallPutOptions = []
    if (callputOptions !== null){
        userCallPutOptions = callputOptions.map((option, index)=>{
            return <CallPutItem key={index} viewOnly={viewOnly} option={option} setExerciseOrder={setExerciseOrder}/>
        })
    }
    return (
    <>
    <table>
      <tbody>
      <tr>
        <th> Time </th>
        <th> Symbol </th>
        <th> Type </th>
        <th> Description </th>
        <th> Value </th>
        <th> Return </th>
        <th> Action </th>
      </tr>
      {userCallPutOptions}
      </tbody>
    </table>
    </>
    );
}

export default CallPutList;