/**
 * Created by renshangui on 16/11/26.
 */
function set_msg(msg) {
    // 设置消息到消息到消息模态框中并显示
    var modal_msg = $("#modal_msg");
    modal_msg.find("#modal_msg_body").text(msg);
    modal_msg.modal("show");
}

function wrap_ajax_on_btn(btn_id, method, url, callback) {
    // 对指定的表单添加事件，使其对系统返回的错误信息做出响应
    var btn = $("#btn_id".replace("btn_id", btn_id));
    var method_upper = method.toUpperCase();
    btn.click(function () {
        var form_data = callback();
        $.ajax({
            method: method_upper,
            url: url,
            data: form_data,
            success: function (resp) {
                if (typeof resp === "object" && resp !== null && !resp.success) {
                    set_msg(resp.message);
                } else if (method_upper === "GET") {
                    $("body").html(resp);
                }
            }
        })
    });
}
