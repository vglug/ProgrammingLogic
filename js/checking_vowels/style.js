$(document).ready(function(){
    $('#submit').on('click', function(){
    var user_input = $('#input_letter').val();
    var vowels = ['a','e','i','o','u','A','E','I','O','U'];
    if (vowels.includes(user_input)){
        $('.result').html("Yes");
        console.log("Yes");
    } else {
        $('.result').html("No");
        console.log("No");
        }
    });
});

