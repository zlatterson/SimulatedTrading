import React,{useState, useEffect} from 'react';
import UserList from '../components/UserList';
import {showUsers, showUser, showUserBuySellActions} from "../services/UserService";

function HomeContainer() {
  const [isLoaded, setIsLoaded] = useState(false)
  const [users, setUsers] = useState([])
  // const [user, setUser] = useState([])

  const [selectedUserId,setSelectedUserId] = useState(null)
  const [selectedUser, setSelectedUser] = useState(null)

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
  setSelectedUser(result)
  })
}, [selectedUserId]);

  return (
<div>
  {users.Modules}
  <UserList users={users} setSelectedUserId={setSelectedUserId}/>
</div>
  );
}
// setSelectedUser={setSelectedUser} selectedUser={selectedUser}
export default HomeContainer;
