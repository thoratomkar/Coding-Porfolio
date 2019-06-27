import React, { Component } from 'react';
import './App.css';
import Radium,{StyleRoot} from 'radium';
import Person from './Person/Person';

class App extends Component{

  state = {
    persons: [
      { id: '1', name: 'Omkar', age: 24},
      { id: '2', name: 'Ketan', age: 23},
      {id: '3', name: 'Niraj', age: 23}
    ],
    showPersons: false
  };

  switchNameHandler = (newName) =>{

    this.setState  ( {
      persons: [
        { name: newName, age: 24},
      { name: 'Ketan Mudur', age: 23}
      ]
    });
  };

  
  onChangedHandler = (event, personID) =>{

    const personIndex = this.state.persons.find((p) => {
      return p.id === personID;
    });

    

    const person = {...this.state.persons[personIndex]};
    person.name = event.target.value;

    const persons = [...this.state.persons];
    persons[personIndex] = person

    this.setState  ( {
      persons: persons 
    });
  };

  toggleNameHandler = () =>{
    
      const doesShow = this.state.showPersons;
      this.setState({
        showPersons : !doesShow });
    
  }

  deletePersonHandler = (PersonIndex) =>{
    //const person = this.state.persons.slice;
    const person = [...this.state.persons];
    person.splice(PersonIndex, 1);
    this.setState({persons:person});
  }

  render(){

    const style = {
      backgroundColor : 'green',
      font : 'white',
      border: '1px solid blue',
      padding: '8px',
      cursor: 'pointer',
      ':hover':{
        backgroundColor : 'lightgreen',
        color : 'black'
      }
    }

    let person = null;
    const classes = [];
    if (this.state.persons.length <=2){
      classes.push('red')
    }

    if (this.state.persons.length <=1){
      classes.push('bold')
    }

    if(this.state.showPersons){
      style.backgroundColor = 'red';
      style[':hover'] = {
        backgroundColor : 'pink',
        color : 'red'
      }
      person = (
        <div>

          {
            this.state.persons.map((person, PersonIndex) =>{
              return <Person 
              click = {() =>this.deletePersonHandler(PersonIndex)}
              name={person.name} 
              age={person.age}
              key={person.id}
              changed = {(event) => this.onChangedHandler(event,person.id)}/>
            })
          }

        </div>
      );
      

    }

    return (
      <StyleRoot>
        <div className="App">
          <h1>Hi, I'm a React App </h1>
          <p className ={classes.join(' ')}>My Friends </p>
          <button onClick={this.toggleNameHandler}
          style={style}>Toggle Names</button>
          { person
          }
        </div>
      </StyleRoot>
    );
  }
  
}

export default Radium(App);
