import React from 'react';

const UserItem = ({user,setSelectedUserId}) => {
    const handleClick = () => {
        setSelectedUserId(user.id)
    }

    return (
    <li>
        <h3 onClick={handleClick}>@{user.username} {user.name} ${user.money}</h3>
        {/* {user.name} */}
    </li>
    );
}

export default UserItem;