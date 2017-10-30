$(document).ready(function(){
	if($('#id_is_section').is(':checked')){
		$('#id_mark').parents('p').hide();
		$('#id_total').parents('p').hide();
		$('#id_assignment_self').parents('p').hide();
	}

	$('#id_is_section').click(function(){
		$('#id_mark').parents('p').toggle(!this.checked);
		$('#id_total').parents('p').toggle(!this.checked);
		$('#id_assignment_self').parents('p').toggle(!this.checked);
	})

    $('#id_percentage').change(function(){
    	var form = $(this).closest('form');
    	var course_selected = $('#id_assignment_course option:selected').text();
        $.ajax({
        	url: form.attr('data-check-percent-url'),
        	data: {
        	    'course_selected': course_selected,
        		'current_percentage': $('#id_percentage').val()
        	},
        	dataType: 'json',
        	success: function(data){
                if(!data.is_valid){
                    alert('Over a hundred!');
                }
        	},
        	error: function(data){
        		alert(data.responseText);
        	}
        })
    })

	$('#id_assignment_course').change(function(){
		var form = $(this).closest('form');
	    var course_selected = $('#id_assignment_course option:selected').text();
		$('#section-modal-label').text("Add to " + course_selected);
		$.ajax({
			url: form.attr('data-update-assignment-list-url'),
			data: {
			    'course_selected': course_selected
			},
			dataType: 'json',
			success: function(data){
			    $('#id_assignment_self').empty();
			    $('#id_assignment_self').append($('<option />').val('---------').text('---------'));
			    $.each(data.assignments, function(index, assignment){
			        $('#id_assignment_self').append($('<option />').val(assignment.assignment_name).text(assignment.assignment_name));
			    })
			},
			error: function(data){
                $('#id_assignment_self').empty();
                $('#id_assignment_self').append($('<option />').val('---------').text('---------'));
                alert(data.responseText)
			}
		})
	})
})
