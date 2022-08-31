import React from 'react';
import CallPutContract from './CallPutContract';
import StockOrderBuySell from './StockOrderBuySell';
import StockOrderCallPutList from './StockOrderCallPutList';
import { Container } from 'react-bootstrap';

const Stock = ({foundStock, user,setOrderTypeBuySell,orderTypeBuySell, setOrderTypeCallPut, orderTypeCallPut, quantityInput, setQuantityInput, setSentBuySellOrder, options, setSelectedOption, selectedOption, option, optionQuantityInput, setOptionQuantityInput, setSentOptionOrder}) => {
    const handleBuySellOrder = (e) => {
        e.preventDefault();
        setOrderTypeCallPut(false)
        setOrderTypeBuySell(true)
        setSelectedOption(null)
      }
      const handleCallPutOrder = (e) => {
        e.preventDefault();
        setOrderTypeBuySell(false)
        setOrderTypeCallPut(true)
        setSelectedOption(null)
      }

    return (
        <Container>
        <div className='stock-container'>
        {foundStock !== null ? 
            <div>
                <h1>{foundStock.ticker}</h1>
                <p>{foundStock.summary}</p>
                <button class="table table-striped table-dark text-center align-middle table-sm"onClick={handleBuySellOrder} value="Market Order">
                    Market Order
                </button>
                <button onClick={handleCallPutOrder} value="Call Put Contract">
                    Call Put Contract
                </button>
                {orderTypeBuySell === true ?
                    <StockOrderBuySell user={user} stock={foundStock} quantityInput={quantityInput} setQuantityInput={setQuantityInput} setSentBuySellOrder={setSentBuySellOrder}/> : <></>
                }
                {orderTypeCallPut === true ?
                <div>
                    {option !== null ?
                    <CallPutContract user={user} contract={selectedOption} stock={foundStock} option={option} optionQuantityInput={optionQuantityInput} setOptionQuantityInput={setOptionQuantityInput} setSentOptionOrder={setSentOptionOrder}/>
                    : <></>}
                    <StockOrderCallPutList user={user} options={options} setSelectedOption={setSelectedOption} option={option}/> 
                    </div>
                    : <></>

                }
            </div>
        : <></>}
        </div>
        </Container>
    );
}

export default Stock;