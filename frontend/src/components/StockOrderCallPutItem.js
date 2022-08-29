import React from 'react';
import CallPutContract from './CallPutContract';

const StockOrderCallPutItem = ({option,selectedOption,setSelectedOption}) => {

    const handleClick = () => {
        setSelectedOption(option["Contract Name"])
        console.log(option["Contract Name"] = selectedOption)
    }

    return (
    <>
    <li onClick={handleClick}> Bid: {option["Bid"]} | Ask: {option["Ask"]}| IV:{option["Implied Volatility"]} | % Change:{option["% Change"]} | {option["Contract Name"]}</li>
    {option["Contract Name"] == selectedOption ? <CallPutContract selectedOption={selectedOption}/> : <></>}
    </>
  );

}

export default StockOrderCallPutItem;