import React,{useState, useEffect} from 'react';
import BuySellList from '../components/BuySellList';
import StockSearch from '../components/StockSearch';
import UserList from '../components/UserList';
import {showUserBuySellActions} from "../services/UserService";
import {searchStockByTicker} from "../services/StockService";

function Dashboard() {
    const [isLoaded, setIsLoaded] = useState(false)

    const [currentUser, setCurrentUser] = useState(1)
    const [buySellActions, setBuySellActions] = useState([])

    const [searchInput, setSearchInput] = useState(null)
    const [searchedTicker, setSearchedTicker] = useState(null)
    const [foundStock, setFoundStock] = useState(null)

    useEffect(()=>{
        setIsLoaded(true)
    }, []);

    // Show user buy sell actions
    useEffect(()=>{
        if(!isLoaded){
    return
    }
    showUserBuySellActions(currentUser).then((result)=>{
        setBuySellActions(result)
    })
    }, [isLoaded]);

    // Search Ticker
    useEffect(()=>{
        if(!isLoaded){
    return
    }
    searchStockByTicker(searchedTicker).then((result)=>{
        setFoundStock(result)
    })
    }, [searchedTicker]);

    return (
    <div>
        <StockSearch searchInput={searchInput} setSearchInput={setSearchInput} setSearchedTicker={setSearchedTicker} searchedTicker={searchedTicker}/>
        <BuySellList selectedUserBuySellActions={buySellActions}/>
    </div>
    );
    }
export default Dashboard;
