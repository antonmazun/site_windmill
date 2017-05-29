
//
//$(document).ready(function(){
//    $("#add").click(function(){
//        btn = $(this);
//       // alert(btn.attr("value"));
//        $.ajax({type: "POST", url:"/add_comments/", data: {author_name: $("#auth_name").val(), text: $("#text").val(), xhr: true}, success: function(result){
//             let status = jQuery.parseJSON(result);
//                alert("You cool");
//        }});
//    });
//});


function hide_form(){
    var form = document.getElementById("form_review");
        form.style.display = "none";
        
}


function anonim_user(){
    var anonim = document.getElementById("auth_name");
    
    if (anonim == "" ){
        anonim.val = "anonim";
    }
}

//anonim_user();