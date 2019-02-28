$(function () {
    console.log('进入发送短信js')
    $('#sendM').click(function () {

        $.ajax({
            type:'get',
            url:'/sendS/',
            data:{'phone':$('#phone').val()},
            success:function (recv) {
                console.log(recv)
            }
        })
    })

    $('#login').click(function () {

        $.ajax({
            type:'get',
            url:'/newlogin/',
            data:{'phone':$('#phone').val(),'yzm':$('#yzm').val()},
            success:function (recv) {
                console.log(recv)
                $('#log').submit()
                // window.open('localhost:8105/upheadimg/',target = '_self')
            }
        })
    })
})
