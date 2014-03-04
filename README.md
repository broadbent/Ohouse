# The Clearinghouse

This is/shall a Clearinghouse for all the projects mentioned.

## Installation

### Environment

This software is based on AMsoil, please refer to the [installation guide there](https://github.com/fp7-ofelia/amsoil/wiki/Installation).  
Please follow at least the "Base" and "Plugins" steps.

**Troubleshooting** Fire up the server via `python src/main.py` and install the packages which are not found.
Note that sometimes the output is only given to the log in `log/amsoil.log`.

### Additional

* Copy the `deploy/config.json.example` to `deploy/config.json` and adjust the entries (should be self-explanatory).
* Either
  * Install trust root certificates to `deploy/trust` (as pem) and a admin cert (`admin-key.pem` and `admin-cert.pem`) to `admin`.
  * Or create test certificates and credentials and copy them to the respective places (see `test/creds/TODO.md`).
* Run the server with `python src/main.py`
* In a new cosole run the config client `python admin/config_client.py --interactive` and make change according to your setup

### Test drive

You may run the `xx_tests.py` scripts in `test/unit` to make sure everything works fine.
The test scripts assume that there are test certificates and credentials in `test/creds` (for creating them please see `test/creds/TODO.md`).

<<<<<<< HEAD
=======

>>>>>>> 887a4f9b32f1f4bcfd02e7656a70b47734b44874
## Architectural decisions

* Please see the `ofed` - `plugin.py` for considerations on how to protect information regarding authZ.
