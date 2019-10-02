# Marketplace Product Registration Page
VERSION = '0.0.1'
BOTTLEIP = '0.0.0.0'
BOTTLEPORT = '13175'

# Install Requrirements via PIP
from bottle import Bottle, route, get, post, request, response, run, static_file, template # Webserver

#------------------------------------------------------------------
# Setup the Bottle WebServer
#------------------------------------------------------------------
app = Bottle(__name__)

@app.hook('after_request')
def enable_cors():
	  """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
	  response.headers['Access-Control-Allow-Origin'] = '*'
	  response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	  response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

#------------------------------------------------------------------
# Index Endpoint
#------------------------------------------------------------------

# Index Route
@app.route('/', method='GET')
def index():
    print(request)
    return {'status':200, 'response':'Connection to the CloudMage API has been successfully established'}

# Logo Route
# @app.route('/logo', method='GET')
# def logo():
# 	return static_file('images/logo.png', root='.', mimetype='image/png')

# # EULA Route
# @app.route('/eula', method='GET')
# def eula():
# 	return template('eula')

# # Registration Form Route
@app.route('/pr', method='POST')
def MergeRequest():
	
    if 'action' in request.forms:
      pr_action = request.forms.get('action')
      print(pr_action)
      
    if 'number' in request.forms:
      pr_number = request.forms.get('number')
      print(pr_number)

    if 'changes' in request.forms:
      pr_change_obj = request.forms.get('changes')
      print(pr_change_obj)

    if 'pull_request' in request.forms:
      pr_obj = request.forms.get('pull_request')
      print(pr_obj)

    return {'status':200, 'response':'Connection to the CloudMage PR API has been successfully established'}

# # Submit Registration
# @app.route('/process', method='POST')
# def process_registration():
    
#     if 'email' in request.forms:
#         email = request.forms.get('email')

#     if 'username' in request.forms:
#         username = request.forms.get('username')
        
#     if 'password' in request.forms:
#         password = request.forms.get('password')

#     if 'domain_name' in request.forms:
#         domain_name = request.forms.get('domain_name')
    
#     ##### Resolving Customer Registration Token ##### 
#     if 'mp_reg' in request.forms:
#         mptoken = request.forms.get('mp_reg')

#         # Resolve Customer via Marketplace Metering Service
#         marketplaceClient = boto3.client(
#             'meteringmarketplace',
#             region_name='us-east-1'
#             )
        
#         customerData = marketplaceClient.resolve_customer(
#             RegistrationToken=mptoken
#             )
        
#         product_id = customerData['ProductCode']
#         customer_id = customerData['CustomerIdentifier']
    
#     form_data = {
#         "email": email,
#         "username": username,
#         "password": password,
#         "domain_name": domain_name,
#         "mptoken": mptoken,
#         "product_id": product_id,
#         "customer_id": customer_id
#         }

#     # TODO: Validate no other accounts share this identifier
#     # TODO: Store information away with your customer record

#     return template('formdata', form_data=form_data)

#------------------------------------------------------------------ 
# Start the Web Server 
#------------------------------------------------------------------ 
# Run the flask server 
if __name__ == '__main__': 
    app.run(host=BOTTLEIP, port=BOTTLEPORT) 

