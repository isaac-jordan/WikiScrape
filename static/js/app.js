$(document).foundation();

$('#search').keyup(function(e) {
	var query = $(this).val();

	$.ajax({
		type: "POST",
		url:"/ajaxSuggest/",
		data: "search=" + query
	}) .done(function( data ) {
		var response = "Suggestions: ";
		var i;
		for (i=0;i<data.length;++i) {
			response = response + "<a>" + data[i] + "</a>, "
		}
		$('#suggestions').html(response);
	});
});
