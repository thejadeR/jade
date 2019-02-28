$(document).ready(function(){
		 $(".table_list tr").mouseover(function(){
		 $(this).addClass("over");}).mouseout(function(){
		 $(this).removeClass("over");})
		 /*$(".message_list tr:even").addClass("alt");*/
	});

//澶嶉€夋鍏ㄩ€�
function chooseAll(multiChk){
	if(multiChk[0].checked==false)
	{
		for (i=1;i<multiChk.length;i++)
		{
		   multiChk[i].checked = false;
		}
	}
	else
	{
		for (i=1;i<multiChk.length;i++)
		{
		   multiChk[i].checked = true;
		}
	}
}