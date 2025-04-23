function check(){
    if(confirm("Are you sure?")){
        alert("Ayt bet!")
        img = document.querySelector("img");
        img.remove();
}else{
    alert("oh okay cool")
}  
}