import React, {Component} from 'react';

import Aux from '../../../hoc/Auxillary';

import classes from './Person.css';

class Person extends Component {

    render(){

        console.log('[Person.js] rendering');
        return (
        
        <Aux>
            {/*I'm a person
            <p>I am {Math.floor(Math.random()*30)} years old</p>
            <h1>Dynamic Content</h1>*/}
            <p onClick={this.props.click}>I'm {this.props.name} and I'm {this.props.age} years old</p>
            <p>{this.props.children}</p>
            <input type="text" onChange={this.props.changed} value={this.props.name}/>
        </Aux>
    
    )

    }
    
};

export default Person;