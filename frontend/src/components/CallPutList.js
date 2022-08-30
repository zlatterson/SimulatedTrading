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
    <ul>{userCallPutOptions}</ul>
    );
}

export default CallPutList;