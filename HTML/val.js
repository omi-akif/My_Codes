var attempt = 4;
function validate(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if(username == "Afia" && password == "afia"){
        alert("You just found me");
        return false;
    }
    else{
        attept--;
        alert("You have left "+attempt+ "attempt");

        if(attempt == 0){
            document.getElementById("username").disabled = true;
            document.getElementById("password").disabled = true;
            document.getElementById("submit").disabled = true;
        return false;
        }
    }
}