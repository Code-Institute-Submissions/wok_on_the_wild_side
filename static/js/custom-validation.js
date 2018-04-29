$(document).ready(function(){

    $.validator.setDefaults({
       ignore: []
    });
    $('#photo').on('change', function() { // fires every time this field changes
            $(this).valid();                  // force a validation test on this field
        });
    
    $("#contribute-form").validate({
        rules: {
            dish_name: {
                required: true,
                minlength: 5,
                maxlength: 50
            },
            descr: {
                required: true,
                minlength: 5,
                maxlength: 350
            },
            c_time: {
        		required: true,
        		min: 5,
        		max: 180
        	},
        	serves: {
        		required: true
        	},
        	cuisine: {
                required: true
            },
            author:{
                required: true,
                minlength: 3,
                maxlength: 50
            },
            photo: {
        		required: true,
        		extension: "jpg|png"
            },
            ingr:{
                required: true,
                minlength: 5,
                maxlength: 100
            },
        	step:{
                required: true,
                minlength: 5,
                maxlength: 350
            }
        },
        //For custom messages
        messages: {
             dish_name: {
                required: "Enter a name for your dish",
                minlength: "Enter at least 5 characters",
                maxlength: "Max length exceeded"
            },
            descr:{
                required: "This is required",
                minlength: "Enter at least 5 characters",
                maxlength: "Max length exceeded"                
            },
            c_time:{
                required: "This is required",
                min: "Miniumum time allowed is 5 minutes",
                maxs: "Maximum time allowed is 180 minutes"                 
            },
            serves:{
                required: "Please select an option"
            },
        	cuisine: {
                required: "Please select an option"
            },
            author:{
                required: "This is required",
                minlength: "Enter at least 3 characters",
                maxlength: "Max length exceeded"
            },
            photo: {
        		required: "This is required",
        		extension: "Incorrect file format, this needs to be JPG or PNG"
            },
            ingr:{
                required: "This is required",
                minlength: "Enter at least 5 characters",
                maxlength: "Max length exceeded"
            },
        	step:{
                required: "This is required",
                minlength: "Enter at least 5 characters",
                maxlength: "Max length exceeded"
            }
        },
        errorClass: "invalid form-error",
        errorElement : 'div',
        errorPlacement: function(error, element) {
            error.appendTo( element.parent() );
        },
        onfocusout: false,
        onkeyup: false,
        focusCleanup: true
    });
    $("#update-form").validate({
        rules: {
            dish_name: {
                required: true,
                minlength: 5,
                maxlength: 50
            },
            descr: {
                required: true,
                minlength: 5,
                maxlength: 350
            },
            c_time: {
        		required: true,
        		min: 5,
        		max: 180
        	},
            author:{
                required: true,
                minlength: 3,
                maxlength: 50
            },
            ingr:{
                required: true,
                minlength: 5,
                maxlength: 100
            },
        	step:{
                required: true,
                minlength: 5,
                maxlength: 350
            }
        },
        //For custom messages
        messages: {
             dish_name: {
                required: "Enter a name for your dish",
                minlength: "Enter at least 5 characters",
                maxlength: "Max length exceeded"
            },
            descr:{
                required: "This is required",
                minlength: "Enter at least 5 characters",
                maxlength: "Max length exceeded"                
            },
            c_time:{
                required: "This is required",
                min: "Miniumum time allowed is 5 minutes",
                maxs: "Maximum time allowed is 180 minutes"                 
            },
            author:{
                required: "This is required",
                minlength: "Enter at least 3 characters",
                maxlength: "Max length exceeded"
            },
            ingr:{
                required: "This is required",
                minlength: "Enter at least 5 characters",
                maxlength: "Max length exceeded"
            },
        	step:{
                required: "This is required",
                minlength: "Enter at least 5 characters",
                maxlength: "Max length exceeded"
            }
        },
        errorClass: "invalid form-error",
        errorElement : 'div',
        errorPlacement: function(error, element) {
            error.appendTo( element.parent() );
        },
        onfocusout: false,
        onkeyup: false,
        focusCleanup: true
    });
    $("#photo-form").validate({
        rules: {
            photo: {
        		required: true,
        		extension: "jpg|png"
            }
        },
        //For custom messages
        messages: {
            photo: {
        		required: "This is required",
        		extension: "Incorrect file format, this needs to be JPG or PNG"
            }
        },
        errorClass: "invalid form-error",
        errorElement : 'div',
        errorPlacement: function(error, element) {
            error.appendTo( element.parent() );
        },
        onfocusout: false,
        onkeyup: false,
        focusCleanup: true
    });
});


