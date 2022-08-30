import React from 'react';
import BuySellItem from './BuySellItem';
import CallPutItem from './CallPutItem';

const CallPutList = ({callputOptions}) => {
    let userCallPutOptions = []
    if (callputOptions !== null){
        userCallPutOptions = callputOptions.map((option, index)=>{
            return <CallPutItem key={index} option={option}/>
        })
    }
    return (
    <ul>{userCallPutOptions}</ul>
    );
}

export default CallPutList;