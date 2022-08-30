import React,{useState, useEffect} from 'react';
import UserList from '../components/UserList';
import {showUsers, showUser, showUserBuySellActions, showUserCallPutOptions} from "../services/UserService";

function HomeContainer() {
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

  return (
<div>
  <UserList users={users} viewOnly={viewOnly} selectedUserId={selectedUserId} setSelectedUserId={setSelectedUserId} selectedUserBuySellActions={selectedUserBuySellActions} callputOptions={selectedUserCallPutOptions}/>
</div>
  );
}
// setSelectedUser={setSelectedUser} selectedUser={selectedUser}
export default HomeContainer;
