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




function download_csv(csv_string){
    
    var universalBOM = "\uFEFF";
    var a = window.document.createElement('a');
    a.setAttribute('href', 'data:text/csv; charset=utf-8,' + encodeURIComponent(universalBOM+csv_string));
    a.setAttribute('download', 'example.csv');
    window.document.body.appendChild(a);
    a.click();
}
download_csv(texto)