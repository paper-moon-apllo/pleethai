var wordpage = 1;
var examplepage = 1;

$(document).ready(function(){
    LoadWordList();
    LoadExampleList();

    // Change backgroundcolor of selected item
    $(document).on('mouseenter', '.row', function() {
        $(this).css("background", "#f5f5f5");
    });
    $(document).on('mouseleave', '.row', function() {
        $(this).css("background", "#fff");
    });

    // Show detail modal
    $(document).on('click', '.row', function(e) {
        e.preventDefault();
        $( "#detail-modal .modal-content" ).load($(this).attr("href"), function() {
            $("#word-detail-modal").modal("show");
        });
    });

    // load items
    $(document).on('inview', '#wordbottom', function(e, isInView) {
        if (isInView) {
            wordpage++;
            LoadWordList();
        }
    });
    $(document).on('inview', '#examplebottom', function(e, isInView) {
        if (isInView) {
            examplepage++;
            LoadExampleList();
        }
    });
});

// Search
$('#keyword').keyup(function(e) {
    if ( e.which == 13 ) {
         $("#keyword").blur();
    }
    wordpage = 1;
    examplepage = 1;
    $('#wordcontainer').empty();
    $('#examplecontainer').empty();
    LoadWordList();
    LoadExampleList();
});

function LoadWordList() {
    $('#wordloading').show();
    $.ajax({
        'url': 'searchword',
        'type': 'GET',
        'data': {
            'keyword': $('#keyword').val(),
            'page' : wordpage,
        },
        'dataType': 'text'
    }).done( response => {
        $('#wordcontainer').append(response);
    });
    $('#wordloading').hide();
}

function LoadExampleList() {
    $('#exampleloading').show();
    $.ajax({
        'url': 'searchexample',
        'type': 'GET',
        'data': {
            'keyword': $('#keyword').val(),
            'page' : examplepage,
        },
        'dataType': 'text'
    }).done( response => {
        $('#examplecontainer').append(response);
    });
    $('#exampleloading').hide();
}

