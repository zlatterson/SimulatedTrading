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
    <div className='buy-sell-box'>
    <h3>Options</h3>
    <table class="table table-striped table-dark text-center align-middle table-sm">
      <tbody>
      <tr>
        <th> Symbol </th>
        <th> Time </th>
        <th> Type </th>
        <th> Description </th>
        <th> Value </th>
        <th> P/L </th>
        <th> Action </th>
      </tr>
      {userCallPutOptions}
      </tbody>
    </table>
    </div>
    </>
    );
}

export default CallPutList;