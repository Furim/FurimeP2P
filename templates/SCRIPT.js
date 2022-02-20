
function getDucos(){
    document.getElementById("getDucosButton").disabled = true; 
    var ducoUsername = document.getElementById("ducoUsername").value; 
    document.getElementById("spinner").innerHTML = '<div class="loader"></div>';
    var responseCode;
    
    fetch('/chatroom?ducoUsername='+ducoUsername, {
        method: 'POST'
    })

    
    .then(function(response) {
        if((response.status == 500) || (response.status == 502)){
        alert("There was a server error, please try again");

            // alert("You already claimed DUCO's in this hour!");
        } else if(response.status == 200){
            responseCode = response.status
            console.log('😎');
            return response.json()

           
        }

    }).then(function(object) {
        if(responseCode == 200){
            document.getElementById("spinner").innerHTML = '<p>Invite code:'+object.chat_read+'<p>';
            console.log(object.duinoResponse);
        } 
        document.getElementById("getDucosButton").disabled = false; 

      
    })

}

