import React, {useEffect} from 'react';
import classes from './Cockpit.css'
const cockpit = (props) =>{

    useEffect(() => {
        console.log('[Cockpit.js] useEffect');
        setTimeout(() =>{
            alert('Saved data to cloud!');
        }, 1000);
        return () => {
            console.log('[Cockpit.js] cleanup work in useEffect');
          };
    },[]);

    useEffect(() => {
        console.log('[Cockpit.js] 2nd useEffect');
        return () => {
          console.log('[Cockpit.js] cleanup work in 2nd useEffect');
        };
      });

    const classesAssigned = [];
    let btnClass = '';

    if(props.showPersons){
        btnClass = classes.Red;
    }
    
    if (props.personslength <=2){
      classesAssigned.push(classes.red)
    }

    if (props.personslength <=1){
      classesAssigned.push(classes.bold)
    }

    return (
        <div className ={classes.Cockpit}>
            <h1>Hi, I'm a React App </h1>
            
            <p className ={classesAssigned.join(' ')}>My Friends </p>
            
            <button
                className={btnClass}
                onClick={props.clicked}>Toggle Persons</button>
        </div>
    );
}

export default React.memo(cockpit);