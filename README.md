# JARPC clients #

---------
origin - https://git.angrydev.ru/public_repos/jarpc-clients/-/tree/v0.2/

JARPC client's factories with predefined transports for libraries: cabbage, aiohttp, requests.


## Installation ##
```
# Example for version 0.1:
pip install git+http://git.angrydev.ru/public_repos/jarpc-clients.git@v0.1#egg=jarpc_clients==0.1
```

## Usage ##

1) Choose desired transport and install required packages (this library's installation doesn't include transport-dependent packages);
2) Use factory to create JARPC client or use transport separately:

```python
>>> from jarpc_clients import create_cabbage_client
>>>
>>> amqp_rpc = ...
>>> client = create_cabbage_client(amqp_rpc=amqp_rpc, exchange='exchange_name', default_ttl=30.0)
>>> result = client(method='method_name', params=dict(param1=1))
>>> result = client.method_name(param1=1)
```

```python
>>> from jarpc import JarpcClient
>>> from jarpc_clients import RequestsTransport
>>>
>>> transport = RequestsTransport(url='http://example.com/jarpc')
>>> client = JarpcClient(transport=transport)
>>> result = client(method='method_name', params=dict(param1=1))
>>> result = client.method_name(param1=1)
>>> transport.close_session()
```
