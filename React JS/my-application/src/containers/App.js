import React, { Component } from 'react';
import classes from './App.css';

import Persons from '../components/Persons/Persons';

import Cockpit from '../components/Cockpit/Cockpit';
import WithClass from '../hoc/WithClass';
class App extends Component{

  constructor(props){
    super(props)
    console.log('[App.js] Constructor');
  }

  state = {
    persons: [
      { id: '1', name: 'Omkar', age: 24},
      { id: '2', name: 'Ketan', age: 23},
      {id: '3', name: 'Niraj', age: 23}
    ],
    showPersons: false,
    showCockpit: true
  };

  static getDerivedStateFromProps(props,state){
    console.log('[App.js] getDerivedStateFromProps',props)

    return state;
  }

  componentDidMount(){
    console.log('[App.js] componentDidMount');
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log('[App.js] shouldComponentUpdate');
    return true;
  }

  componentDidUpdate() {
    console.log('[App.js] componentDidUpdate');
  }

  switchNameHandler = (newName) =>{

    this.setState  ( {
      persons: [
        { name: newName, age: 24},
      { name: 'Ketan Mudur', age: 23}
      ]
    });
  };

  
  nameChangedHandler = ( event, id ) => {
    const personIndex = this.state.persons.findIndex(p => {
      return p.id === id;
    });

    const person = {
      ...this.state.persons[personIndex]
    };

    // const person = Object.assign({}, this.state.persons[personIndex]);

    person.name = event.target.value;

    const persons = [...this.state.persons];
    persons[personIndex] = person;

    this.setState( {persons: persons} );
  }

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
    console.log('[App.js] render')
    let person = null;
    
    

    if(this.state.showPersons){
      
      
      person = 
          <Persons
            persons = {this.state.persons}
            clicked = {this.deletePersonHandler}
            changed = {this.nameChangedHandler} />;         
      

    }

    return (
      
      <WithClass classes={classes.App}>
        <button
          onClick={() => {
            this.setState({ showCockpit: false });
          }}
        >
          Remove Cockpit
        </button>
        {this.state.showCockpit ?(<Cockpit 
         showPersons = {this.state.showPersons}
         personslength = {this.state.persons.length}
         clicked = {this.toggleNameHandler}
         />
         ):null}
        { person }
      </WithClass>
      
    );
  }
  
}

export default App;
