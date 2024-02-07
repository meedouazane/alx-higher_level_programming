$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('#btn_translate').click(function () {
    const language = $('#language_code').val();
    $.get(url + $.param({ lang: language }), function (data) {
      $('#hello').html(data.hello);
    });
  });
});
