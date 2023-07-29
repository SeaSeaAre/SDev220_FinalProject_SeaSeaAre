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

// 3) Script to get date and time
setInterval(function() {
    var date = new Date();
    $('#clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ':' +
        (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ':' +
        (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
    }, 500);
    
// 4) Script to update the page always at (0:00) because django isn't dynamic
function autoRefresh(hours, minutes, seconds) {
    var now = new Date(), then = new Date();
    then.setHours(hours,minutes,seconds,0);
    if(then.getTime()-now.getTime()<=0) {
        then.setDate(now.getDate()+1);
    }
    var timeout = (then.getTime()-now.getTime());
    setTimeout(function() { window.location.reload(true); }, timeout);
}
autoRefresh(0,0,0);