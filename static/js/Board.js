var serverAddress = "127.0.0.1"
var portNumber = "5000"

function display(cell){
    var cellValue = $(cell).children('span').first().html()
    if (cellValue == ''){
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
            },
            error: function (jqXHR, textStatus, errorThrown) {
                statusCode = (jqXHR.status);
            }
        });
        }
    }

}
      
function restoreState(){
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
}