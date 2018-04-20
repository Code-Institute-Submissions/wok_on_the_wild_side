$(document).ready(function(){
    // Navbar
    $('.sidenav').sidenav();
    // Dropdown
    $('select').formSelect();
  });


//var ing_i = 1;
//var step_i = 1;

$("#add_ingr").click(function(){
  var newInput = $(document.createElement('input'))
   .attr({
       //id: 'ingr'+ing_i,
       name: 'ingr',
       type: "text",
       "class": "validate ingr"
   });
  $("#ingredients").append(newInput);
  //ing_i++;
});

$('#remove_ingr').on('click', function () {
    if($('#ingredients input').length > 1)
    {
        $('#ingredients input:text:last').remove();
    }
});

$("#add_step").click(function(){
  var newInput = $(document.createElement('textarea'))
   .attr({
       //id: 'step'+step_i,
       name: 'step',
       type: "text",
       "class": "materialize-textarea validate"
   });
  $("#steps").append(newInput);
  //step_i++;
});

$('#remove_step').on('click', function () {
    if($('#steps input').length > 1)
    {
        $('#steps input:text:last').remove();
    }
});

