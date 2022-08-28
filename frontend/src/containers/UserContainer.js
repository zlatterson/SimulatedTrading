import React,{ useState, useEffect } from "react";
import {all_users} from '../services/UserService'

function UserContainer() {
    const [username, setUsername] = useState("");
    const [name, setName] = useState("");
    const [moneyPaidIn, setMoneyPaidIn] = useState("");

    const [allUsers, setAllUsers] = useState[[]]

    useEffect(()=>{
      all_users().then((result)=>{
        setAllUsers(result)
      })
  }, []);

  return (
    <>
    users: {allUsers}
    </>
  );
}

export default UserContainer;