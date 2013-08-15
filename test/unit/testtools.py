#!/usr/bin/env python

import sys
import os.path
import xmlrpclib

class SafeTransportWithCert(xmlrpclib.SafeTransport): 
    """Helper class to force the right certificate for the transport class."""
    def __init__(self, key_path, cert_path):
        xmlrpclib.SafeTransport.__init__(self) # no super, because old style class
        self._key_path = key_path
        self._cert_path = cert_path
        
    def make_connection(self, host):
        """This method will automatically be called by the ServerProxy class when a transport channel is needed."""
        host_with_cert = (host, {'key_file' : self._key_path, 'cert_file' : self._cert_path})
        return xmlrpclib.SafeTransport.make_connection(self, host_with_cert) # no super, because old style class

def ssl_call(method_name, params, endpoint, key_path='alice-key.pem', cert_path='alice-cert.pem', host='127.0.0.1', port=8001):
    key_path = os.path.abspath(os.path.expanduser(key_path))
    cert_path = os.path.abspath(os.path.expanduser(cert_path))
    if not os.path.exists(key_path) or not os.path.exists(cert_path):
        raise RuntimeError("Key or cert file not found")
    transport = SafeTransportWithCert(key_path, cert_path)
    proxy = xmlrpclib.ServerProxy("https://%s:%s/%s" % (host, str(port), endpoint), transport=transport)
    # return proxy.get_version()
    method = getattr(proxy, method_name)
    
    return method(*params)