import React from 'react';

const Profile = ({currentUser}) => {

    return (
        <div>
        {currentUser !== null ? 
            <div>
                <p>{currentUser.username}</p>
                <p>Starting Cash: ${currentUser.money_paid_in.toFixed(2)}</p>
                <p>Settled Cash: ${currentUser.money.toFixed(2)}</p>
            </div>
        : <></>}
        </div>
    );
}

export default Profile;