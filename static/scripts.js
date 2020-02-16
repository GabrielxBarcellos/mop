

function valida_form(classe_ignora){

    $('.erro').removeClass('erro')
    $.each($('[name]'), function (indexInArray, valueOfElement) { 

        console.log($(valueOfElement).hasClass(classe_ignora))
         if  (!$(valueOfElement).hasClass(classe_ignora)){
             if ($(valueOfElement).val()==""){
                $(valueOfElement).addClass('erro');
             } 
             
        
         }
    });

    $('.erros li').remove()
    if ($('.erro').length >0){
      //adiciona mostra erro
      $.each($('.erro'), function (indexInArray, valueOfElement) { 
        input_err = $(valueOfElement).attr('name')
        msg_err = $('<li>').text(input_err + ' não preenchido') 
        $('.erros').append(msg_err)
         
      });
        return false
    }else{
        return true
    }
}

function download_csv(csv_string){
    
    var universalBOM = "\uFEFF";
    var a = window.document.createElement('a');
    a.setAttribute('href', 'data:text/csv; charset=utf-8,' + encodeURIComponent(universalBOM+csv_string));
    a.setAttribute('download', 'mop.csv');
    window.document.body.appendChild(a);
    a.click();
}


function trazer_option(select ,item_banco ,url_back, pai, pai2){
    if (pai2 == null){
      var el = pai
    }else{
      var el = pai2
    }
    $(el).change(function(){
  
      if (pai2 == null){
        var json = {dado:$(pai).val()}
      }else{
        var json = {dado:$(pai).val(), dado2:$(pai2).val()}
      }
      $.ajax({
        url: url_back,
        data: json,
        type: 'POST',
        success: function(response){
          $( select + " .del" ).remove()
          $.each(response, function(i,v){
            var valor = v[item_banco]
            console.log(valor)
            var option = $('<option>',{
              'val': valor,
              'text':valor,
              'class':'del'})
            $(select).append(option)
            
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems);
          })
    
        }
    })
    })
  }