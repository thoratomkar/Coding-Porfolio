import React from 'react'

const validation = (props) =>{

    let msg = 'text too short';

    if(props.text>=5){
        msg = 'text too long'
    }

    return(
    <div>
        <p>{msg}</p>
    </div>
    );
}

export default validation;