import React from 'react';
import StockOrderBuySell from './StockOrderBuySell';

const Stock = ({foundStock, user,setOrderTypeBuySell,orderTypeBuySell, setOrderTypeCallPut, orderTypeCallPut, quantityInput, setQuantityInput, setSentBuySellOrder}) => {
    const handleBuySellOrder = (e) => {
        e.preventDefault();
        setOrderTypeCallPut(false)
        setOrderTypeBuySell(true)
      }
      const handleCallPutOrder = (e) => {
        e.preventDefault();
        setOrderTypeBuySell(false)
        setOrderTypeCallPut(true)
      }

    return (
        <div>
        {foundStock !== null ? 
            <div>
                <h1>{foundStock.ticker}</h1>
                <p>{foundStock.summary}</p>
                <button onClick={handleBuySellOrder} value="Market Order">
                    Market Order
                </button>
                <button onClick={handleCallPutOrder} value="Call Put Contract">
                    Call Put Contract
                </button>
                {orderTypeBuySell === true ?
                    <StockOrderBuySell user={user} stock={foundStock} quantityInput={quantityInput} setQuantityInput={setQuantityInput} setSentBuySellOrder={setSentBuySellOrder}/> : <></>
                }
                {orderTypeCallPut === true ?
                    <StockOrderBuySell user={user} stock={foundStock} quantityInput={quantityInput} setQuantityInput={setQuantityInput} setSentBuySellOrder={setSentBuySellOrder}/> : <></>
                }
            </div>
        : <></>}
        </div>
    );
}

export default Stock;