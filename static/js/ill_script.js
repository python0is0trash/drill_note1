$(document).ready(function() {
$("#addButton").click(function() {
  var copy = $(".input").first().clone();
  copy.find(".removeButton").click(function() {
    $(this).closest(".input").remove(); // Удаление элемента при нажатии на кнопку
  });
  $(".input").last().after(copy);
});
});

$(document).ready(function() {
$("#addButton1").click(function() {
  var copy = $(".input1").first().clone();
  copy.find(".removeButton1").click(function() {
    $(this).closest(".input1").remove(); // Удаление элемента при нажатии на кнопку
  });
  $(".input1").last().after(copy);
});
});

$(document).ready(function() {
$("#addButton2").click(function() {
  var copy = $(".input2").first().clone();
  copy.find(".removeButton2").click(function() {
    $(this).closest(".input2").remove(); // Удаление элемента при нажатии на кнопку
  });
  $(".input2").last().after(copy);
});
});

$(document).ready(function() {
$("#addButton3").click(function() {
  var copy = $(".input3").first().clone();
  copy.find(".removeButton3").click(function() {
    $(this).closest(".input3").remove(); // Удаление элемента при нажатии на кнопку
  });
  $(".input3").last().after(copy);
});
});
