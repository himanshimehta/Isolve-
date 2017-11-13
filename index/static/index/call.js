{%load static%}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js" ></script>
<script >
   $(document).ready(function() {
     $("#but").click(function(){
        $("#demo").show();
          $("#word").hide();
    });
    $("#but1").click(function(){
        $("#word").show();
        $("#demo").hide();
    });
    $("ul.red li").click(function(){
        var x=this;
       // $(this).addClass("active");
        document.getElementById("text").innerHTML=$(this).text();
    });
    $("ul.red li").hover(function(){
        $(this).css("background-color", "#8adba5");},function(){
            $(this).css("background-color", "white");
        });
    $("#sub").click(function(){
            var x=$("#text").text();
            document.getElementById("ans").innerHTML=x;
            $("#ans").show();
    });

    
});
</script>
