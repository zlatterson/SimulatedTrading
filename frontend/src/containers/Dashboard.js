import React,{useState, useEffect} from 'react';
import BuySellList from '../components/BuySellList';
import StockSearch from '../components/StockSearch';
import {showUserBuySellActions, showUser, showUserCallPutOptions} from "../services/UserService";
import {searchStockByTicker} from "../services/StockService";
import {postBuySellAction} from "../services/BuySellActionService";
import {showOptions,showOption, postCallPutOption, exerciseCallPutOption} from "../services/CallPutOptionService";
import Stock from '../components/Stock';
import Profile from '../components/Profile';
import CallPutList from '../components/CallPutList';
import { Container, Col, Row, Tab, Nav } from 'react-bootstrap';
import colorSharp2 from "../assets/img/color-sharp2.png";



function Dashboard() {
    const [isLoaded, setIsLoaded] = useState(false)

    const [currentUserId, setCurrentUserId] = useState(1)
    const [currentUser, setCurrentUser] = useState(null)
    const [buySellActions, setBuySellActions] = useState([])

    const [searchInput, setSearchInput] = useState(null)
    const [searchedTicker, setSearchedTicker] = useState(null)
    const [foundStock, setFoundStock] = useState(null)

    const [orderTypeBuySell, setOrderTypeBuySell] = useState(false)
    const [quantityInput, setQuantityInput] = useState(null)

    const [sentBuySellOrder, setSentBuySellOrder] = useState(null)
    // call put
    const [orderTypeCallPut, setOrderTypeCallPut] = useState(false)
    const [options, setOptions] = useState([])
    const [selectedOption, setSelectedOption]  = useState(null)
    const [option, setOption] = useState(null)
    const [optionQuantityInput, setOptionQuantityInput] = useState(null)
    const [sentOptionOrder, setSentOptionOrder] = useState(null)
    // 
    // SELL order for buy sell
    const [sellQuantityInput, setSellQuantityInput] = useState(null)
    const [sentSellOrder, setSentSellOrder] = useState(null)
    // Get user buy sell actions
    const [callputOptions, setCallPutOptions] = useState([])
    const [exerciseOrder, setExerciseOrder] = useState(null)

    const [runnningTotal, setRunningTotal] = useState(0)
useEffect(()=>{
        setIsLoaded(true)
    }, []);

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
    // place buy sell order **TODO RES
useEffect(()=>{
    if(!isLoaded){
        return
    }
    postBuySellAction(sentBuySellOrder)
    }, [sentBuySellOrder]);
    // callput
useEffect(()=>{
    if(!isLoaded){
        return
    }
    showOptions(searchedTicker).then((result)=>{
        setOptions(result)
    })
    }, [orderTypeCallPut]);

useEffect(()=>{
    if(!isLoaded){
        return
    }
    if(sentOptionOrder == null){
        return
    }
    postCallPutOption(sentOptionOrder)
    }, [sentOptionOrder]);

useEffect(()=>{
    if(!isLoaded){
        return
    }
    if(selectedOption == null){
        return
    }
    showOption(selectedOption).then((result)=>{
        setOption(result)
    })
    }, [selectedOption]);    
// SELL buy sell actions
useEffect(()=>{
    if(!isLoaded){
        return
    }
    if(sentSellOrder == null){
        return
    }
    postBuySellAction(sentSellOrder).then(() => {
        setSentSellOrder(null)
    })
    }, [sentSellOrder]);
// EXERCISE call put order
useEffect(()=>{
    if(!isLoaded){
        return
    }
    if(exerciseOrder == null){
        return
    }
    exerciseCallPutOption(exerciseOrder).then(() => {
        setExerciseOrder(null)
    })
    }, [exerciseOrder]);
// Refresh service
    const MINUTE_MS = 12000;

    useEffect(() => {
    const interval = setInterval(() => {
        console.log("refreshed")
        showUser(currentUserId).then((result)=>{
            setCurrentUser(result)
        })
        showUserBuySellActions(currentUserId).then((result)=>{
            setBuySellActions(result)
        })
        showUserCallPutOptions(currentUserId).then((result)=>{
            setCallPutOptions(result)
        })
    }, MINUTE_MS);

    return () => clearInterval(interval); // This represents the unmount function, in which you need to clear your interval to prevent memory leaks.
    }, [])

    return (
        <div>
                <section className="project" id="dashboard">
      <Container>
        <Row>
        <Col size={12}>
                <h2>Dashboard</h2>
                <p>Here you can make trades.</p>
                <Profile 
                currentUser={currentUser}
                />
                <StockSearch 
                searchInput={searchInput} 
                setSearchInput={setSearchInput} 
                setSearchedTicker={setSearchedTicker}
                />
          </Col>
        </Row>
      </Container>
      <img className="background-image-right" src={colorSharp2}></img>
    </section>
        <section section className="dashboard" id="dashboard">
            <Container>
            <Stock 
                foundStock={foundStock} 
                user = {currentUser} 
                orderTypeBuySell={orderTypeBuySell} 
                setOrderTypeBuySell={setOrderTypeBuySell} 
                orderTypeCallPut={orderTypeCallPut} 
                setOrderTypeCallPut={setOrderTypeCallPut} 
                setQuantityInput = {setQuantityInput} 
                quantityInput={quantityInput} 
                setSentBuySellOrder={setSentBuySellOrder} 
                options={options} 
                selectedOption={selectedOption} 
                setSelectedOption={setSelectedOption} 
                option={option} 
                optionQuantityInput={optionQuantityInput} 
                setOptionQuantityInput={setOptionQuantityInput} 
                setSentOptionOrder={setSentOptionOrder}
            />
            <BuySellList selectedUserBuySellActions={buySellActions} 
                sellQuantityInput={sellQuantityInput} 
                setSellQuantityInput={setSellQuantityInput} 
                setSentSellOrder={setSentSellOrder} 
                user={currentUser}
                runnningTotal={runnningTotal}
                setRunningTotal={setRunningTotal}
            />
            <CallPutList 
                callputOptions={callputOptions} 
                setExerciseOrder={setExerciseOrder}
            />
        </Container>
     </section>
    </div>
    );
    }
export default Dashboard;
