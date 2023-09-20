$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type: 'GET',
            url : "/getMessages",
            success: function(response){
                //alert(response.message)
                $("#msg-area").empty();
                for (var key in response.messages)
                {
                    //let textToShow = "<div class='container'><b>"+response.messages[key].sender+"</b><p>"+response.messages[key].messageText+"</p></div>"
                    let textToShow = "<li> " + response.messages[key].sender +  " to "  + response.messages[key].reciever +" : " + response.messages[key].messageText+" </li><br>"
                    $("#msg-area").append(textToShow);
                }
            },
            error: function(response){
            }
        });
    },1000);
    })