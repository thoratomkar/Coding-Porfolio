import React from 'react';

const userInput = (props) =>{

    const style = {
        
        font : 'inherit',
        border: '4px solid red',
        padding: '8px',
        cursor: 'pointer'
      }

    return (
        <div>
            <input type="text" onChange={props.changed} value={props.ogname}
            style={style}/>
        </div>
    );
}

export default userInput;