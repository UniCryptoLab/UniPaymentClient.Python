$(document).ready(function () {

    $('#query-result-table').DataTable({
        "searching": false,
        "destroy": true
    });
    //Submit Query Invoice Form
    $('#queryInvoiceForm').submit(function (e) {
        e.preventDefault();
        const formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '/query-invoice',
            data: formData,
            success: function (response) {
                const code = response.code;
                if (code === 'OK') {
                    const data = response.data;
                    $('#query-result-table').DataTable({
                        "searching": false,
                        "destroy": true,
                        "data": data.models,
                        columns: [
                            {data: 'invoice_id'},
                            {data: 'order_id'},
                            {data: 'price_amount'},
                            {data: 'price_currency'},
                            {data: 'pay_amount'},
                            {data: 'pay_currency'},
                            {data: 'paid_amount'},
                            {data: 'status'},
                            {
                                data: 'invoice_url',
                                render: function (data, type, row) {
                                    if (data) {
                                        return '<a href="' + data + '">CheckOut</a>';
                                    }
                                    return '';
                                }
                            }
                        ]
                    });
                } else {
                    alert(response.msg);
                }
            },
            error: function (data) {
                alert(data);
            },
        });
    });

});