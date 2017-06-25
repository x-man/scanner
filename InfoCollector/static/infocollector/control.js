/*$(document).ready(function(){
	$("#add_rule").click(function(){
		var app = $("#app").val();
		var app_description = $("#app_description").val();
		var rule_kind = $("#rule_kind").val();
		var rule_type = $("#rule_type").val();
		var target = $("#target").val();
		var content = $("#content").val();
		var csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
		var url = "{% url 'infocollector:addWebFingerprint' %}";
		alert(url);
		var params = {
			'app':app,
			'app_description':app_description,
			'rule_kind':rule_kind,
			'rule_type':rule_type,
			'target':target,
			'content':content,
			'csrfmiddlewaretoken':csrfmiddlewaretoken
		};
		$.post(url, params,function(data,status){
			alert('ok');
		});
	});
});*/
function changeSideMenuStatus(menu){
	$("#domainInfo").attr('class','');
	$("#subdomainInfo").attr('class','');
	$("#ipInfo").attr('class','');
	$("#portInfo").attr('class','');
	$("#vulnInfo").attr('class','');
	$("#"+menu).attr('class','active');
}