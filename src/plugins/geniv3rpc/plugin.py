import amsoil.core.pluginmanager as pm
from g3rpc.genivthree import GENIv3Handler, GENIv3DelegateBase
from g3rpc import exceptions as geni_exceptions

def setup():
    # setup config keys
    config = pm.getService("config")
    # config.Config.install("geniv2rpc.cert_root", "~/.gcf/trusted_roots", "Folder which includes trusted clearinghouse certificates for GENI API v2 (in .pem format)")
    
    # register xmlrpc endpoint
    xmlrpc = pm.getService('xmlrpc')
    geni_handler = GENIv3Handler()
    pm.registerService('geniv3handler', geni_handler)
    pm.registerService('geniv3delegatebase', GENIv3DelegateBase)
    pm.registerService('geniv3exceptions', geni_exceptions)
    xmlrpc.registerXMLRPC('geni3', geni_handler, '/RPC2') # name, handlerObj, endpoint