$(document).ready(function(){
    // Navbar
    $('.sidenav').sidenav();
    // Dropdown
    $('select').formSelect();
  });

  
$("#add_ingr").click(function(){
  var newInput = $(document.createElement('input'))
   .attr({
       id: 'ingr',
       name: 'ingr',
       type: "text",
       "class": "validate"
   });
  $("#ingredients").append(newInput);
});


$("#add_step").click(function(){
  var newInput = $(document.createElement('input'))
   .attr({
       id: 'step',
       name: 'step',
       type: "text",
       "class": "validate"
   });
  $("#steps").append(newInput);
});