'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  API_BASE_URL: JSON.stringify(process.env.API_BASE_URL) || '"http://localhost:5000/api"',
  CLIENT_ID: JSON.stringify(process.env.CLIENT_ID) || '"TBD"',
  GOOGLE_CLIENT_ID: JSON.stringify(process.env.GOOGLE_CLIENT_ID) || '"TBD"'
})
