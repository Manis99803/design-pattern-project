var serverAddress = "127.0.0.1"
var portNumber = "5000"


function displayMessage(message) {
    $("#outputFeedback").css("display", "block");
    $("#outputFeedback").html(message);
}

function checkNumber(value){
    if(!isNaN(value)){
        value = parseInt(value);
        if(value >=1 && value <= 9)
            return true;
        else
            return false;
    } else {
        return false;
    }
}

function display(cell){
    var cellValue = $(cell).children('span').first().html()
    if (cellValue == '' && checkNumber(cellValue)){
        var value = prompt("Enter Value")
        console.log($(cell).attr('data-value'))
        if (value != null) {
        cellData = $(cell).attr('data-value').split(" ")
        console.log(cellData)
        var cellObject = {}
        cellObject[cellData[0].trim()] = cellData[1].trim()
        cellObject[cellData[2].trim()] = cellData[3].trim()
        cellObject[cellData[4].trim()] = cellData[5].trim()
        cellObject[cellData[6].trim()] = cellData[7].trim()
        cellObject["value"] = value.trim()
        console.log(cellObject)
        $.ajax({
            url: 'http://' + serverAddress + ':' + portNumber + '/api/v1/set_cell_value',
            dataType: "json",
            type: "POST",
            contentType: "application/json",
            xhrFields: { withCredentials: false },
            crossDomain: true,
            data: JSON.stringify(cellObject),
            success: function (data) {
                $(cell).first().html(value)
                if (data["message"] == "1"){
                    displayMessage("Winner Winner Chicken Dinner")
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                statusCode = (jqXHR.status);
            }
        });
        }
    }

}
      
$("#restoreState").on('click', function(){
    $.ajax({
        url: 'http://' + serverAddress + ':' + portNumber + '/api/v1/restore_previous_state',
        dataType: "json",
        type: "POST",
        contentType: "application/json",
        xhrFields: { withCredentials: false },
        crossDomain: true,
        success: function (data) {
            expression = '[data-value="squareNumber ' +  data["squareNumber"] + " cellNumber " + data["cellNumber"] + " rowNumber "
                + data["rowNumber"] + " columnNumber " + data["columnNumber"] + '"]'
            $("li").filter(expression).html(data["value"])
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log("Can't Undo any more")
        }
    });
})

$("#saveGame").on('click', function() {
    console.log("In save game function");
    cellElements = $("li").children('span')
    rowElements = []
    row = []
    for(var i = 0; i <= 81; i++){
        row.push($(cellElements[i]).html())
        if ((i + 1) % 9 == 0) {
            rowElements.push(row)
            row = []
        }
    }
    $.ajax({
        url: 'http://' + serverAddress + ':' + portNumber + '/api/v1/save_game',
        dataType: "json",
        type: "POST",
        contentType: "application/json",
        xhrFields: { withCredentials: false },
        crossDomain: true,
        data : JSON.stringify(rowElements),
        success: function (data) {
            console.log("Game saved")
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log("Can't Undo any more")
        }
    });


})