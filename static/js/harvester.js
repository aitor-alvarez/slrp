// harvester.js
jQuery(function($) {
	// $("div.radio").click(function () {
	// 	$(this).parent().removeClass("required");
	// });

	$("#collection_form").submit(function () {
		var repo = $("#repo").val();
		var postdata = $(".collection").serializeArray();
		console.log("POSTDATA:" + postdata);
		$.post("/harvest/repository/"+repo, postdata, function(data) {
			for(i in data) {
				console.log(i);
			}
		});	
	});

	$("#harvest_btn").click(function() {

		$('#modalwait').modal('show')
		$.get("{% url 'oai_harvest_collection' object.identifier %}", function(data) {
			console.log(data);
			$('#modalwait').modal('hide')
		});
		// $("#spinwait").css("display", "inline");
	});


	$(document).ready(function() {
		
	});
});
