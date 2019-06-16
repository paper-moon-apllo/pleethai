var wordPage = 1;
var examplePage = 1;

$(document).ready(function(){
    loadWordList();
    loadExampleList();

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
            wordPage++;
            loadWordList();
        }
    });
    $(document).on('inview', '#examplebottom', function(e, isInView) {
        if (isInView) {
            examplePage++;
            loadExampleList();
        }
    });
});

// Search
$('#keyword').keyup(function(e) {
    if ( e.which == 13 ) {
         $("#keyword").blur();
    }
    wordPage = 1;
    examplePage = 1;
    $('#wordcontainer').empty();
    $('#examplecontainer').empty();
    loadWordList();
    loadExampleList();
});

function loadWordList() {
    $('#wordloading').show();
    $.ajax({
        'url': 'searchword',
        'type': 'GET',
        'data': {
            'keyword': $('#keyword').val(),
            'page' : wordPage,
        },
        'dataType': 'text'
    }).done( response => {
        $('#wordcontainer').append(response);
    });
    $('#wordloading').hide();
}

function loadExampleList() {
    $('#exampleloading').show();
    $.ajax({
        'url': 'searchexample',
        'type': 'GET',
        'data': {
            'keyword': $('#keyword').val(),
            'page' : examplePage,
        },
        'dataType': 'text'
    }).done( response => {
        $('#examplecontainer').append(response);
    });
    $('#exampleloading').hide();
}

