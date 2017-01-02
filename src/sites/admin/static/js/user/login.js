/**
 * Created by renshangui on 2017/1/2.
 */
$(function () {
    $("form").bind("keypress", function (e) {
        if(e.keyCode == 13){
            $(".btn-login").click();
        }
    });
    $(".btn-login").click(act_form);
});