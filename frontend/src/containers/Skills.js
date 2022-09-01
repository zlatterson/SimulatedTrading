import meter1 from "../assets/img/meter1.svg";
import meter2 from "../assets/img/meter2.svg";
import meter3 from "../assets/img/meter3.svg";
import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';
import arrow1 from "../assets/img/arrow1.svg";
import arrow2 from "../assets/img/arrow2.svg";
import colorSharp from "../assets/img/color-sharp.png"
import React,{useState, useEffect} from 'react';
import UserList from '../components/UserList';
import {showUsers, showUser, showUserBuySellActions, showUserCallPutOptions} from "../services/UserService";

const Skills = ({}) => {
    const [isLoaded, setIsLoaded] = useState(false)
    const [users, setUsers] = useState([])
  
    const [selectedUserId,setSelectedUserId] = useState(null)
    const [selectedUserBuySellActions, setSelectedUserBuySellActions] = useState([])
    const [selectedUserCallPutOptions, setSelectedUserCallPutOptions] = useState([])
  
    const [viewOnly, setViewOnly] = useState(true)
  
    useEffect(()=>{
      showUsers().then((result)=>{
      setUsers(result)
      })
      setIsLoaded(true)
  }, []);
  
  useEffect(()=>{
    if(!isLoaded){
      return
    }
    showUserBuySellActions(selectedUserId).then((result)=>{
      setSelectedUserBuySellActions(result)
    })
    showUserCallPutOptions(selectedUserId).then((result)=>{
      setSelectedUserCallPutOptions(result)
  })
    // TODO: Add another.then() to find the running pl percentage of each user
  }, [selectedUserId]);
    const responsive = {
        superLargeDesktop: {
          // the naming can be any, depends on you.
          breakpoint: { max: 4000, min: 3000 },
          items: 5
        },
        desktop: {
          breakpoint: { max: 3000, min: 1024 },
          items: 3
        },
        tablet: {
          breakpoint: { max: 1024, min: 464 },
          items: 2
        },
        mobile: {
          breakpoint: { max: 464, min: 0 },
          items: 1
        }
      };


        return (
            <section className="skill" id="users">
                <div className="container">
                    <div className="row">
                        <div className="col-12">
                            <div className="skill-bx wow zoomIn">
                                <h2>Users</h2>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.<br></br> Lorem Ipsum has been the industry's standard dummy text.</p>
                                <Carousel responsive={responsive} infinite={true} className="owl-carousel owl-theme skill-slider">
                                <UserList users={users} viewOnly={viewOnly} selectedUserId={selectedUserId} setSelectedUserId={setSelectedUserId} selectedUserBuySellActions={selectedUserBuySellActions} callputOptions={selectedUserCallPutOptions}/>
                                </Carousel>
                            </div>
                        </div>
                    </div>
                </div>
                <img className="background-image-left" src={colorSharp} alt="Image" />
            </section>
      );
}

export default Skills;