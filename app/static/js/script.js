$('onready', function(){
  $('form.form div.radio').addClass('radio-inline');

  var $skill_hidden_input = $('input[name=skill]');

  var skillset = [];

  $("button#add-skill").click(function(){
    var skill = $("input[name=user-skill]").val();

    // check for value in input[user-skill]
    if (skill) {

      // skillset.push({skill});
      skillset.push({skill});

      // console.log(JSON.stringify(skillset));


      var table_row_count = $("table tbody tr").length;
      var table_row_id = table_row_count +1;

      // var markup_no = "<td>"+ table_row_id +"</td>";
      var markup_skill = '<td id="skill">'+ skill +'</td>';
      var markup_remove = '<td><button id="btn-remove-row" type="button" class="btn btn-link"> Remove </button></td>';

      var markup_row = '<tr id="table-row-'+table_row_id+'">' +
                        // markup_no +
                        markup_skill +
                        markup_remove +
                        '</tr>';

      // add a row with skill and
      // experience level onto the table
      $("table tbody").prepend(markup_row);

    }
    // clear input
    $("input[name=user-skill]").val("");

    // Find and remove selected table rows
    $("button#btn-remove-row").click(function() {
      var to_remove = $(this).parents("td").siblings("td#skill").text();
      skillset = skillset.filter(function(el) {
        return el.skill !== to_remove;
      });
      $(this).parents("tr").remove();
      $skill_hidden_input.val(JSON.stringify(skillset));
    });

    $skill_hidden_input.val(JSON.stringify(skillset));
  });
});
