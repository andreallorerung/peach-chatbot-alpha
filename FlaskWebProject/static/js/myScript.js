
function myFunction() {
  var typeHereText = document.getElementById('type_here').value;
  var prefix= "User: ";
  document.getElementById("user_input").innerHTML =  prefix + typeHereText;
  var json = {"textForPython": typeHereText};
  //console.log(JSON.stringify(json));
  document.getElementById("type_here").value = "";
    $.ajax({
      url:'/api/chatBot',
      data: typeHereText, //JSON.stringify(json),
      type:'POST',
      //dataType: 'application/json',
      //contentType: 'application/json',
      success: function(reply) {
        jQuery("#user_input").append('<br />' + reply);
        //alert(JSON.parse(reply.responseText).NLPtext);
        console.log(reply);
    },
    error: function(jqXHR, textStatus, errorThrown){
      console.log(errorThrown);
    }
});
}
