var options="";
$("#vzvod").on('change',function(){
    var value=$(this).val();
    options="<option>None</option>"
    options+='{%- for cadet in cadets -%}' +
    '<option value="{{ cadet }}">{{ cadet }}</option>' +
    '{%- endfor -%}';
    $("#vzvods").html(options);
//    else
//        $("#vzvods").find('option').remove()
});

//var options=""; //store the dynamic options
//$("#gender").on('change',function(){ //add a change event handler to gender select
//    var value=$(this).val(); //get its selected value
//    options="<option>Select Your Name</option>"
//    if(value=="Male") //value ==Male then set male required options
//    {
//        options+="<option value='Male1'>Male 1</option>"
//                +"<option value='Male2'>Male 2</option>";
//        $("#name").html(options);
//    }
//    else if(value=="Female") //else set female required options
//    {
//        options+='<option value="female1">Female 1</option>'
//                 +'<option value="female2">Female 2</option>';
//        $("#name").html(options);
//    }
//    else
//        $("#name").find('option').remove() //if first default text option is selected empty the select
//});
