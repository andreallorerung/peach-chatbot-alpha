function myFunction() {
  var content = document.getElementById('type_here').value;
  content.fontcolor("blue");
  //var prefix= "User: ";
  jQuery("#user_input").append('<b>User: </b>' + content);

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
        jQuery("#user_input").append('<br />' + '<b>Bot: </b>' + msg + '</br />');
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

  document.getElementById("searchBox").value = "";
    $.ajax({
      url:'/api/chatBot/search',
      data: searchEntry,
      type:'POST',
     dataType: 'json',
      //dataType: 'text',
      success: function(results) {
        console.log('success')
        //error message if no search results were found
    if (results == 'no results found'){
     jQuery("#search_input").append('There were no search results found for ' + '"'+searchEntry + '"'+ '. Please try a different search field.');
    }else{
      //otherwise create hyperlink from each element in the array
    jQuery("#search_input").append('Your Search Results for '+ '"'+ searchEntry + '"'+  ':').append(results.map(function(link){return '<li><a href="'+link+'">'+link+'</a></li>';}));

    }
    },
    error: function(jqXHR, textStatus, errorThrown){
      console.log(errorThrown);
    }
});
}

function clearSearch(){
    document.getElementById("search_input").innerHTML= "";
}

function chatHelp(){
  Alert.render("The ChatBot can talk to you about any of your concerns from the previous page.First tell the bot what topic you want to discuss by setting the topic - like 'set practical' or 'set family'. Then you can begin, try saying 'I want to talk about my friend.' or 'I want to talk about work'.");

}
function noConsent(){
  Alert.render("Please be assured your treatment will not be affected if you choose not to continue. \n Other options are available which your GP or nurse will be able to tell you about.");
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
        document.getElementById('dialogboxhead').innerHTML = "Information Message";
        document.getElementById('dialogboxbody').innerHTML = dialog;
        document.getElementById('dialogboxfoot').innerHTML = '<button onclick="Alert.ok()">OK</button>';
    }
	this.ok = function(){
		document.getElementById('dialogbox').style.display = "none";
		document.getElementById('dialogoverlay').style.display = "none";
	}
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
