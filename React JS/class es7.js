class Human{
 
    gender = 'Male';
  
  
  const printGender = () =>{
    console.log(this.gender);
  }
}

class Person extends Human{
  
  
    name = "Max";
    gender = "Female"
  
  
  const printMyName = () =>{
    console.log(this.name);
  }
}

const person = new Person();
person.printMyName();
person.printGender();