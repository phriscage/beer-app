 //
// Chris Page <chrispage@google.com>
//
// Validate the parameters based off whitelist and protect against length and names
//
var requiredParams = ["scope", "response_type", "client_id", "redirect_uri"];
var optionalParams = ["state", "nonce", "prompt", "id_token_hint", "response_mode"];
var customParams = ["x-client-ver", "x-client-SKU"];
var whiteListParams = requiredParams.concat(optionalParams.concat(customParams));
var requestParams = context.getVariable('request.queryparams.names').toArray();
var faultResponse = {
    fault: {
        faultstring: "ParameterValidation[ParameterValidation]:" +
            "Execution failed. reason: ParameterValidation[ParameterValidation]: ",
        detail: {
            errorcode: "steps.parametervalidation.ExecutionFailed"
        }
    }
}
try {
    // validate if params 0
    if (requestParams.length === 0 || requestParams.length < requiredParams.length) {
        faultResponse.fault.faultstring +=
            "Not enough valid parameters found " + requiredParams;
        throw faultResponse.fault.faultstring;
    } 
    // validate number of parameters
    if (requestParams.length > whiteListParams.length) {
        faultResponse.fault.faultstring += requestParams.length +
            " parameter(s) is greater than " + whiteListParams.length;
        throw faultResponse.fault.faultstring;
    } 
}
catch(err) {
    context.setVariable('parameterValidation.fault', JSON.stringify(faultResponse));
}

// validate name of parameters
for (var i = 0; i < requestParams.length; i++) {
    for (var j = 0; j < whiteListParams.length; j++) {
        var valid = false;
        if (whiteListParams[j].toLowerCase() == requestParams[i].toLowerCase()) {
            valid = true;
            break;
        }
    }
    if (!valid) {
        print("bad param: " + requestParams[i].toLowerCase())
        faultResponse.fault.faultstring += "'" + requestParams[i] + "'" +
        " is not a valid parameter."
        context.setVariable('parameterValidation.fault', JSON.stringify(faultResponse));
        break;
    }
}