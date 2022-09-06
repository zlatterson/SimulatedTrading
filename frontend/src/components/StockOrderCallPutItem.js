import React from 'react';
import CallPutContract from './CallPutContract';

const StockOrderCallPutItem = ({option,setSelectedOption, user}) => {

    const handleClick = () => {
        setSelectedOption(option["Contract Name"])
    }

    return (
    <tr onClick={handleClick}>
      <td>{option["Bid"]}</td>
      <td>{option["Ask"]}</td>
      <td>{option["Change"]}</td>
      <td>{option["Volume"]}</td>
      <td>{option["Implied Volatility"]}</td>
      <td>{option["Strike"]}</td>
    </tr>
  );

}

export default StockOrderCallPutItem;