$(document).ready(function(){
    // Navbar
    $('.sidenav').sidenav();
    // Dropdown
    $('select').formSelect();
  });


var ing_i = 1;
var step_i = 1;

$("#add_ingr").click(function(){
  var newInput = $(document.createElement('input'))
   .attr({
       id: 'ingr'+ing_i,
       name: 'ingr',
       type: "text",
       "class": "validate ingr"
   });
  $("#ingredients").append(newInput);
  ing_i++;
});

$("#add_step").click(function(){
  var newInput = $(document.createElement('input'))
   .attr({
       id: 'step'+step_i,
       name: 'step',
       type: "text",
       "class": "validate"
   });
  $("#steps").append(newInput);
  step_i++
});
