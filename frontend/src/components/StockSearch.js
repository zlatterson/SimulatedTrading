import React from 'react';
import { Container } from 'react-bootstrap';

const StockSearch = ({setSearchedTicker, searchInput, setSearchInput}) => {
    const handleSearchInput = (e) => {
        setSearchInput(e.target.value)
      }
      const newSubmit = (e) => {
        e.preventDefault();
        setSearchedTicker(searchInput)
      }
  return (
    <Container>
    <form onSubmit={newSubmit}>
    <input class="form-control py-2 rounded-pill mr-1 pr-5 nav-pills mb-5 justify-content-center align-items-center" type="text" onChange={handleSearchInput} placeholder="Search ticker or place order directly..."></input>
    <input type="submit" value="Search" class="btn btn-primary"/>
  </form>
  </Container>
  );
}

export default StockSearch;