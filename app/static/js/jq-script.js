$('onready', function() {
  var $data = {};
  var $radio_input_names = [];
  var $radio_input_values = [];

  var $div_skill = $('form div#skill-radio');
  var $hidden_field = $('form input[name=skill_set]');
  // var $radio = $('div#skill-radio input[type=radio]');

  $div_skill.each(function (index, element) {
    var radio_input = $(this).find("input[type=radio]");
    var radio_input_name = radio_input.attr("name");

    $data[radio_input_name] = 0;
    $radio_input_names.push(radio_input_name);

    radio_input.click(function() {
      var checked_radio_name = $(this).attr("name");
      $data[checked_radio_name] = $(this).attr("value");

      $hidden_field.val(JSON.stringify($data));
    });
  });

});
