$(document).ready(function(){
    $("#id_query").select2({
        tags: true,
        createTag: function (params) {
            return {
                id: params.term,
                text: params.term,
                newOption: true
            }
        }
    });

    /* convert datetime field to datepicker */

    $('.datepicker').datepicker({
        beforeShow: function() {
            setTimeout(function(){
                $('.ui-datepicker').css('z-index', 99999999999999);
            }, 0);
        }
    });

});