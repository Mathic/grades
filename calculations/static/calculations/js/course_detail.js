$(document).ready(function(){
    var button = $(this).closest('button');

    $('button[id^="view_assignment_"').click(function(){
        var name = $(this).closest('tr').find('td:eq(0)').text();
        var section_name = name.replace(/[^\w]/g,'');

        $.ajax({
            type: 'GET',
            url: button.attr('data-view-assignment'),
            data: {
                'section_name': section_name
            },
            dataType: 'json',
            success: function(data){
                alert(url)
            },
            error: function(data){

            }
        })
    })
})
