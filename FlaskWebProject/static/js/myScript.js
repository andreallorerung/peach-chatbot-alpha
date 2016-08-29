function myFunction() {
  var content = document.getElementById('type_here').value;
  //var prefix= "User: ";
  jQuery("#user_input").append('<br />' + 'User:' + content);

  var elem = document.getElementById('chatScroll');
  elem.scrollTop = elem.scrollHeight;
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
        jQuery("#user_input").append('<br />' + 'Bot: ' + msg).scrollTop(1000);
      //  updateScroll();
        //alert(JSON.parse(reply.responseText).NLPtext);
      //  console.log(reply);
    },
    error: function(jqXHR, textStatus, errorThrown){
      console.log(errorThrown);
    }
});
}



function updateScroll(){
    var element = document.getElementById("w3-card");
    element.scrollTop = element.scrollHeight;
}

function SearchFunction() {
  var searchEntry = document.getElementById('searchBox').value;
  //var prefix= "User: ";
  //jQuery("#user_input").append('<br />' + 'User:' + content);

//  document.getElementById("user_input").append =  prefix + content;
//  var json = {"textForPython": content};
  //console.log(JSON.stringify(json));
  document.getElementById("searchBox").value = "";
    $.ajax({
      url:'/api/chatBot/search',
      data: searchEntry, //JSON.stringify(json),
      type:'POST',
      //dataType: 'application/json',
      //dataType: 'script',
      success: function(returnDict) {
        console.log('success');
      //  console.log('success');
      //  alert(msg);
      jQuery("#user_input").append('<br />' + 'Search results for ' + searchEntry + ': ' + returnDict);
        //alert(JSON.parse(reply.responseText).NLPtext);
      //  console.log(reply);
    },
    error: function(jqXHR, textStatus, errorThrown){
      console.log(errorThrown);
    }
});
}
// source: https://www.developphp.com/video/JavaScript/Custom-Confirm-Box-Programming-Tutorial
function CustomAlert(){
    this.render = function(dialog){
        var winW = window.innerWidth;
        var winH = window.innerHeight;
        var dialogoverlay = document.getElementById('dialogoverlay');
        var dialogbox = document.getElementById('dialogbox');
        dialogoverlay.style.display = "block";
        dialogoverlay.style.height = winH+"px";
        dialogbox.style.left = (winW/2) - (550 * .5)+"px";
        dialogbox.style.top = "100px";
        dialogbox.style.display = "block";
        document.getElementById('dialogboxhead').innerHTML = "Error Message";
        document.getElementById('dialogboxbody').innerHTML = dialog;
        document.getElementById('dialogboxfoot').innerHTML = '<button onclick="Alert.ok()">OK</button>';
    }
	this.ok = function(){
		document.getElementById('dialogbox').style.display = "none";
		document.getElementById('dialogoverlay').style.display = "none";
	}
}
var Alert = new CustomAlert();








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
