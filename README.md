# Using HTTP proxy in Python

This repo contains example code for using HTTP proxy in Python.

Once you have the Proxy URL from Enzoguard's [Cloud console](https://cloud.enzoguard.com), set the following environment variables:

```bash
HTTP_PROXY="https://test-app:snipped@pe2xqel.enzoproxy.com"
HTTPS_PROXY="https://test-app:snipped@pe2xqel.enzoproxy.com"
```

Once set, run the Python program:

```bash
python3 main.py
```

You will see IP address of the proxy instead of the IP address of your workstation.

To skip the proxy, you can unset the environment variable or launch a new shell and run the program again.

> Warning: Please note that Enzoguard uses TLS for proxy connection for security reasons.
This is supported only in newer versions of requests and urllib3 library. Please make
sure that requests library is version 2.31.0 or above and urllib3 is version 2.1.0 or above.

## Questions

If you have any questions, please open a GitHub issue or reach out to Enzoguard support.
