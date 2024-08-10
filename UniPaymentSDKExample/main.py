import json

from flask import Flask, render_template, request, flash, redirect, jsonify
from unipayment import Configuration, BillingAPI, CommonAPI, ApiException
from unipayment.models import CreateInvoiceRequest, QueryInvoicesRequest

app = Flask(__name__)
app.config['clientId'] = '74feb539-ba5a-4ae9-b901-4da4fb539574'
app.config['clientSecret'] = 'BsoRhgqzhR1TYMtwTRYdPxBTvR5rxkW9K'
app.config['appId'] = '2a9bd90b-fe95-4659-83cb-04de662fbbac'
app.config['isSandbox'] = True


@app.route("/")
def index():
    return render_template('index.html', title='Create Invoice',
                           clientId=app.config['clientId'],
                           clientSecret=app.config['clientSecret'],
                           appId=app.config['appId'])


@app.route("/create-invoice")
def create_invoice():
    return render_template('index.html', title='Create Invoice',
                           clientId=app.config['clientId'],
                           clientSecret=app.config['clientSecret'],
                           appId=app.config['appId'])


@app.route("/create-invoice", methods=['POST'])
def post_create_invoice():
    client_id = request.form['clientId']
    client_secret = request.form['clientSecret']
    app_id = request.form['appId']

    price_amount = request.form['priceAmount']
    price_currency = request.form['priceCurrency']
    pay_currency = request.form['payCurrency']
    network = request.form['network']
    notify_url = request.form['notifyUrl']
    redirect_url = request.form['redirectUrl']
    order_id = request.form['orderId']
    title = request.form['title']
    description = request.form['description']
    lang = request.form['lang']
    ext_args = request.form['extArgs']
    confirm_speed = request.form['confirmSpeed']

    create_invoice_request = CreateInvoiceRequest(
        app_id=app_id,
        price_amount=price_amount,
        price_currency=price_currency,
        pay_currency=pay_currency,
        pay_network=network,
        notify_url=notify_url,
        redirect_url=redirect_url,
        order_id=order_id,
        title=title,
        description=description,
        lang=lang,
        ext_args=ext_args,
        confirm_speed=confirm_speed)

    print('~~~~~~~')
    config = Configuration()
    config.client_id = client_id
    config.client_secret = client_secret
    config.app_id = app_id
    config.debug = True

    try:
        billing_api = BillingAPI(configuration=config)
        create_invoice_response = billing_api.create_invoice(create_invoice_request)
        if create_invoice_response.code != 'OK':
            flash(create_invoice_response.msg)
        else:
            return redirect(create_invoice_response.data.invoice_url)
    except ApiException as e:
        error_response = json.loads(e.body)
        return render_template('index.html', title='Create Invoice',
                               clientId=app.config['clientId'],
                               clientSecret=app.config['clientSecret'],
                               errorCode=error_response['code'],
                               errorMessage=error_response['msg'])


@app.route("/query-invoice")
def query_invoice():
    return render_template('query-invoice.html', title='Query Invoice',
                           clientId=app.config['clientId'],
                           clientSecret=app.config['clientSecret'],
                           appId=app.config['appId'])


@app.route("/query-invoice", methods=['POST'])
def post_query_invoice():
    client_id = request.form['clientId']
    client_secret = request.form['clientSecret']

    invoice_id = request.form['invoiceId']
    order_id = request.form['orderId']
    status = request.form['status']
    start = request.form['start']
    end = request.form['end']
    page_size = 10
    page_no = 1
    is_asc = request.form['isAsc']

    config = Configuration()
    config.client_id = client_id
    config.client_secret = client_secret
    config.debug = True

    billing_api = BillingAPI(configuration=config)

    query_invoices_request = QueryInvoicesRequest(invoice_id=invoice_id, order_id=order_id, status=status, start=start,
                                                  end=end, page_size=page_size, page_no=page_no, is_asc=is_asc)

    try:
        query_invoice_response = billing_api.query_invoices(query_invoices_request)
        return json.loads(query_invoice_response.to_json())
    except ApiException as e:
        error_response = json.loads(e.body)
        return jsonify(error_response)


@app.route("/privacy")
def privacy():
    return render_template('privacy.html', title='Privacy Policy')


@app.route("/check-notify", methods=['POST'])
def check_notify():
    notify = request.get_json()
    client_id = app.config['clientId']
    client_secret = app.config['clientSecret']

    config = Configuration()
    config.client_id = client_id
    config.client_secret = client_secret
    config.debug = True

    common_api = CommonAPI(configuration=config)
    try:
        check_ipn_response = common_api.check_ipn(notify)
        return jsonify(check_ipn_response.to_dict())
    except ApiException as e:
        error_response = json.loads(e.body)
        return jsonify(error_response)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
