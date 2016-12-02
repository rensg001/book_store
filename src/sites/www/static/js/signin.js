/**
 * Created by renshangui on 16/11/27.
 */
//    function get_login_form_data() {
//        var login_form = $("#login_form");
//        var name = login_form.find("input[name='name']").val();
//        var passwd = login_form.find("input[password='passwd']").val();
//    }
//    var login_data = get_login_form_data();

function get_signup_form_data() {
    var data = {};
    var signup_form = $("#signupform");
    data.login_id = signup_form.find("input[name='login_id']").val();
    data.password = signup_form.find("input[name='password']").val();
    data.email = signup_form.find("input[name='email']").val();
    data.name = signup_form.find("input[name='name']").val();
    data.nickname = signup_form.find("input[name='nickname']").val();
    data.gender = signup_form.find("input[name='gender']:checked").val();
    data.mobile = signup_form.find("input[name='mobile']").val();
    data.birthday = signup_form.find("input[name='birthday']").val();
    data.address = signup_form.find("input[name='address']").val();
    return data;
}

$(function () {
    // datetime picker
    $('.form_date').datetimepicker({
        language:  'zh-CN',
        weekStart: 1,
        todayBtn:  1,
		autoclose: 1,
		todayHighlight: 1,
		startView: 2,
		minView: 2,
		forceParse: 0,
        format: 'yyyy-mm-dd'
    });

    var url = $("#signupform").attr("action");
    wrap_ajax_on_btn("btn-signup", "POST", url, get_signup_form_data);
});

