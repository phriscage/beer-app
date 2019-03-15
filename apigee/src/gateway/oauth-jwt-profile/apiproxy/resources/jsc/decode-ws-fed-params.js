 // parse url query string and seat as object
function parse_query_string(query) {
  var vars = query.split("&");
  var query_string = {};
  for (var i = 0; i < vars.length; i++) {
    var pair = vars[i].split("=");
    var key = decodeURIComponent(pair[0]);
    var value = decodeURIComponent(pair[1]);
    // If first entry with this name
    if (typeof query_string[key] === "undefined") {
      query_string[key] = decodeURIComponent(value);
      // If second entry with this name
    } else if (typeof query_string[key] === "string") {
      var arr = [query_string[key], decodeURIComponent(value)];
      query_string[key] = arr;
      // If third or later entry with this name
    } else {
      query_string[key].push(decodeURIComponent(value));
    }
  }
  return query_string;
}

// extract the wresult content
var wresult = decodeURIComponent(context.getVariable("apigee.wresult"));
var wa = decodeURIComponent(context.getVariable("apigee.wa"));
var wpreply = decodeURIComponent(context.getVariable("apigee.wpreply"));

var referer = parse_query_string(context.getVariable("request.header.Referer"));
if ('wreply' in referer) {
    context.setVariable('apigee.referer.wreply', referer.wreply);
}
if ('wctx' in referer) {
    context.setVariable('apigee.referer.wctx', referer.wctx);
}