
    window.onload = function() {
    var today = new Date().toISOString().split('T')[0];
    document.getElementById('date').setAttribute('min', today);
     };
    function validate(){
    
      let age = parseInt(document.getElementById('age').value);
      let number = document.getElementById('mbno').value.trim();

      
      if (age < 0) {
          alert("Age must be a non-negative number.");
          return false;
      }
      
      if (number.length !== 10 ) {
          alert("Mobile number must be a 10-digit number.");
          return false;
      }
      
      return true; // Return true if all validations pass
    }