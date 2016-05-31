function sample2() {
	$.getJSON('data.json', function(data) {
		var template = "<h1>{{firstName}} {{lastName}}</h1>Blog: {{blogURL}}";
		var html = Mustache.to_html(template, data);
		$('#sampleArea').html(html);
	});
}