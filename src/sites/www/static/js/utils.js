/**
 * Created by renshangui on 16/12/3.
 * 表单提交工具
 */


jQuery.fn.formToDict = function() {
    var fields = this.serializeArray();
    var json = {};
    for (var i = 0; i < fields.length; i++) {
        if(!fields[i].name.startsWith("_")){
            json[fields[i].name] = fields[i].value;
        }
    }
    return json;
};

function post_form(){
    // 需要页面包含modal_msg模态框
    var form = $(this).parents("form");
    var args = form.formToDict();
    $.ajax({
        url: form.attr("action"),
        data: args,
        method: "POST",
        success: function(resp){
            //check attributes
            if (typeof resp === "object" && resp !== null){
                var modal_msg = $(".modal_msg");
                if(!resp.success){
                    // show error message on modal
                    modal_msg.find(".modal_msg_body").text(resp.message);
                    modal_msg.modal("show");
                }else{
                    modal_msg.find(".modal_msg_body").text("操作成功");
                    modal_msg.modal("show");
                    setTimeout(location.reload.bind(location), 2000);
                }
            }else{
                // replace page
                $("body").html(resp);

            }
        }
    })
}
