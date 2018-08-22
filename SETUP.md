# Beer App - Setup
This documentation provides details for how to setup the Beer App interface and API. You can choice either [SETUP-STAND-ALONE.md](SETUP-STAND-ALONE.md) or [Setup Backend - Hybrid](SETUP-HYBRID.md) for the front-end

* [Setup Frontend](#setup_frontend)
* [Setup Backend - Stand-Alone](SETUP-STAND-ALONE.md)
* [Setup Backend - Hybrid](SETUP-HYBRID.md)


## <a name="setup_frontend"></a>Setup Frontend:
Install the Node packages via NPM (This will be added to a Docker development image in the future)

        cd frontend
        npm install

Build and run the development environment as a Node instance and Docker application locally. You can specify configuration variables if needed via command line.I.E. `CLIENT_ID=1234 npm run dev`. Make changes accordingly.

        npm run dev

Launch browser to UI:

        http://localhost:8080
