/*-----------------------------------
#ALL SCRIPTS HERE WILL EXTEND TO OTHER PAGES
---------------------------------------------*/


// 1) Character remaining counter

$(document).ready(function() {
    var start = 0;
    var limit = 1000;

    $("#message").keyup(function(){
        start = this.value.length
        if(start > limit) {
            return false;
        }
        else if (start ==1000) {
            $("#remaining").html("Characters remaining: "+ (limit - start)).css('color', 'red');
            swal("Oops !" , "Characters limit exceeded!", "info");
        }
        else if (start > 984) {
            $("#remaining").html("Characters remaining: "+ (limit - start)).css('color', 'red');
        }
        else if (start < 1000) {
            $("#remaining").html("Characters remaining: "+ (limit - start)).css('color', 'black');
        }
        else {
            $("#remaining").html("Characters remaining: "+ (limit - start)).css('color', 'red');
        }
    })

})
// 2) Inputmask (PHONE)
$(document).ready(function(){
    $(".phone").inputmask("(99) 999-999", {"onincomplete": function() {
        swal("Oops!" , "Incomplete phone. Please review !" , "info");
        $(".phone").val(""); /*#prevent vulnerability by deleting input*/
        return false;
    }})


})



