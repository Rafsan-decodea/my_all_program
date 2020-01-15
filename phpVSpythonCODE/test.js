


$(document).ready(function(){
   $('#displaybtn').click(function(){
  
       $.ajax({
           method:"post",
           url:"test.php",
           data:$('#display_data').serialize(),
           datatype:"html",
           success: function(response)
           {
               $('#display_data').html(response);
           }
        
       })
   })
});