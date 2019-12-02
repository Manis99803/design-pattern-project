var serverAddress = "127.0.0.1"
var portNumber = "5000"

function raiseError(errorMessage){
    $("#outputFeedback").css("display", "block");
    $("#outputFeedback").html(errorMessage);
}

function extractParameters(userObject){
    userObject["name"] = $("#name").val()
    userObject["password"] = $("#password").val()
    return userObject;
}

function checkForAllParameters(userObject){
    if(userObject["name"] == '')
        return false;
    if(userObject["password"] == '')
        return false;
    return true;
}

$("#userSignup").on('click', function() {
    var userObject = {}
    userObject = extractParameters(userObject);
    if (checkForAllParameters(userObject)){
        $.ajax({
            url: 'http://' + serverAddress + ':' + portNumber + '/api/v1/user_signup',
            dataType: "json",
            type: "POST",
            contentType: "application/json",
            xhrFields: { withCredentials: false },
            crossDomain: true,
            data: JSON.stringify(userObject),
            success: function (data) {
                window.location.href = 'http://' + serverAddress + ':' + portNumber + '/login'
            },
            error: function (jqXHR, textStatus, errorThrown) {
                raiseError("User name already exist");
            }
        });
    }
})
      