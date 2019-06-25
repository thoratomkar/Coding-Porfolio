import React from 'react';
import './Person.css';

const person = (props) => {

    return (
    
    <div className='Person'>
        {/*I'm a person
        <p>I am {Math.floor(Math.random()*30)} years old</p>
        <h1>Dynamic Content</h1>*/}
        <p onClick={props.click}>I'm {props.name} and I'm {props.age} years old</p>
        <p>{props.children}</p>
        <input type="text" onChange={props.changed} value={props.name}/>
    </div>
    
    )
};

export default person;