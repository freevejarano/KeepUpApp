window.onload = function() {
  if(document.title=="Keep Up"){
    var offer = document.getElementById("offer");
    if(typeof offer.value == "undefined"){
      offer.innerHTML += "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR09guhYQlcWXypvKIMNi5YvWX3HmtSVjsKSQ&usqp=CAU' width='300' height='300'/>"
    }
  }
};