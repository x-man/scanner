/*$(document).ready(function(){
	$(".sideMenu").click(function(){
		$("#domainInfo").attr('class','');
		$("#subdomainInfo").attr('class','');
		$("#ipInfo").attr('class','');
		$("#portInfo").attr('class','');
		$("#vulnInfo").attr('class','');
		$("#"+this.id).attr('class','active');

		$.getJSON("show/"+this.id,function(data){
			$("#info_table").html("");
			if(this.id == "domainInfo"){
				$("#info_table").html(
					"<tr>\
		                <th>id</th>\
		                <th>域名</th>\
		                <th>所属公司</th>\
		                <th>添加日期</th>\
		                <th>状态</th>\
		                <th>操作</th>\
		            </tr>"
				);

			}else if(){
				$("#info_table").html(
					"<tr>\
                        <th>id</th>\
                        <th>子域名</th>\
                        <th>网站标题</th>\
                        <th>添加日期</th>\
                        <th>所属域名</th>\
                        <th>状态</th>\
                        <th>操作</th>\
                    </tr>"
				);
			}
			else if(){
				$("#info_table").html(
					"<tr>\
                        <th>id</th>\
                        <th>子域名</th>\
                        <th>网站标题</th>\
                        <th>添加日期</th>\
                        <th>所属域名</th>\
                        <th>状态</th>\
                        <th>操作</th>\
                    </tr>"
				);
			}
			else if(){
				$("#info_table").html(
					"<tr>\
                        <th>id</th>\
                        <th>子域名</th>\
                        <th>网站标题</th>\
                        <th>添加日期</th>\
                        <th>所属域名</th>\
                        <th>状态</th>\
                        <th>操作</th>\
                    </tr>"
				);
			}else if(){
				$("#info_table").html(
					"<tr>\
                        <th>id</th>\
                        <th>子域名</th>\
                        <th>网站标题</th>\
                        <th>添加日期</th>\
                        <th>所属域名</th>\
                        <th>状态</th>\
                        <th>操作</th>\
                    </tr>"
				);
			}
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