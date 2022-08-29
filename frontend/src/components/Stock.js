import React from 'react';

const Stock = ({foundStock}) => {

    return (
        <div>
        {foundStock !== null ? 
            <div>
                <h1>{foundStock.ticker}</h1>
                <p>{foundStock.currency}</p>
                <p>{foundStock.summary}</p>
                <p>{foundStock._current_price}</p>
            </div>
        : <>hi</>}
        </div>
    );
}

export default Stock;