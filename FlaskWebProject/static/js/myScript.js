function myFunction() {
  var content = document.getElementById('type_here').value;
  //var prefix= "User: ";
  jQuery("#user_input").append('<br />' + 'User:' + content);
//  document.getElementById("user_input").append =  prefix + content;
  var json = {"textForPython": content};
  //console.log(JSON.stringify(json));
  document.getElementById("type_here").value = "";
    $.ajax({
      url:'/api/chatBot/chat',
      data: content, //JSON.stringify(json),
      type:'POST',
      //dataType: 'application/json',
      dataType: 'script',
      success: function(msg) {
        console.log('success');
      //  console.log('success');
      //  alert(msg);
        jQuery("#user_input").append('<br />' + 'Bot: ' + msg);
        //alert(JSON.parse(reply.responseText).NLPtext);
      //  console.log(reply);
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
