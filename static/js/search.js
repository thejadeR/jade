(function (c) {
    c.gdhpSearchUI = function (j) {
    };
    var d = true;
    c.gdhpSearchUI.defaults =
        {
            searchUrl: null,
            domainInputId: "#searchDomainName",
            tldInputId: "#searchTldName",
            tldToggleId: "#searchTldToggle",
            tldListId: "#searchTldList",
            searchButton: "#searchButton",
            tldListHighlightColor: "#fedfb7",
            domainInputLabelText: "Search for a new domain",
            initialTld: true
        };
    c.fn.gdhpDomainSearch = function (k) {
        var j = c.extend({}, c.gdhpSearchUI.defaults, k || {});
        c("<div id='searchInputLabel' unselectable='on'>" + j.domainInputLabelText + "</div>").appendTo(c(j.domainInputId).parent());
        c("<style type='text/css'> .t-hilite{ background-color:" + j.tldListHighlightColor + "} </style>").appendTo("head");
        c("#searchInputLabel").bind("click", function (l) {
            c(j.domainInputId).focus()
        }).addClass(c(j.domainInputId).attr("class")).css({
            position: "absolute", color: "#CCCCCC", top: "0px", left: "0px"
        });
        c(j.domainInputId).focus().bind("paste", function (l) {
            a(l, j.domainInputId)
        }).bind("click", function (l) {
            a(l, j.domainInputId)
        }).bind("keypress", function (l) {
            a(l, j.domainInputId)
        }).bind("focus", function () {
            if (c(this).val() === "杈撳叆鎮ㄦ兂娉ㄥ唽鐨勫煙鍚�") {
                c(this).val("")
            }
        }).bind("blur", function (l) {
            if (c(j.domainInputId).val() === "") {
                c("#searchInputLabel").css({
                    display: "block"
                })
            }
        });
        c(j.tldInputId).focus(function () {
            g(j.tldListId, j.tldToggleId)
        }).keyup(function (l) {
            f(this, l, j.tldInputId, j.tldListId, j.tldToggleId)
        }).keydown(function (l) {
            e(this, l, j.tldListId, j.tldToggleId, j.tldInputId)
        });
        c(j.tldToggleId).html("&#9660;").addClass("stoggledown").bind("click", function () {
            g(j.tldListId, j.tldToggleId)
        });
        c(j.tldListId + " li").each(function (l) {
            c(this).bind("click", function () {
                c(j.tldInputId).val(this.innerHTML);
                g(j.tldListId, j.tldToggleId)
            }).bind("mouseover mouseout", function () {
                c(this).toggleClass("t-hilite")
            })
        });

        /*鎸夐挳浜嬩欢
        c(j.searchButton).click(function (m)
        {
            var l = c(j.domainInputId);
            var n = c(j.tldInputId);
            b(j.searchUrl, l, n, j.tldListId);
            m.preventDefault();
            m.stopPropagation()
        })*/
    };

    function g(j, k) {
        if (c(k).hasClass("stoggledown")) {
            c(k).html("&#9650;").removeClass("stoggledown").addClass("stoggleup")
        }
        else {
            c(k).html("&#9660;").removeClass("stoggleup").addClass("stoggledown")
        }
        c(j).toggle()
    }
})(jQuery);