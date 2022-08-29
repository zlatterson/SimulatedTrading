import React from 'react';

const StockSearch = ({setSearchedTicker, searchedTicker, searchInput, setSearchInput}) => {
    const handleSearchInput = (e) => {
        setSearchInput(e.target.value)
      }
      const newSubmit = (e) => {
        e.preventDefault();
        setSearchedTicker(searchInput)
      }
  return (
    <form onSubmit={newSubmit}>
    {/* <label htmlFor="new-item">Search for a term:</label> */}
    <input id="new-item" type="text" onChange={handleSearchInput} placeholder="Search term (Case-sensitive)..."></input>
    <input type="submit" value="Search" />
  </form>
  );
}

export default StockSearch;