// When the window loads run the function
window.onload = function() {
  if(document.title=="Keep Up"){ // To index.html
    var offer = document.getElementById("offer");
    if(offer.innerText == ""){ // If there is no news show the info
      offer.innerHTML += "<br><h1>No Hay Noticias</h1><br>"
      offer.innerHTML += "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR09guhYQlcWXypvKIMNi5YvWX3HmtSVjsKSQ&usqp=CAU' width='300' height='300'/>";
    }
  }else if(document.title=="Keep Up - Editar"){
    // When the window just loads the info but doesn´t edit it, fix a html problem
      var title = document.getElementsByName("title")[0];
      title.value=document.getElementById("prov").innerText;
      var desc = document.getElementsByName("description")[0];
      desc.value=document.getElementById("prov2").innerText;
  }
};