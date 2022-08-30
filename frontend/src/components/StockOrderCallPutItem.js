import React from 'react';
import CallPutContract from './CallPutContract';

const StockOrderCallPutItem = ({option,setSelectedOption, user}) => {

    const handleClick = () => {
        setSelectedOption(option["Contract Name"])
    }

    return (
    <h5>
    <li onClick={handleClick}> Bid: {option["Bid"]} | Ask: {option["Ask"]}| IV:{option["Implied Volatility"]} | % Change:{option["% Change"]} | {option["Contract Name"]}</li>
    </h5>
  );

}

export default StockOrderCallPutItem;