var applicationIdp = context.getVariable('verifyapikey.VerifyAPIKeyUrl.idp');
// dynamically get the KVM values base 
var faultResponse = {
    fault: {
        faultstring: "DelegationValidation[DelegationValidation]:" +
            "Execution failed. reason: DelegationValidation[DelegationValidation]: ",
        detail: {
            errorcode: "steps.delegatevalidation.ExecutionFailed"
        }
    }
}
try {
    // validate if params 0
    if (context.getVariable(applicationIdp) == null || !context.getVariable(applicationIdp)) {
        faultResponse.fault.faultstring +=
            "No Authorization IdP found ";
        throw faultResponse.fault.faultstring;
    } 
}
catch(err) {
    context.setVariable('delegateValidation.fault', JSON.stringify(faultResponse));
}

var authUrl = context.getVariable(applicationIdp + '.authorization_url');
var wa = context.getVariable(applicationIdp + '.wa');
var wtrealm = context.getVariable(applicationIdp + '.wtrealm');
var wreply = context.getVariable(applicationIdp + '.wreply');
wreply += '?' + context.getVariable('request.querystring');

var redirectUrl = authUrl + '?wa=' + encodeURIComponent(wa) + '&wtrealm=' + encodeURIComponent(wtrealm) + '&wreply=' + encodeURIComponent(wreply);
context.setVariable('redirectUrl', redirectUrl);



