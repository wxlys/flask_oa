function bindEmailCaptchaClick() {
    // 绑定点击事件   event发生位置
  $("#captcha-btn").click(function (event) {
      // 阻止默认的事件
      event.preventDefault();

      //var获取输入框的值
      var email = $("input[name='email']").val();
      // print(email)

      //ajax请求
      $.ajax({
          url: "/auth/captcha/email?email=" + email,
          method: "GET",
          // 回调函数success
          success: function (result) {
                console.log('AJAX 请求成功，返回结果：', result);
                alert("111111111111");
          },
          error: function (error) {
              console.log(error);
              alert("222222222222");
          }
      });
  });
}

// 整个网页加载完成后再执行
$(function () {
  bindEmailCaptchaClick();
});
