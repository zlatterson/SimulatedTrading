import React from 'react';

const Profile = ({currentUser}) => {

    return (
        <div>
        {currentUser !== null ? 
            <div>
                <h5>{currentUser.username} Settled Cash: ${currentUser.money}</h5>
            </div>
        : <></>}
        </div>
    );
}

export default Profile;