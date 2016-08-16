function myFunction() {
  var typeHereText = document.getElementById('type_here').value;
  var prefix= "User: ";
  document.getElementById("user_input").innerHTML =  prefix + typeHereText;
  var json = {"textForPython": typeHereText};
  //console.log(JSON.stringify(json));
  document.getElementById("type_here").value = "";
    $.ajax({
      url:'/api/chatBot/chat',
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









function addSelect(){
$('#checkbox').change(function() {
  if ($(this).is(':checked')) {
    alert('Checked');
  } else {
    console.log('Unchecked');
  }
});
}

//function addSelect(){
  //if(document.getElementById('breathing').checked) {
    //  alert("checked");
//  } else {
  //    alert("not checked");
//  }
//}
