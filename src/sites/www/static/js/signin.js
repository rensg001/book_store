/**
 * Created by renshangui on 16/11/27.
 */

function logout() {
    $.get("/logout",
        function (resp) {
            if (resp.success){
                location.reload();
            }
        }
    )
}

// init bootstrap-fileinput plugin
var btnCust = '<button type="button" class="btn btn-default" title="Add picture tags" ' +
    'onclick="alert(\'Call your custom code here.\')">' +
    '<i class="glyphicon glyphicon-tag"></i>' +
    '</button>';
$("input[name='fileupload']").fileinput({
    overwriteInitial: true,
    maxFileSize: 1500,
    showClose: false,
    showCaption: false,
    browseLabel: '',
    removeLabel: '',
    browseIcon: '<i class="glyphicon glyphicon-folder-open"></i>',
    removeIcon: '<i class="glyphicon glyphicon-remove"></i>',
    removeTitle: 'Cancel or reset changes',
    elErrorContainer: '#kv-avatar-errors-1',
    msgErrorClass: 'alert alert-block alert-danger',
    defaultPreviewContent: '<img src="/static/images/default_avatar.png" alt="Your Avatar" style="width:160px">',
    layoutTemplates: {main2: '{preview} ' + btnCust + ' {remove} {browse}'},
    allowedFileExtensions: ["jpg", "png", "gif", "jpeg"],
    uploadUrl: "/file/upload",
    uploadAsync: true
}).on("filebatchselected", function (event, files) {
    $("input[name='fileupload']").fileinput("upload");
}).on("fileuploaded", function (event, data, id, index) {
    $("input[name='avatar']").val(data.response["data"]["filepath"]);
});

$(function () {
    // datetime picker
    $('.form_date').datetimepicker({
        language: 'zh-CN',
        weekStart: 1,
        todayBtn: 1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        minView: 2,
        forceParse: 0,
        format: 'yyyy-mm-dd'
    });

    $(".btn-submit").click(act_form);

});

