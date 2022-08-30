import React from 'react';
import StockOrderCallPutItem from './StockOrderCallPutItem';

const StockOrderCallPutList = ({user, options, setSelectedOption}) => {
    const optionNodes = options.map((option, index) => {
        return <StockOrderCallPutItem user={user} key={index} option={option} setSelectedOption={setSelectedOption}/>
    })
  return (
    <>
    <ul>{optionNodes}</ul>
    </>
  );

}

export default StockOrderCallPutList;