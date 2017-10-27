$(document).ready(function(){
	if($('#id_is_section').is(':checked')){
		$('#id_mark').parents('p').hide();
		$('#id_total').parents('p').hide();
	}

	$('#id_is_section').click(function(){
		$('#id_mark').parents('p').toggle(!this.checked);
		$('#id_total').parents('p').toggle(!this.checked);
	})

	$('#id_assignment_course').change(function(){
	    var course_selected = $('#id_assignment_course option:selected').text()
		$('#section-modal-label').text("Add to " + course_selected);
		var form = $(this).closest('form');
		$.ajax({
			url: form.attr('data-update-assignment-list-url'),
			data: {
			    'course_selected': $('#id_assignment_course option:selected').text()
			},
			dataType: 'json',
			success: function(data){
			    var options = $('#id_assignment_self');
			    options.empty();
			    options.append($('<option />').val('---------').text('---------'));
			    $.each(data.assignments, function(index, assignment){
			        options.append($('<option />').val(assignment.assignment_name).text(assignment.assignment_name));
			    })
			},
			error: function(data){
			    var options = $('#id_assignment_self');
                options.empty();
                options.append($('<option />').val('---------').text('---------'));
			}
		})
	})
})
