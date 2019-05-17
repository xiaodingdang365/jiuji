function search() {
   var parm = $('#search_content').val()
    $.post('/search/',{'q':parm},function (result) {

    })
}