var $DOM = $(document);
$DOM.on('click', '#get_invoices_submit', function() {

	console.log("get invoices clicked");

    company_id = $(".company_id").val();
    $('.invoice_results').empty()
    if(!company_id){
        tmpl = '<p class="text-center"> Company name cannot be empty </p>'
        $('.invoice_results').append(tmpl)
    } else{
        $.ajax({
            type: 'get',
            url: '/get_all_invoices/' + company_id,
            success: function(result) {
                console.log(result);
                $('.invoice_results').append(result)
            }
        });
    }
});

