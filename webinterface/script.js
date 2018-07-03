export function sendImg() {
	console.log("test");
	var value = $( "#previewImg" ).attr('src');
	console.log(value);
	if ($(value).val() != 0) {
	$.post("server.php", {
	    variable:value
	}, function(data) {
	    if (data != "") {
	        //alert('We sent Jquery string to PHP : ' + data);
	    }
	});
	}
}
