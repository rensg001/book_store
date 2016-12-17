/**
 * Created by renshangui on 16/12/17.
 */

/**
 * 初始化分页列表
 *
 */

function init_book(cover, book_name, blurb) {
    var book = $("#book-demo").clone();
    book.appendTo("#page-content");
    book.find("div.pictogram").find("img").attr("src", cover);
    book.find("div.blurb").find("a").text(book_name);
    book.find("div.blurb").find("small").text(blurb);
    book.removeClass("hide");
}

function init_book_list(resp) {
    var list = resp.data.list;
    $("#page-content").empty();
    for (var index in list) {
        var book = list[index];
        if (book.hasOwnProperty("cover")
            && book.hasOwnProperty("name")
            && book.hasOwnProperty("blurb")) {
            init_book(book.cover, book.name, book.blurb);
        }
    }
}

var $pagination = $("#pagination");
var defaultOpts = {
    first: "首页",
    last: "尾页",
    prev: "上一页",
    next: "下一页"
};
var page_size = "2";
$pagination.twbsPagination(defaultOpts);

function init_paginator(resp) {
    init_book_list(resp);
    var totalPages = resp.data.total_page;
    var currentPage = $pagination.twbsPagination('getCurrentPage');


    $pagination.twbsPagination('destroy');
    $pagination.twbsPagination($.extend({}, defaultOpts, {
        startPage: currentPage,
        totalPages: totalPages,
        initiateStartPageClick: false,

        onPageClick: function (event, page) {
            console.log(event, page);
            $.ajax({
                url: "/book/list?page={page}&page_size={page_size}".replace("{page}", page).replace("{page_size}", page_size),
                method: "get",
                success: init_book_list
            })
        }
    }));
}

$.ajax({
    url: "/book/list?page=1&page_size={page_size}".replace("{page_size}", page_size),
    method: "get",
    success: init_paginator
});

/**
 * 导航栏搜索
 */
function search_form() {
    var form = $(this).parents("form");
    var args = form.formToDict();
    $.ajax({
        url: "/book/list?page=1&page_size={page_size}&name={name}".replace("{name}", args["book_name"]).replace("{page_size}", page_size),
        method: "get",
        success: init_paginator
    })
}

$("#search").click(search_form);

$(document).ready(function () {
    $(window).keydown(function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });
});