$(document).ready(function(){
	$('add_domain').click(function(){
		var domain = $("domain").text();
		var company = $("company").text();
		var data = {'domain':domain, 'company':company};
		$.post("{% url 'infocollector:collect' %}",data,function(data,status){
			alert(data);
		});
	});
});