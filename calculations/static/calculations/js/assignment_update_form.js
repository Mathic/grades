//hide_page = true;
$(document).ready(function(){
	if($('#id_is_section').is(':checked')){
		$('#id_mark').parents('p').hide();
		$('#id_total').parents('p').hide();
	}else{
		$('#id_mark').parents('p').show();
		$('#id_total').parents('p').show();
	}
	/*$('#id_is_section').click(function(){
		hide_page = !hide_page;
		if(hide_page){
			$('#id_mark').parents('p').hide();
			$('#id_total').parents('p').hide();
		}else{
			$('#id_mark').parents('p').show();
			$('#id_total').parents('p').show();
		}
		
		if($('#id_is_section').is(':checked')){
			$('#id_mark').parents('p').hide();
			$('#id_total').parents('p').hide();
		}else{
			$('#id_mark').parents('p').show();
			$('#id_total').parents('p').show();
		}
		$('#id_mark').parents('p').toggle(!this.checked);
		$('#id_total').parents('p').toggle(!this.checked);
		
	})*/
})
