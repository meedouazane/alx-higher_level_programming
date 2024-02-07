$(document).ready(function () {
  $('#add_item').on('click', add);
  function add () {
    $('.my_list').append('<li>Item</li>');
  }
  $('#remove_item').on('click', remove);
  function remove () {
    $('.my_list li:last-child').remove();
  }
  $('#clear_list').on('click', clear);
  function clear () {
    $('.my_list li').remove();
  }
});
