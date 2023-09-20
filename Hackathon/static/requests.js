$(document).on('submit','#text-form',function(e){
    e.preventDefault();

    $.ajax({
      type:'POST',
      url:'/send',
      data:{
          username:$('#reciever-user').val(),
          message:$('#text-message-field').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(data){
      },
      error: function(data){
          //alert(data)
      }
    });
    document.getElementById('message').value = ''
  });