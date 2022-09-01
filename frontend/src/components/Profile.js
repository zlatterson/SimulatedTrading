import React from 'react';

const Profile = ({currentUser}) => {

    return (
        <div>
        {currentUser !== null ? 
            <div>
                <p>{currentUser.username}<br></br>Starting Cash: ${currentUser.money_paid_in.toFixed(2)}<br></br>Settled Cash: ${currentUser.money.toFixed(2)}</p>
            </div>
        : <></>}
        </div>
    );
}

export default Profile;