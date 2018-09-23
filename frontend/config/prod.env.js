'use strict'
module.exports = {
  NODE_ENV: '"production"',
  BEERS_API_BASE_URL: JSON.stringify(process.env.BEERS_API_BASE_URL) || '"http://localhost:5000/api"',
  OAUTH_API_BASE_URL: JSON.stringify(process.env.OAUTH_API_BASE_URL) || '"http://localhost:5000/api/oauth"',
  CLIENT_ID: JSON.stringify(process.env.CLIENT_ID) || '"TBD"',
  CLIENT_SECRET: JSON.stringify(process.env.CLIENT_SECRET) || '"TBD"',
  GOOGLE_CLIENT_ID: JSON.stringify(process.env.GOOGLE_CLIENT_ID) || '"TBD"'
}
