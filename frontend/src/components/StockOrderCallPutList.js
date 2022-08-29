import React from 'react';
import StockOrderCallPutItem from './StockOrderCallPutItem';

const StockOrderCallPutList = ({user, options }) => {

    const optionNodes = options.map((user, index, options) => {
        return <StockOrderCallPutItem user={user} key={index} options={options}/>
    })
  return (
    <>
    <ul>{optionNodes}</ul>
    </>
  );

}

export default StockOrderCallPutList;