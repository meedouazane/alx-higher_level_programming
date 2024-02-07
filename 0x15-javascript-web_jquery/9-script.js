$(document).ready(function () {
  $(function () {
    $.ajax({
      method: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  });
});
