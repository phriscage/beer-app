// 
// Chris Page <chrispage@google.com>
// 
// Create dynamic target.url for service callout from variables. 
// TO-DO: Will need to create logic based off third-party IdP names. 
//
var targetUrl = context.getVariable('oauth.openid.google.jwks_uri')
var re = new RegExp('^(https?://[^/]+)(/.*)$');
var match = re.exec(targetUrl);
if (match) {
  context.setVariable('servicecallout.RetriveJWKs.target.url', match[1]);
  context.setVariable('sc_urlPath', match[2]);
}