import React from 'react';

const StockSearch = ({setSearchedTicker, searchInput, setSearchInput}) => {
    const handleSearchInput = (e) => {
        setSearchInput(e.target.value)
      }
      const newSubmit = (e) => {
        e.preventDefault();
        setSearchedTicker(searchInput)
      }
  return (
    <form onSubmit={newSubmit}>
    <input type="text" onChange={handleSearchInput} placeholder="Search ticker or place order directly..."></input>
    <input type="submit" value="Search" />
  </form>
  );
}

export default StockSearch;