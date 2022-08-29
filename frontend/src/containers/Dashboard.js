import React,{useState, useEffect} from 'react';
import BuySellList from '../components/BuySellList';
import StockSearch from '../components/StockSearch';
import UserList from '../components/UserList';
import {showUserBuySellActions, showUser} from "../services/UserService";
import {searchStockByTicker} from "../services/StockService";
import Stock from '../components/Stock';
import Profile from '../components/Profile';

function Dashboard() {
    const [isLoaded, setIsLoaded] = useState(false)

    const [currentUserId, setCurrentUserId] = useState(1)
    const [currentUser, setCurrentUser] = useState(null)
    const [buySellActions, setBuySellActions] = useState([])

    const [searchInput, setSearchInput] = useState(null)
    const [searchedTicker, setSearchedTicker] = useState(null)
    const [foundStock, setFoundStock] = useState(null)

    const [orderTypeBuySell, setOrderTypeBuySell] = useState(false)
    const [orderTypeCallPut, setOrderTypeCallPut] = useState(false)
    const [quantityInput, setQuantityInput] = useState(null)

    const [sentBuySellOrder, setSentBuySellOrder] = useState(null)

    useEffect(()=>{
        setIsLoaded(true)
    }, []);

    // Show user buy sell actions
    useEffect(()=>{
        if(!isLoaded){
    return
    }
    showUser(currentUserId).then((result)=>{
        setCurrentUser(result)
    })
    showUserBuySellActions(currentUserId).then((result)=>{
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

    // BUY/SELL ORDER
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
        <Profile currentUser={currentUser}/>
        <StockSearch searchInput={searchInput} setSearchInput={setSearchInput} setSearchedTicker={setSearchedTicker}/>
        <Stock foundStock={foundStock} user = {currentUser} orderTypeBuySell={orderTypeBuySell} setOrderTypeBuySell={setOrderTypeBuySell} orderTypeCallPut={orderTypeCallPut} setOrderTypeCallPut={setOrderTypeCallPut} setQuantityInput = {setQuantityInput} quantityInput={quantityInput} setSentBuySellOrder={setSentBuySellOrder}/>
        <BuySellList selectedUserBuySellActions={buySellActions}/>
    </div>
    );
    }
export default Dashboard;
