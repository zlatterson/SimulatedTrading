import React,{useState, useEffect} from 'react';
import UserList from '../components/UserList';
import {showUsers, showUser, showUserBuySellActions} from "../services/UserService";

function HomeContainer() {
  const [isLoaded, setIsLoaded] = useState(false)
  const [users, setUsers] = useState([])

  const [selectedUserId,setSelectedUserId] = useState(null)
  const [selectedUserBuySellActions, setSelectedUserBuySellActions] = useState(null)

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
  // TODO: Add another.then() to find the running pl percentage of each user
}, [selectedUserId]);

  return (
<div>
  {users.Modules}
  <UserList users={users} selectedUserId={selectedUserId} setSelectedUserId={setSelectedUserId} selectedUserBuySellActions={selectedUserBuySellActions}/>
</div>
  );
}
// setSelectedUser={setSelectedUser} selectedUser={selectedUser}
export default HomeContainer;
