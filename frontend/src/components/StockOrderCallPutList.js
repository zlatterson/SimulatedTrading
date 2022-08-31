import React from 'react';
import StockOrderCallPutItem from './StockOrderCallPutItem';

const StockOrderCallPutList = ({user, options, setSelectedOption}) => {
    const optionNodes = options.map((option, index) => {
      
        return <StockOrderCallPutItem user={user} key={index} option={option} setSelectedOption={setSelectedOption}/>
    })
  return (
    <>

    <table class="table table-striped text-center align-middle table-sm">
      <caption> Calls </caption>
      <tbody>
      <tr>
        <th>Bid</th>
        <th> Ask</th>
        <th> Change</th>
        <th> Volume</th>
        <th> IV</th>
        <th> Strike </th>
      </tr>
      {optionNodes}
      </tbody>
    </table>

    </>
  );

}

export default StockOrderCallPutList;