var SERVER_ERROR_MESSAGE = "An unexpected error occurred while communicating the server."
var NO_RESULT_MESSAGE = "No results found.";
var WAIT_TIME = 500;

var wordPage = 0;
var examplePage = 0;
var holdFlag = false;
var clearFlag = false;
var inputTimer;
var clickTimer;

$(document).ready(function(){
    loadWordList();
    loadExampleList();
    loadTagList();

    // Change backgroundcolor of selected item
    $('#searchcontainer').on('mouseenter', '.row-word, .row-example', function() {
        $(this).addClass('bg-light');
    })
    .on('mouseleave', '.row-word, .row-example', function() {
        $(this).removeClass('bg-light');
    })

    // Show detail modal *dont show when hold
    .on('mousedown', '.row-word, .row-example', function() {
        holdFlag = false;
        clickTimer =setTimeout(function(){
            holdFlag = true;
        }, 350);
    })
    .on('mouseup', '.row-word, .row-example', function() {
        if (clickTimer) {
            clearTimeout(clickTimer);
        }
        // If selected text, return
        if(window.getSelection) {
            selectedStr = window.getSelection().toString();
            if(selectedStr !== '' && selectedStr !== '\n') {
              return;
            }
        }
        if (!holdFlag) {
            $( "#detail-modal .modal-content" ).load($(this).attr("href"), function() {
                $("#detail-modal").modal("show");
            });
        }
    });

    // Show tags modal
    $(document).on('click', '#tagbutton', function() {
        $("#tag-modal").modal("show");
    });

    // Create toggles
    $('#tag-modal').on('shown.bs.modal', function() {
        $('.tag-toggle').bootstrapToggle();
    })

    // Search by change toggle
    .on('change', '.tag-toggle', function(e) {
        if (!clearFlag) {
            search();
        }
    });
  

    // load items
    $('#searchcontainer').on('inview', '#wordbottom', function(e, isInView) {
        if (isInView && $('.row-word').length >= 20) {
            loadWordList();
        }
    })
    .on('inview', '#examplebottom', function(e, isInView) {
        if (isInView && $('.row-example').length >= 20) {
            loadExampleList();
        }
    });
});

// Search
$('#keyword').on('input', function(e) { 
    if (e.type == 'keyup' && e.which == 13) {
        //if not pc, hide keyboard
        if (navigator.userAgent.match(/(iPhone|iPad|iPod|Android)/i)) {
            $("#keyword").blur();
        }
        //If hit enter key, not staart timer
        return;
    }
    initTimer();
});

function initTimer() {
    //reset timer
    if (inputTimer) {
        clearTimeout(inputTimer);
    }
    inputTimer = setTimeout(search, WAIT_TIME);
}

function search() {
    wordPage = 0;
    examplePage = 0;
    $('#wordcontainer').empty();
    $('#examplecontainer').empty();
    loadWordList();
    loadExampleList();
}

function loadWordList() {
    $('#wordloading').show();
    wordPage++;
    $.ajax({
        'url': 'searchword',
        'type': 'GET',
        'data': {
            'keyword': $('#keyword').val(),
            'tags' : getTags(),
            'page' : wordPage,
        },
        'dataType': 'text'
    })
    .done( response => {
        if (!response && $('.row-word').length == 0) {
            $('#wordcontainer').append('<div class="alert alert-warning">'
            + NO_RESULT_MESSAGE + '</div>');
        } else if (response) {
            $('#wordcontainer .alert').remove();
            $('#wordcontainer').append(response);
        }
        
    })
    .fail( () => {
        wordPage--;
        $('#wordcontainer').append('<div class="alert alert-danger">'
        + SERVER_ERROR_MESSAGE + '</div>');
    })
    .always( () => {
        $('#wordloading').hide();
    });
}

function loadExampleList() {
    $('#exampleloading').show();
    examplePage++;
    $.ajax({
        'url': 'searchexample',
        'type': 'GET',
        'data': {
            'keyword': $('#keyword').val(),
            'tags' : getTags(),
            'page' : examplePage,
        },
        'dataType': 'text'
    })
    .done( response => {
        if (!response && $('.row-example').length == 0) {
            $('#examplecontainer').append('<div class="alert alert-warning">'
            + NO_RESULT_MESSAGE + '</div>');
        } else if (response) {
            $('#examplecontainer .alert').remove();
            $('#examplecontainer').append(response);
        }
    })
    .fail( () => {
        examplePage--;
        $('#examplecontainer').append('<div class="alert alert-danger">'
        + SERVER_ERROR_MESSAGE + '</div>');
    })
    .always( () => {
        $('#exampleloading').hide();
    });
}

function loadTagList() {
    $('#tagloading').show();
    $.ajax({
        'url': 'tags',
        'type': 'GET',
        'dataType': 'text'
    })
    .done( response => {
        if (!response) {
            $('#tag-modal-content').append('<div class="alert alert-warning">'
            + NO_RESULT_MESSAGE + '</div>');
        } else {
            $('#tag-modal-content .alert').remove();
            $('#tag-modal-content').append(response);
        }
    })
    .fail( () => {
        $('#tag-modal-content').append('<div class="alert alert-danger">'
        + SERVER_ERROR_MESSAGE + '</div>');
    })
    .always( () => {
        $('#tagloading').hide();
    });
}


// Clear tags
function allToggleOff(e) {
    clearFlag = true;
    $('.tag-toggle').bootstrapToggle('off');
    search();
    clearFlag = false;
}

// Get selected tags
function getTags() {
    return $('.tag-toggle:checked').map(function(){
        return $(this).val();
    }).get();
}

