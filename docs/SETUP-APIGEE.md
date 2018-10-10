# Beer App - Setup Apigee
This documentation provides details for configuring the Beer App Apigee resource components into your [Apigee](https://apigee.com) organization for OAuth Authorization, configuration, and coresponding API products. We will leverage Apigee's NPM module, [Edge Launchpad](https://github.com/apigee/edge-launchpad) and [Gulp.js](https://gulpjs.com/) that wraps the Apigee Management API. 

* [Setup Apigee_Prerequisites](#setup_apigee_prerequisites)
* [Setup Apigee_resources](#setup_apigee_resources)


## <a name="setup_apigee_prerequisites">Setup Apigee Prerequisites</a>
These instructions will setup the Apigee [Edge Launchpad](https://github.com/apigee/edge-launchpad) and [Gulp.js](https://gulpjs.com/) 

Change directories into the Apigee [directory](../apigee)

        cd apigee

Install NPM modules and Gulp-cli

        npm install 
        npm install -g gulp-cli
        

## <a name="setup_apigee_resources">Setup Apigee Resources</a>
These instructions will provision the following Apigee resource components into your Apigee organization:

* OAuth Authorization Proxy *oauth-jwt-profile*
* OAuth Core configuration KVM *oauth-jwt-profile.core*
* OAuth Keys configuration KVM *oauth-jwt-profile.keys*
* Beer App Products *beer-app-sandbox*, *beer-app-gold*

Change directories into the Apigee [directory](../apigee)

        cd apigee

Set your Organization, Environment, and Username environment variables

        export APIGEE_ORG=<apigee organization name>
        export APIGEE_ENV=<apigee environment name>
        export APIGEE_USERNAME=<apigee org admin username>


Run the *gulp* command with the *deploy* method and verify everything is successful

        gulp deploy --org $APIGEE_ORG --env $APIGEE_ENV --username $APIGEE_USERNAME
        

## <a name="next"></a>Next:

* Try some of the [labs](../labs)


## <a name="cleanup"></a>Cleanup:
Let's cleanup everything for a fresh start

        gulp clean --org $APIGEE_ORG --env $APIGEE_ENV --username $APIGEE_USERNAME
