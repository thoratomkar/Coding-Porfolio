import React, { Component } from 'react';
import './App.css';
import Person from './Person/Person';

class App extends Component{

  state = {
    persons: [
      { name: 'Omkar', age: 24},
      { name: 'Ketan', age: 23}
    ]
  };

  switchNameHandler = (newName) =>{

    this.setState  ( {
      persons: [
        { name: newName, age: 24},
      { name: 'Ketan Mudur', age: 23}
      ]
    });
  };

  
  onChangedHandler = (event) =>{

    this.setState  ( {
      persons: [
        { name: 'Omkar Thorat', age: 24},
      { name: event.target.value, age: 23}
      ]
    });
  };

  render(){

    const style = {
      backgroundColor : 'white',
      font : 'inherit',
      border: '1px solid blue',
      padding: '8px',
      cursor: 'pointer'
    }

    return (
      <div className="App">
        <h1>Hi, I'm a React App </h1>
        <button onClick={this.switchNameHandler.bind(this,'Omkar Thorat')}
         style={style}>Switch Name</button>
        <Person name={this.state.persons[0].name} 
        age={this.state.persons[0].age}
        />
        <Person name={this.state.persons[1].name}
        age={this.state.persons[1].age}
        click={this.switchNameHandler.bind(this, 'Omkar Sunil Thorat')}
        changed={this.onChangedHandler}>Hobbies: watching football
        </Person>
      </div>
    );
  }
  
}

export default App;
