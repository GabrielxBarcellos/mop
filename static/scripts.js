$('btn')

function valida_form(classe_ignora){

    $('.erro').removeClass('erro')
    $.each($('[name]'), function (indexInArray, valueOfElement) { 

        console.log($(valueOfElement).hasClass(classe_ignora))
         if  (!$(valueOfElement).hasClass(classe_ignora)){
             if ($(valueOfElement).val()==""){
                $(valueOfElement).addClass('erro');
             } 
             
        
         }
         console.log('p2')
    });
    var erros = $('.erro').length
    console.log('qdt erros:' + erros)

    if (erros >0){
        return false
    }else{
        return true
    }
}