$(function() {
  $('#med_srch_id').keyup(function() {
    $.ajax({
      type: "POST",
      url: "/dawakhana/search_medicine_listing/",
      data: {
        'search_text': $('#med_srch_id').val(),
        'csrfmiddlewaretoken': $("input[name=cscsrfmiddlewaretoken]").val()
      },
      success: searchSuccess,
      dataType: 'html'

    });
  });
});

function searchSuccess(data, textStatus, jqXHR) {
  $('#med_srch_result').html(data);
}